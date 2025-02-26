def word_count(text):
    count = len(text.split())
    return count

def letter_count(text):
    letter_dict = {}
    letters = list(text)
    for letter in letters:
        letter_dict[letter.lower()] = letter_dict.setdefault(letter.lower(),0) + 1
    return letter_dict
