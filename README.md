# 🎙️ Full Stack Audio Transcription App

This project uses **FastAPI** (backend) and **React (Vite)** (frontend) to transcribe audio files into text using **OpenAI Whisper**.

---

## ⚙️ Backend Setup (FastAPI + Whisper)

1. Go to backend folder:
   ```bash
   cd backend
   ```

2. Create virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate        # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make sure **FFmpeg** is installed and added to PATH.  
   - Download: https://ffmpeg.org/download.html
   - Example (Windows): place in `C:\ffmpeg\bin` and add to PATH.

5. Start backend:
   ```bash
   uvicorn main:app --reload
   ```

   Backend runs at: `http://127.0.0.1:8000`

---

## 🎨 Frontend Setup (React + Vite)

1. Go to frontend folder:
   ```bash
   cd forntend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm run dev
   ```

   Dev server runs at: `http://127.0.0.1:5173`

4. Build production files:
   ```bash
   npm run build
   ```

   This creates `dist/` folder.

---

## 🌐 Running Full Project Together

1. Build React app:
   ```bash
   cd forntend
   npm run build
   ```

2. Start FastAPI backend (serves React app and API):
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

3. Open in browser:
   ```
   http://127.0.0.1:8000
   ```

   - React frontend loads here  
   - API endpoint available at: `http://127.0.0.1:8000/api/transcribe`

---

## 📤 Example API Request

Send an audio file with cURL:

```bash
curl -X POST "http://127.0.0.1:8000/api/transcribe"   -F "file=@sample.wav"
```

Response:
```json
{
  "transcript": "Hello world, this is a transcription example."
}
```
