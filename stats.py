def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for character in text :
        char_lower = character.lower()
        if char_lower in char_count:
            char_count[char_lower] = char_count[char_lower] + 1
        else :
            char_count[char_lower] = 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_count(char_count):
    sorted_list = []
    for character, value in char_count.items():
        sorted_list.append({"char": character, "num": value})
    sorted_list.sort(reverse=True, key=sort_on) 
    return sorted_list

    

