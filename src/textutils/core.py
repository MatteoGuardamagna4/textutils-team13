import string

def average_word_length(text: str) -> float:
    """
    Promedio de caracteres por palabra en `text`.
    - Divide por espacios.
    - Quita puntuación al inicio/fin de cada token.
    - Ignora tokens vacíos.
    - Devuelve 0.0 si no hay palabras.
    """
    if not isinstance(text, str) or not text.strip():
        return 0.0

    words = []
    for tok in text.split():
        w = tok.strip(string.punctuation)
        if w:
            words.append(w)

    if not words:
        return 0.0

    total = sum(len(w) for w in words)
    return total / len(words)

def unique_words(text: str) -> list:
    words = text.lower().split()
    return sorted(set(words))
