open_brak = ['(', '[', '{']
close_brak = [')', ']', '}']


def is_paired(input_string):
    stack = []
    for i in input_string:
        if i in open_brak:
            stack.append(i)  # Put open on stack
        elif i in close_brak:
            item = close_brak.index(i)  # get index to look for open paren
            if (len(stack) > 0) and open_brak[item] == stack[len(stack)-1]:
                stack.pop()  # If it matches the most recent item in stack, remove most recent item
            else:
                return False
    return len(stack) == 0
