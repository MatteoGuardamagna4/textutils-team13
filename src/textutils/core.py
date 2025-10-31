from unicodedata import normalize
import string
import re

def count_sentences(text: str) -> int:
    """
    Counts the number of sentences in the given text.

    A sentence is defined as a sequence of characters ending with one of
    the following punctuation marks: '.', '?', or '!'.

    - Ignores trailing whitespace or punctuation-only fragments.
    - Returns 0 if text is empty or has no sentence-ending punctuation.
    Examples:
        "Hello world. How are you? Bye!" -> 3
        "Test.  " -> 1
        "" -> 0
        "A! B? C." -> 3
    """
    if not isinstance(text, str) or not text.strip():
        return 0

    # Use regex to split text by ., ?, or ! followed by optional spaces
    sentences = re.split(r'[.!?]+\s*', text.strip())

    # Filter out any empty strings that may result from split
    sentences = [s for s in sentences if s]

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

def count_vowels(text: str) -> int:
    """
    Return the total count of vowels (case-insensitive) in the input string.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

result1 = count_vowels("Hello World")
print(result1)
    
