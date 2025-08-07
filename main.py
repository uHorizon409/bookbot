from stats import get_num_words
from stats import get_char_count
from stats import sort_count
import sys

def main():

    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_list = sort_count(char_count)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
            print(f"Found {num_words} total words")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()


    
    
