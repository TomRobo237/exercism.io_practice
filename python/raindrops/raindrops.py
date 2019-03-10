def raindrops(number):
    rain = 'Pling' * (not number % 3) + 'Plang' * (not number % 5) + 'Plong' * (not number % 7)
    if not rain:
        rain = str(number)
    return rain
