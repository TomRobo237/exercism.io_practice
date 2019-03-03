def is_armstrong(number):
    return number == sum([ (x**len(str(number))) for x in [ int(x) for x in list(str(number))]])
