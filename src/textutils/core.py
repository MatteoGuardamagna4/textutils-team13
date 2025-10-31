import string
import re
from unicodedata import normalize
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

def word_count(text: str) -> dict[str, int]:
    """Return a case-insensitive word frequency dict.
    Example: "Red red BLUE" -> {"red": 2, "blue": 1}
    """
    counts = {}
    words = text.lower().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def slugify(text: str) -> str:
    """
    Convierte `text` en un slug seguro:
    - Convierte a minúsculas.
    - Normaliza caracteres unicode (elimina acentos).
    - Elimina caracteres que no son letras o números.
    - Sustituye espacios y separadores por guiones.
    - Quita guiones duplicados, al inicio y final.
    - Devuelve una cadena vacía si no hay texto útil.
    """
    if not isinstance(text, str) or not text.strip():
        return ''
    
    # Convertir a minúsculas y normalizar unicode
    t = text.lower()
    t = normalize('NFKD', t).encode('ascii', 'ignore').decode('ascii')
    
    # Reemplazar todo lo que no sea letra, número o espacio por espacio
    t = re.sub(r'[^a-z0-9\s-]', '', t)
    
    # Reemplazar espacios y guiones múltiples por un solo guion
    t = re.sub(r'[\s-]+', '-', t)
    
    # Quitar guiones al inicio y final
    t = t.strip('-')
    
    return t
