# 🎥 YouTube Transcriber

AI-powered web application that converts YouTube videos into text transcripts using speech recognition.

## 🌟 Features

- Download audio from YouTube videos
- Automatic transcription using AssemblyAI
- Multi-language support with automatic language detection
- Clean, intuitive web interface
- Download transcripts as .txt files

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Audio Processing:** yt-dlp
- **AI Transcription:** AssemblyAI API
- **Language:** Python 3.12

## 🚀 Live Demo

[View Live App](https://your-app-url-here.streamlit.app) *(Coming soon)*

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

4. Create `.env` file with your API key:
```
ASSEMBLYAI_API_KEY=your_api_key_here
```

5. Run the app:
```bash
streamlit run app.py
```

## 📝 Future Enhancements

- Batch transcription with parallel processing
- Duplicate link detection
- Video duration validation
- Export as multiple formats (PDF, DOCX)

## 👤 Author

Trisha Supannopaj
- GitHub: [@Thoophoms](https://github.com/Thoophoms)
- LinkedIn: [https://www.linkedin.com/in/trisha-supannopaj/]
- Portfolio Website: [https://www.thoophoms.com/]

---

*Built as part of my AI Engineering portfolio*
*The app works locally, and this is a known YouTube API limitation*