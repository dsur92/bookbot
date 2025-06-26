def word_count(book):
    return len(book.split())

def character_count(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_dict(items):
    def sort_on(dictionary):
        return dictionary["num"]

    sorted_char = []
    for item in items:
        sorted_char.append({"char": item, "num": items[item]})
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char

