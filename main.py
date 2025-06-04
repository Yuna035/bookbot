import sys
from stats import (
    get_word_count, 
    get_char_counts,
    list_letters 
)
     
    
def print_report(book_path, num_words, listed_letters):   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch in listed_letters:
        print(f'{ch["char"]}: {ch["num"]}')

    print("============= END ===============")


def main():
        err = "Usage: python3 main.py <path_to_book>"
        try:                                   
            book_path = sys.argv[1]
            book_text = get_book_text(book_path)
            num_words = get_word_count(book_text)
            chars_count_dict = get_char_counts(book_text)
            listed_letters = list_letters(chars_count_dict) 
            print_report(book_path, num_words, listed_letters)
        except IndexError:
            print(err) 
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
       

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
   

main()
    
