def word_count(text: str) -> dict[str, int]:
    """Return a case-insensitive word frequency dict.
    Example: "Red red BLUE" -> {"red": 2, "blue": 1}
    """
    counts = {}
    words = text.lower().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the top n (word, count) pairs sorted by:
    1) highest count desc, 2) word asc for ties.
    Example: {"a":2,"b":2,"c":1}, n=2 -> [("a",2),("b",2)]
    """
    # Sort by count descending (negative for desc), then word ascending
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

def normalize_whitespace(text: str) -> str:
    """Collapse any whitespace runs (spaces, tabs, newlines) to single spaces
    and trim leading/trailing whitespace.
    Example: "  a   b \\n  c  " -> "a b c"
    """
    return ' '.join(text.split())