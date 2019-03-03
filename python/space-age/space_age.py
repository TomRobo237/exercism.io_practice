
PLANET_YEARS = {'mercury': 0.2408467,
                'venus': 0.61519726,
                'earth': 1,
                'mars': 1.8808158,
                'jupiter': 11.862615,
                'saturn': 29.447498,
                'uranus': 84.016846,
                'neptune': 164.79132}

def space_age(earth_age, planet_name):
    return round(earth_age / PLANET_YEARS[planet_name],2)

class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_age = seconds / 31557600
    def __getattr__(self, name):
        def method(*args):
            if name.split('on_')[1] in PLANET_YEARS.keys():
                return space_age(self.earth_age, name.split('on_')[1])
        return method
        

