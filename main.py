import sys
from stats import get_num_words, get_num_chars, sort_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def get_book_text():
    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report():
    print("============ BOOKBOT ============")
    text = get_book_text()
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    char_count = get_num_chars(text)
    sorted_report = sort_report(char_count)
    for item in sorted_report:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    print_report()

main()
