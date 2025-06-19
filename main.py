from stats import *
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # print(get_num_words(book_path))
    # print(count_characters(book_path))
    print(sort_dict(book_path))


main()
