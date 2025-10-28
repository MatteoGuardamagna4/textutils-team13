import textutils.core as c
def test_full_text_processing_pipeline():
       text = "Red red BLUE"
       counts = c.word_count(normalized)
       assert counts == [("red", 2), ("blue", 1)]