def is_isogram(string):
    for letter in string.lower():
        if letter not in [' ', '-'] and string.lower().count(letter) > 1:
            return False
    return True
