def unique_words(text: str) -> list:
    words = text.lower().split()
    return sorted(set(words))
