from stats import get_words, get_word_count, get_letter_count, display_letter_count
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    print(f"Analyzing book found at {file_path}...")
    words = get_words(text)
    word_count = get_word_count(words)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_count = get_letter_count(text)
    letter_count_list = display_letter_count(letter_count)
    for item in letter_count_list:
        print(f"{item['letter']}: {item['num']}")
    print("============= END ===============")
main()