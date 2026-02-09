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

st.title("🎥 Audio/Video Transcriber")
st.write("Convert audio/video files to text transcripts!")


# initialize session.state for storing transcripts
if "transcripts" not in st.session_state:
    st.session_state.transcripts = []


# # input box
# link = st.text_input("Enter YouTube link:", key="link_input")

# File Upload inbox
st.write("**Upload audio/video files:**")
uploaded_files = st.file_uploader(
    label="Choose audio or video files",
    type=['mp3', 'wav', 'm4a', 'mp4', 'webm', 'ogg'],
    accept_multiple_files=True,
    help="Upload audio or video files to transcribe"
)

# Button side by side
# col1, col2 = st.columns(2)

# with col2:
if st.button("Transcribe"):
    if uploaded_files:
        import assemblyai as aai
        import time

        # Configure AssemblyAI
        aai.settings.api_key = ASSEMBLYAI_API_KEY

        st.write("**Processing files...**")

        # Clear/Store completed transcripts
        st.session_state.transcripts = []

        # Process each uploaded file
        for i, uploaded_file in enumerate(uploaded_files, 1):
            st.write(f"### 🎵 File {i}/{len(uploaded_files)}: {uploaded_file.name}")

            try:
                # Save uploaded file to temp folder
                temp_filename = f"{TEMP_DIR}/uploaded_{i}_{uploaded_file.name}"

                # Save to disk
                with open(temp_filename, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                st.success(f"✅ File saved!")

                # Upload to AssemblyAI and transcribe
                st.write(f"☁️ Uploading to AssemblyAI...")
                transcriber = aai.Transcriber()
                config = aai.TranscriptionConfig(
                    speech_models=['universal-2'],
                    language_detection=True
                )

                # Wait for transcription (pooing happens automatically!)
                st.write(f"🤖 Transcribing... (this may take a minute)")
                
                # Now file name is the path that we can pass it to AssemblyAI
                transcript = transcriber.transcribe(temp_filename, config=config)

                # 4: Check if successul
                if transcript.status == aai.TranscriptStatus.error:
                    st.error(f"❌ Transcription failed: {transcript.error}")
                else:
                    st.success(f"✅ Transcription complete!")

                # Save Transcript info
                st.session_state.transcripts.append({
                    'filename': f"transcript_{i}_{uploaded_file.name.rsplit('.', 1)[0]}.txt",
                    'text': transcript.text,
                    'video_title': uploaded_file.name
                })

            except Exception as e:
                st.error(f"❌ Error processing file {i}: {str(e)}")
    else:
        st.warning("No files uploaded yet!")


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




