import re

rm_regex = r'[ +()-.]'
phone_regex = r'^[2-9][0-9]{2}[2-9][0-9]{6}$'


class Phone(object):
    def __init__(self, phone_number):
        self.number = re.sub(rm_regex, '', phone_number)
        if len(self.number) == 11 and self.number.startswith('1'):
            self.number = self.number[1:]
        if not re.match(phone_regex, self.number):
            raise ValueError('Phone number format is invalid!')
        self.area_code = self.number[0:3]

    def pretty(self):
        return f'({self.number[0:3]}) {self.number[3:6]}-{self.number[6:]}'
