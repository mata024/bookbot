def get_num_words(book_text):
    num_words = len(book_text.split())
    return F"Found {num_words} total words"

def get_num_characters(book_text):
    character_counts = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    #original return dict(sorted(character_counts.items()))
    return character_counts


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sort_character_dict(character_dict):
    character_list = []
    for char in character_dict:
        num = character_dict[char]
        character_list.append({"char": char, "num": num})
    character_list.sort(reverse = True, key = sort_on)
    return character_list