def word_count(text):
    count = len(text.split())
    return count

def letter_count(text):
    letter_dict = {}
    words = text.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            letter_dict[letter] += 1
    return letter_dict
