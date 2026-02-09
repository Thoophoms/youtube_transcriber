# YouTube Transcriber - TODO List

## TODO 1 - Streamlit UX & UI
- [✅] Project structure with virtual environment
- [✅] Working Streamlit interface
- [✅] Session state management to store links
- [✅] Multiple link input handling
- [✅] Basic UX flow

## TODO 2 - Make yt-dlp actually download YouTube audio
- [✅] Downloaded actual audio from YouTube
- [✅] Debugged real environment issues
- [✅] Save files in temp/ folder as .webm files
- [✅] Takes multiple YouTube links
- [✅] Shows progress to users

## TODO 3 - Add AssemblyAI transcription to turn .webm files into actual text
- [✅] Register and get API Key https://www.assemblyai.com/
- [✅] Upload audio to AssemblyAI
- [✅] Trigger transcription
- [✅] Handling async operations - Wait for the result (polling)
- [✅] Download transcript as .txt file
- [✅] Session state management to store transcripts
- [✅] Clear links when all done

## TODO 4 - Deploy MVP V1.0
- [✅] Create requirements.txt
- [✅] API Key
- [✅] Deploy on Streamlit cloud
- [✅] Push to GitHub
- [✅] Deploy frontend on Streamlit
- [❌] Check if there's any issue (yt-dlp get blocked on cloud deployments)

## TODO 4 - Ship to user upload audio file (Work perfectly on cloud)
- [✅] Change input box from link input to upload file
- [✅] Input accepts multiple file types(mp3, wav, m4a, mp4, webm, ogg)
- [✅] Bulk upload
- [✅] Clean up button names


## TODO 5 - ZIP file creation

## TODO 6 - Error handling (invalid links, duration check, Duplicate Links)

## TODO 8 - Error Handling & Polish
- [ ] Handle duplicate links (prevent same link being added twice)
- [ ] Validate YouTube link format
- [ ] Check video duration (max 30 minutes)
- [ ] Handle invalid/private/deleted videos
- [ ] Add loading spinners during processing

## Future Enhancements (Post-MVP)
- [ ] User accounts/login
- [ ] Save transcription history if subscribe
- [ ] Playlist support
- [ ] Parallel transcription processing (Approach B)
- [ ] Show progress for all videos simultaneously
- [✅] See what's already added
- [ ] Users are able to delete added link(s) if they change their minds
- [ ] Input box: Once add link to the list clear out the box make it empty
- [ ] Input box: Clear add suggestion when clicking the box


