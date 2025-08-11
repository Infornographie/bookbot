def count_words(content):
    words = content.split()
    return len(words)

def count_characters(content):
    lowercase = content.lower() # Convert content to lowercase to prevent duplicate counts
    char_dict0 = {}
    for char in lowercase:
        if char.isalpha():
            char_dict0[char] = char_dict0.get(char, 0) + 1 # Increment count for each character
    char_dict = [{"char": k, "num": v} for k, v in char_dict0.items()] # Convert to list of dicts
    return char_dict

def sort_on(item):
    return item["num"]  # Sort on the 'num' key

def sort_alpha(char_dict):
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict
    