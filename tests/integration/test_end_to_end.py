import textutils.core as c
import string

def full_text_analysis_pipeline(text: str) -> dict:
    text_lower = text.lower()
    cleaned_for_avg = ''.join(ch for ch in text_lower if ch.isalpha() or ch.isspace())

    # 2. Execute Core Operations
    
    # A. Unique Words (Uses lowercased text)
    unique_words_list = c.unique_words(text_lower)
    
    # B. Word Count (Uses original text for case-specific counting as per test_full_text_processing_pipeline)
    word_counts = c.word_count(text)
    
    # C. Average Word Length (Uses pre-cleaned and lowercased text)
    avg_word_len = c.average_word_length(cleaned_for_avg)
    
    # D. Vowel Count (Uses original text)
    vowel_count = c.count_vowels(text)
    
    # E. Sentence Count (Uses original text)
    sentence_count = c.count_sentences(text)
    
    # F. Slugify (Uses original text)
    text_slug = c.slugify(text)

    # 3. Return Consolidated Results
    return {
        "text": text,
        "unique_words_list": unique_words_list,
        "word_counts": word_counts,
        "average_word_length": avg_word_len,
        "vowel_count": vowel_count,
        "sentence_count": sentence_count,
        "slugified_text": text_slug
    }