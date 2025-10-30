import textutils.core as c

def test_count_vowels_basic_pipeline():
    text = "Hello World"
    result = c.count_vowels(text)
    print(f"The number of vowels in '{text}' is: {result}")

def test_check_for_vowels(text="Hello World"):
    result = c.count_vowels(text)
    has_vowels = result > 0
    print(f"Text: '{text}'")
    print(f"Does the text contain any vowels? {has_vowels}")