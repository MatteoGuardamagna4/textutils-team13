from textutils.core import count_vowels
import textutils.core as c
def test_count_vowels_basic():
    """Test that count_vowels returns the correct number of vowels for a basic string."""
    text = "Hello World"
    assert c.count_vowels(text) == 3
    assert c.count_vowels(text) == 3
    