def factor(x):
    for i in range(1, x):
        if x % i == 0:
            yield i


def classify(number):
    if number <= 0:
        raise ValueError('Needs to be positive integer!')
    total = sum([x for x in factor(number)])
    if total == number:
        return 'perfect'
    if total > number:
        return 'abundant'
    if total < number:
        return 'deficient'
