import textutils.core as c

def test_count_vowels_basic_pipeline():
    text = "Hello World"
    assert c.count_vowels(text) == 3
    