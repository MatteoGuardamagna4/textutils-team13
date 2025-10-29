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