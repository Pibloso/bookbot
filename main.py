import sys
from stats import word_count, letter_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text(sys.argv[1])
    count = word_count(text)
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------""")
    pairs = sorted(letter_count(text).items())
    for pair in pairs:
        if pair[0].isalpha() == True:
            print(f"{pair[0]}: {pair[1]}")
    print("============= END ===============")
main()
