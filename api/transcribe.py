import config, openai

def transcribe_audio(audio_file_path: str) -> str:
    """
    Returns the entire text transcription of an audio file.
    """
    with open(audio_file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file, api_key=config.API_KEY)
        return transcript["text"]

if __name__ == "__main__":
    file_path = "{file_path}"
    transcript = transcribe_audio(file_path)
    print(transcript)
