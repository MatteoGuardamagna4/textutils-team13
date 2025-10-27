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
    # Convert to list of tuples
    items = list(counts.items())
    
    # Bubble sort or manual sorting
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            # Compare: first by count (descending), then by word (ascending)
            if (items[i][1] < items[j][1] or 
                (items[i][1] == items[j][1] and items[i][0] > items[j][0])):
                items[i], items[j] = items[j], items[i]
    
    return items[:n]

def normalize_whitespace(text: str) -> str:
    """Collapse any whitespace runs (spaces, tabs, newlines) to single spaces
    and trim leading/trailing whitespace.
    Example: "  a   b \\n  c  " -> "a b c"
    """
    return ' '.join(text.split())