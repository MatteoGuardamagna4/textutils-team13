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

    return len(sentences)
