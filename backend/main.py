from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import whisper
import warnings
import os
import shutil

app = FastAPI()

react_dist_path = os.path.join(os.path.dirname(__file__), "../forntend/dist")

app.mount("/", StaticFiles(directory=react_dist_path, html=True), name="frontend")

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

# Ensure ffmpeg is in PATH
os.environ["PATH"] += os.pathsep + r"C:\\ffmpeg\\bin"

model = whisper.load_model("small")
print("Whisper model loaded")

@app.post("/api/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("Generating transcription...")
    result = model.transcribe(temp_file)

    os.remove(temp_file)
    return JSONResponse({"transcript": result["text"]})
