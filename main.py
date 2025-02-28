from stats import word_count, letter_count

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    count = word_count(text)
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------""")
    pairs = sorted(letter_count(text).items())
    for pair in pairs:
        if pair[0].isalpha() == True:
            print(f"{pair[0]}: {pair[1]}")
    print("============= END ===============")
main()
