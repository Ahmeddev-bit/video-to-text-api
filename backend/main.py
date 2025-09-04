from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import whisper
import warnings
import os
import shutil
from fastapi.middleware.cors import CORSMiddleware
import ollama
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

import json
import ollama

def generate_metadata(transcript: str):
    prompt = f"""
    You are a YouTube metadata generator.
    Task:
    1. Translate the transcript into English.
    2. Based on the translated transcript, generate the following in valid JSON format only (no extra text or formatting):

    {{
      "title": "A concise, engaging YouTube video title (maximum 10 words)",
      "description": "A short, natural description of the video content, written in English it depend on transcript lenght",
      "hashtags": ["#keyword1", "#keyword2", "#keyword3", "#keyword4", "#keyword5", "#keyword6", "#keyword7", "#keyword8", "#keyword9", "#keyword10"]
    }}

    Transcript:
    {transcript}
    """

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract model output
    content = response["message"]["content"].strip()
    print("Raw Ollama response:", content)

    # Remove possible markdown code fences
    if content.startswith("```"):
        parts = content.split("```")
        if len(parts) >= 2:
            content = parts[1]
        content = content.replace("json", "", 1).strip()

    # Parse JSON safely
    try:
        metadata = json.loads(content)
    except json.JSONDecodeError as e:
        print("JSON parse error:", e)
        metadata = {
            "title": "",
            "description": "",
            "hashtags": []
        }

    return metadata

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

# Ensure ffmpeg is in PATH
os.environ["PATH"] += os.pathsep + r"C:\\ffmpeg\\bin"

model = whisper.load_model("small")
print("Whisper model loaded")


@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("Generating transcription...")
    result = model.transcribe(temp_file)
    transcript = result["text"]

    os.remove(temp_file)

    # Generate metadata locally with Ollama
    metadata = generate_metadata(transcript)

    return JSONResponse({
        "transcript": transcript,
        "title": metadata.get("title", ""),
        "description": metadata.get("description", ""),
        "hashtags": metadata.get("hashtags", [])
    })

