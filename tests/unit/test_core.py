import unittest

def replace_numbers(text):
    """
    Replaces single digits (0-9) in a string with their word representation.
    Note: It handles sequential digits as individual replacements (e.g., "12" becomes "onetwo").
    """
    digit_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    result = []
    for char in text:
        # If the character is a digit and is in our map, replace it.
        if char in digit_map:
            result.append(digit_map[char])
        else:
            # Otherwise, keep the character as is.
            result.append(char)
    return "".join(result)

class TestReplaceNumbers(unittest.TestCase):
    def test_single_digits(self):
        self.assertEqual(replace_numbers("1"), "one")
        self.assertEqual(replace_numbers("9"), "nine")

    def test_mixed_text(self):
        self.assertEqual(replace_numbers("I have 2 cats."), "I have two cats.")
        self.assertEqual(replace_numbers("Room 4B"), "Room fourB")

    def test_multiple_digits(self):
        self.assertEqual(replace_numbers("123"), "onetwothree")

    def test_no_digits(self):
        self.assertEqual(replace_numbers("Hello world!"), "Hello world!")

    def test_digits_in_sentence(self):
        self.assertEqual(replace_numbers("There are 3 dogs and 7 cats."), "There are three dogs and seven cats.")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_numbers(""), "")


# Run the tests
if _name_ == "_main_":
    unittest.main()
