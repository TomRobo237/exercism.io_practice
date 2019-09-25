def convert_to_ints(list_of_numbers):
    retlist = []
    for i in list_of_numbers:
        try:
            retlist.append(int(i))
        except ValueError:
            return False
    return retlist

def verify(isbn):
    isbn = list(isbn.replace('-',''))
    if len(isbn) != 10:
        return False
    if isbn[-1] == 'X':
        isbn[-1] = 10
    isbn = convert_to_ints(isbn)
    if isbn == False:
        return False
    total = 0
    for i in range(0,10):
        total += isbn[i] * (10 - i)
    if total % 11 == 0:
        return True
    else:
        return False
