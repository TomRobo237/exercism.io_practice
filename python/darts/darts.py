ZONES = [1,5,10]
SCORES = [10,5,1]

def give_radius(x, y):
    return (abs(x)**2 + abs(y)**2)**(.5)

def score(x, y):
    radius = give_radius(x, y)
    if radius <= ZONES[0]:
        return SCORES[0]
    for i,j in zip(ZONES,ZONES[1::]):
        if i <= radius <= j:
            return SCORES[ZONES.index(j)]
    return 0

