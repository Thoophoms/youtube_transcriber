import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')

# Make temporary folder to temporary store the audio file
TEMP_DIR = "temp"
# Create temp folder if it doesn't exist
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

st.title("🎥 YouTube Transcriber")
st.write("Convert YouTube videos to text transcripts!")

# initialize session.state for storing links
if "links" not in st.session_state:
    st.session_state.links = []
# initialize session.state for storing transcripts
if "transcripts" not in st.session_state:
    st.session_state.transcripts = []


# input box
link = st.text_input("Enter YouTube link:", key="link_input")

# Button side by side
col1, col2 = st.columns(2)

with col1:
    if st.button("Add to the Download List"):
        # Only add if there's something in the input box
        if link: 
            st.session_state.links.append(link)
            st.success(f"Added link! Total: {len(st.session_state.links)}")

with col2:
    if st.button("Download"):
        if st.session_state.links:

            import yt_dlp
            import assemblyai as aai
            import time

            # Configure AssemblyAI
            aai.settings.api_key = ASSEMBLYAI_API_KEY

            st.write("**Processing videos...**")

            # Configure yt-dlp options
            yt_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{TEMP_DIR}/%(title)s.%(ext)s',
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
                 'nocheckcertificate': True,
            }

            # Clear/Store completed transcripts
            st.session_state.transcripts = []

            # Download each link
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                for i, link in enumerate(st.session_state.links, 1):
                    st.write(f"### 🎥 Video {i}/{len(st.session_state.links)}")

                    try:
                        # 1: Download audio from YouTube
                        st.write(f"⬇️ Downloading audio...")
                        info = ydl.extract_info(link, download=True)
                        audio_filename = ydl.prepare_filename(info)
                        st.success(f"✅ Downloaded!")

                        # 2: Upload to AssemblyAI
                        st.write(f"☁️ Uploading to AssemblyAI...")
                        transcriber = aai.Transcriber()
                        config = aai.TranscriptionConfig(
                            speech_models=['universal-2'],
                            language_detection=True
                            )
                        transcript = transcriber.transcribe(audio_filename, config=config)
         

                        #3: Wait for transcription (pooing happens automatically!)
                        st.write(f"🤖 Transcribing... (this may take a minute)")

                        # 4: Check if successul
                        if transcript.status == aai.TranscriptStatus.error:
                            st.error(f"❌ Transcription failed: {transcript.error}")
                        else:
                            st.success(f"✅ Transcription complete!")

                        # Save Transcript info
                        st.session_state.transcripts.append({
                            'filename': f"transcript_{i}.txt",
                            'text': transcript.text,
                            'video_title': info.get('title', f'video {i}')
                        })

                    except Exception as e:
                        st.error(f"❌ Failed to download video {i}: {str(e)}")
            
            # Clear links the list
            st.session_state.links = []         
        else:
            st.warning("No links added yet!")


    # Show results
    if st.session_state.transcripts:

        st.write("---")
        st.write(f"## 🎉 Completed {len(st.session_state.transcripts)} transcript(s)!")

        for i, t in enumerate(st.session_state.transcripts, 1):


            st.write(f"### 📄 {t['video_title']}")

            st.download_button(
                label = f"📥 Download {t['filename']}",
                data=t['text'],
                file_name=t['filename'],
                mime="text/plain",
                key=f"download_{i}",  # Unique key for each button

            )        
            # Show proview of first 200 characters
            with st.expander("Preview transcript"):
                st.write(t['text'][:200] + "..." if len(t['text']) > 200 else t['text'])


# Show current list
if st.session_state.links:
    st.write("---")
    st.write("**Current links:**")
    for i, l in enumerate(st.session_state.links, 1):
        st.write(f"{i}. {l}")

