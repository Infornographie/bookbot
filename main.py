import sys
from stats import count_words, count_characters, sort_alpha

def get_book_text(bookpath):
    with open(bookpath) as f:
        content = f.read()
        return content    

def main():
    if len(sys.argv) > 1:
        bookpath = sys.argv[1] # Get book path from command line argument
    else:
        (print("Usage: python3 main.py <path_to_book>"))
        sys.exit(1)
    
    text = get_book_text(bookpath)
    word_count = count_words(text)
    dict = sort_alpha(count_characters(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in dict:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main ()