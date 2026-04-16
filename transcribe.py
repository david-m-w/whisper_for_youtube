import yt_dlp
import whisper
import os
import time as t

"""
# Configuration
YOUTUBE_URL = "https://www.youtube.com/watch?v=pXq-5L2ghhg"
AUDIO_FILENAME = "audio_to_transcribe.m4a"
OUTPUT_TEXT_FILE = "transcript.txt"
"""


YOUTUBE_URL = input("url for youtube vid: ")
AUDIO_FILENAME = input("AUDIO_FILENAME (default: audio_to_transcribe.m4a) :")
AUDIO_FILENAME = AUDIO_FILENAME if AUDIO_FILENAME != "" else "audio_to_transcribe.m4a"
OUTPUT_TEXT_FILE = input("OUTPUT_TEXT_FILE (default: transcript.txt) :")
OUTPUT_TEXT_FILE = OUTPUT_TEXT_FILE if OUTPUT_TEXT_FILE != "" else "transcript.txt"

# Model sizes: 'tiny', 'base', 'small', 'medium', 'large', 'large-v3'
# 'medium' requires ~5GB of VRAM. If you have 8GB+ VRAM, change this to 'large-v3' for the best possible accuracy.
print("Model sizes: 'tiny', 'base', 'small', 'medium', 'large', 'large-v3'")
MODEL_SIZE = input("MODEL_SIZE (default: medium) :")
MODEL_SIZE = MODEL_SIZE if MODEL_SIZE != "" else "medium"



def download_audio(url, output_filename):
    print(f"Downloading audio from {url}...")
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': output_filename,
        'quiet': False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete.")
    except Exception as e:
        print(f"Error downloading audio: {e}")
        exit(1)

def transcribe_audio(audio_path, model_size):
    print(f"Loading Whisper model '{model_size}'...")
    print("This will automatically use your NVIDIA GPU if PyTorch CUDA is installed correctly.")
    
    # Load the model (automatically moves to GPU if available)
    model = whisper.load_model(model_size)
    
    print("Starting transcription (this may take a few minutes)...")
    starttime = t.time()
    # Transcribe the audio
    result = model.transcribe(audio_path)
    endtime = t.time()
    print(f"total time elapsed for audio transcription: {endtime-starttime}")
    
    return result["text"]

if __name__ == "__main__":
    # Step 1: Download the audio if it doesn't already exist
    if not os.path.exists(AUDIO_FILENAME):
        download_audio(YOUTUBE_URL, AUDIO_FILENAME)
    else:
        print(f"Found existing audio file: {AUDIO_FILENAME}. Skipping download.")
        
    # Step 2: Transcribe the audio
    transcript = transcribe_audio(AUDIO_FILENAME, MODEL_SIZE)
    
    # Step 3: Save to a text file
    with open(OUTPUT_TEXT_FILE, "w", encoding="utf-8") as f:
        f.write(transcript.strip())
        
    print(f"\nSuccess! Transcription saved to {OUTPUT_TEXT_FILE}")