import React, { useState } from "react";
import "./audio.css";

const Audio = () => {
  const [file, setFile] = useState(null);
  const [data, setdata] = useState("");
  const [error, setError] = useState("");
  const [load, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      setError("⚠️ Please upload file!!");
      setTimeout(() => setError(""), 2000);
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const res = await fetch("http://localhost:8000/transcribe", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error(`HTTP error! Status: ${res.status} ${res.statusText}`);
      }

      const data = await res.json();
      setdata(data);
      console.log(data);
      setError("");
    } catch (err) {
      setError(err.message);
      setTimeout(() => setError(""), 2000);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h1>Genrate from video</h1>
        <p>
          Upload an video file and get instant
          transcription,title,Description,Hashtages for youtube
        </p>
      </header>

      <div className="upload-section">
        <input
          type="file"
          accept="video/*"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button onClick={handleUpload} disabled={load}>
          🚀 Transcribe
        </button>

        {load && (
          // Loader animation
          <div className="loader">
            <div className="loading-text">
              Loading<span className="dot">.</span>
              <span className="dot">.</span>
              <span className="dot">.</span>
            </div>
            <div className="loading-bar-background">
              <div className="loading-bar">
                <div className="white-bars-container">
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                  <div className="white-bar"></div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {error && <div className="error">{error}</div>}
      {data && (
        <div className="transcript-card">
          <div className="transcript-header">
            <h2>📝 Transcript</h2>
            {copied && <span className="copy-success">✅ Text copied!</span>}
            <button
              className="copy-btn"
              onClick={() => {
                navigator.clipboard.writeText(data.transcript);
                setCopied(true);
                setTimeout(() => setCopied(false), 2000);
              }}
            >
              📋 Copy
            </button>
          </div>
          <p>{data.transcript}</p>
          <h2>📌 Title:</h2>
          <p>{data.title}</p>
          <h2>📝 Description:</h2>
          <p>{data.description}</p>
          <h2>🏷️ Hashtags:</h2>
          <p>{data.hashtags}</p>
        </div>
      )}
    </div>
  );
};

export default Audio;
