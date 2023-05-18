import config, whisper

def transcribe_audio(audio_file_path: str) -> dict:
    """
    Returns the text transcription of an audio file. The response is a
    dictionary with three keys:
    text -> the entire text transcription;
    segments -> the model results for an audio segment, including the text
    contained, position within the audio and other data;
    language -> the language detected
    """
    model = whisper.load_model("medium", download_root=config.WHISPER_MODELS_DIR)
    return model.transcribe(audio_file_path)

if __name__ == "__main__":
    file_path = "{file_path}"
    transcript = transcribe_audio(file_path)
    
    # print the entire transcript text
    print(transcript["text"])

    # print the transcript text line by line
    segments = transcript["segments"]
    for segment in segments:
        print(segment["text"])
