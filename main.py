import sys
from stats import get_num_words, get_num_characters, sort_on, sort_character_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def report_title(filepath):
    title = f"""============ BOOKBOT ============
Analyzing book found at {filepath}"""
    return title

def report_word_count_section(filepath):
    word_count_section = f"""----------- Word Count ----------
{get_num_words(get_book_text(filepath))}"""
    return word_count_section

def report_character_count_section(filepath):
    all_characters = sort_character_dict(get_num_characters(get_book_text(filepath)))
    character_count_section = f"""--------- Character Count -------"""
    for char in all_characters:
        if char["char"].isalpha():
            num = char["num"]
            character_count_section = f"""{character_count_section}
{char["char"]}: {num}"""
    character_count_section = f"""{character_count_section}
============= END ==============="""
    return character_count_section

def print_report(filepath):
    print(report_title(filepath))
    print(report_word_count_section(filepath))
    print(report_character_count_section(filepath))


def main():
    #path = "books/frankenstein.txt"
    #print(get_book_text(path))
    #print(get_num_words(get_book_text(path)))
    #print(get_num_characters(get_book_text(path)))
    #print(sort_character_dict(get_num_characters(get_book_text(path))))
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_report(sys.argv[1])

main()