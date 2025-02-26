from stats import word_count, letter_count

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    count = word_count(text)
    print(f"{count} words found in the document")
    print(letter_count(text))

main()
