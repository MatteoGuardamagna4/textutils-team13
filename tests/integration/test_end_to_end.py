import textutils.core as c
def test_full_text_processing_pipeline():
       text = "Red red BLUE"
       assert c.word_count(text) == {"red": 2, "blue": 1}