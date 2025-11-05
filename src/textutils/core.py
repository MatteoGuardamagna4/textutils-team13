from unicodedata import normalize
import string
import re


def count_sentences(text: str) -> int:
    """
    Return the number of sentences in the given text.
    Sentences are split using '.', '!', or '?' as delimiters.
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


def unique_words(text: str) -> list[str]:
    """
    Return a sorted list of unique words in lowercase.
    """
    words = text.lower().split()
    return sorted(set(words))


def word_count(text: str) -> dict[str, int]:
    """
    Return a case-insensitive word frequency dictionary.
    Example:
        "Red red BLUE" -> {"red": 2, "blue": 1}
    """
    counts = {}
    words = text.lower().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def slugify(text: str) -> str:
    """
    Convert text into a URL-safe slug:
    - Convert to lowercase.
    - Normalize Unicode characters (remove accents).
    - Remove non-alphanumeric characters.
    - Replace spaces and hyphens with a single hyphen.
    - Trim hyphens at the start and end.
    - Return an empty string if the text is invalid or empty.
    """
    if not isinstance(text, str) or not text.strip():
        return ''

    # Convert to lowercase and normalize Unicode
    t = text.lower()
    t = normalize('NFKD', t).encode('ascii', 'ignore').decode('ascii')

    # Remove non-alphanumeric characters
    t = re.sub(r'[^a-z0-9\s-]', '', t)

    # Replace multiple spaces or hyphens with a single hyphen
    t = re.sub(r'[\s-]+', '-', t)

    # Trim leading/trailing hyphens
    t = t.strip('-')

    return t


def count_vowels(text: str) -> int:
    """
    Return the total number of vowels (case-insensitive) in the input text.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def average_word_length(text: str) -> float:
    """
    Return the average number of characters per word in the given text.
    - Splits by spaces.
    - Removes punctuation from the start and end of each word.
    - Ignores empty tokens.
    - Returns 0.0 if no words are found.
    """
    if not isinstance(text, str) or not text.strip():
        return 0.0

    words = []
    for token in text.split():
        word = token.strip(string.punctuation)
        if word:
            words.append(word)

    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def replace_numbers(text):
    # Mapping of digits to words
    num_words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    
    # Replace each digit with its word equivalent
    result = ''.join(num_words.get(char, char) for char in text)
    return result

