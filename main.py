import sys
from stats import get_num_words, get_chars_dict, sort_char_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(chars_dict,num_words, text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(char_counts, num_words, text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    sorted_chars = sort_char_counts(char_counts)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()