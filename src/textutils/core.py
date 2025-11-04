def replace_numbers(text):
    # Mapping of digits to words
    num_words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    
    # Replace each digit with its word equivalent
    result = ''.join(num_words.get(char, char) for char in text)
    return result


# Example usage
print(replace_numbers("I have 2 cats and 1 dog."))  
# Output: "I have two cats and one dog."
