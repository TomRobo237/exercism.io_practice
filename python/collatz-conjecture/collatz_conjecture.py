def steps(number, counter=0):
    if number <= 0:
        raise ValueError('Gave 0 or negative number')
    if number == 1:
        return counter
    counter += 1
    if number % 2 == 0:
        return steps(number / 2, counter)
    if number % 2 == 1:
        return steps(3 * number + 1, counter)
