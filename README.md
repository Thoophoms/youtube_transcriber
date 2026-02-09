# 🎥 Audio/Video Transcriber

AI-powered web application that converts audio and video files into text transcripts using speech recognition.

## 🌟 Features

- Upload audio/video files (MP3, WAV, M4A, MP4, WEBM, OGG)
- Automatic transcription using AssemblyAI API
- Multi-language support with automatic language detection
- Clean, intuitive web interface
- Download transcripts as .txt files
- Preview transcripts before downloading

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Transcription:** AssemblyAI API (Universal-2 model)
- **Language:** Python 3.12
- **Deployment:** Streamlit Cloud

## 🚀 Live Demo

**[Try it now!](https://aiyoutubetranscriber.streamlit.app)**

Upload your audio or video file and get an AI-generated transcript in seconds!

## 💻 Running Locally

1. Clone the repository:
```bash
git clone https://github.com/Thoophoms/youtube_transcriber.git
cd youtube_transcriber
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your AssemblyAI API key:
```
ASSEMBLYAI_API_KEY=your_api_key_here
```

5. Run the app:
```bash
streamlit run app.py
```

## 🏗️ Development Journey

Initially built with YouTube download functionality using yt-dlp. Pivoted to direct file upload for improved cloud deployment reliability and broader use cases (works with any audio/video source, not just YouTube).

## 📝 Future Enhancements

- Parallel transcription processing for multiple files
- Export transcripts in multiple formats (PDF, DOCX, SRT subtitles)
- Speaker diarization (identify different speakers)
- Timestamp generation
- Batch processing with progress tracking

## 👤 Author

**Trisha Supannopaj**
- 🌐 Portfolio: [thoophoms.com](https://www.thoophoms.com/)
- 💼 LinkedIn: [trisha-supannopaj](https://www.linkedin.com/in/trisha-supannopaj/)
- 🐙 GitHub: [@Thoophoms](https://github.com/Thoophoms)

---

*Built as part of my AI Engineering portfolio • Showcasing API integration, file handling, and deployment skills*
```

---
