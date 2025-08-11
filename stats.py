def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_char_counts(char_counts):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary has two keys: 'char' and 'num'.
    The list is sorted from greatest to least by 'num'.
    """
    # Convert the dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    
    # Sort the list in-place using .sort()
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    return char_list