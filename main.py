import sys
from stats import word_count
from stats import character_count
from stats import sort_dict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

if len(sys.argv) != 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

def main():
    book_contents = get_book_text(sys.argv[1])
    words = word_count(book_contents)
    character = character_count(book_contents)
    sorted = sort_dict(character)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    
    for sort in sorted:
        if sort["char"].isalpha():
            print(f"{sort['char']}: {sort['num']}")
    
    print("============= END ===============")
        
    
main()