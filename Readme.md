Video to Text & SEO Metadata Generator API

This project is a FastAPI application with a React frontend. It allows users to upload video files, transcribe them using the Whisper model, and generate SEO-friendly YouTube metadata (title, description, hashtags).

🚀 Features

Upload video files (various formats supported)

Automatic transcription to text

SEO-ready metadata generation:

Title (max 10 words)

Description (short and natural, in English)

10 Hashtags

🌟 Benefits

Save time on manual transcription

Instantly get SEO-optimized metadata for YouTube

Upload once, copy, and paste results directly into YouTube

🛠️ Technologies

Frontend: HTML, CSS, React (JavaScript)

Backend: Python (FastAPI, Whisper)

Uvicorn (ASGI server)

FFmpeg (video processing)

⚡ Installation
Prerequisites

Python 3.7+

Node.js

FFmpeg (in PATH)

Clone the repository
git clone https://github.com/yourusername/video-to-text-api.git
cd video-to-text-api

Backend setup
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
pip install fastapi uvicorn whisper
uvicorn main:app --reload

Frontend setup
cd frontend
npm install
npm run dev

📖 User Guide

Start the backend server with:

uvicorn main:app --reload

Start the frontend with:

npm run dev

Open your browser and go to the frontend URL (default: http://localhost:5173).

Upload your video file using the upload form.

Wait for processing. You will receive:

The transcript of your video

An SEO-friendly title (max 10 words)

A short description in English

10 hashtags for YouTube SEO

Copy the results and paste them directly into your YouTube video settings.
