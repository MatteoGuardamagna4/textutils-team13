import textutils.core as c

def test_count_sentences_basic():
    text = "Hello world. How are you? Bye!"
    assert c.count_sentences(text) == 3

def test_count_sentences_trailing_spaces():
    text = "Test.  "
    assert c.count_sentences(text) == 1

def test_count_sentences_empty():
    text = ""
    assert c.count_sentences(text) == 0

def test_count_sentences_mixed_punctuation():
    text = "A! B? C."
    assert c.count_sentences(text) == 3