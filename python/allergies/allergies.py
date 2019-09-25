allergens = ['cats', 'pollen', 'chocolate', 'tomatoes', 'strawberries', 'shellfish', 'peanuts', 'eggs']


class Allergies(object):
    def __init__(self, score):
        self.allergy_dict = {allergens[item]: int(binary) for item, binary in enumerate(list(f'{score % 256:08b}'))}

    def allergic_to(self, item):
        return bool(self.allergy_dict[item])

    @property
    def lst(self):
        return [x for x, y in self.allergy_dict.items() if y == 1]
