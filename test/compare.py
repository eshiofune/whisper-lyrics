import re
import lyrics

def get_bigrams(sentence: str) -> list[list]:
    """
    Splits out spaces and special characters and returns a list of
    bigrams composed of the words in the sentence.
    """
    words = [
        word.lower() for word in re.split(r"[\s,']", sentence) if word != ""
    ]
    bigrams = []
    for i in range(len(words) - 1):
        bigrams.append([ words[i], words[i+1] ])
    return bigrams

def compare_bigrams(base_bigrams: str, comparing_bigrams: str):
    """
    Returns a value representing the similarity of the two bigrams.
    """
    difference = [
        pair for pair in base_bigrams if pair not in comparing_bigrams
    ]
    return 1 - len(difference) / len(base_bigrams)

if __name__ == "__main__":
    human_lyrics = lyrics.HUMAN_LYRICS.split("\n")
    api_lyrics = lyrics.WHISPER_API_LYRICS.split("\n")
    medium_model_lyrics = lyrics.WHISPER_MEDIUM_MODEL_LYRICS.split("\n")

    assert len(human_lyrics) == len(api_lyrics)
    assert len(human_lyrics) == len(medium_model_lyrics)

    api_similarity_total = 0
    model_similarity_total = 0

    for i, line in enumerate(human_lyrics):
        human_bigrams = get_bigrams(line)
        api_bigrams = get_bigrams(api_lyrics[i]) # this is why we asserted
        # that their lengths are equal
        api_similarity_total += compare_bigrams(human_bigrams, api_bigrams)

        model_bigrams = get_bigrams(medium_model_lyrics[i])
        model_similarity_total += compare_bigrams(human_bigrams, model_bigrams)

    print(f"API similarity level: {api_similarity_total / len(human_lyrics)}")
    print(f"Medium model similarity level: {model_similarity_total / len(human_lyrics)}")
