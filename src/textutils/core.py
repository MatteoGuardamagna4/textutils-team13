import re
from unicodedata import normalize

def slugify(text):
    # Lowercase the text and remove apostrophes from contractions
    text = re.sub(r"(\w)['’](\w)", r"\1\2", text.lower())
    # Replace all non-word characters and underscores with hyphens
    text = re.sub(r'[\W_]+', '-', text).strip('-')
    # Optionally normalize unicode (remove accents, etc.)
    text = normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    # Remove any leftover non-alphanumeric characters
    text = re.sub(r'[^a-z0-9-]', '', text)
    # Collapse multiple hyphens
    text = re.sub(r'-+', '-', text)
    return text
