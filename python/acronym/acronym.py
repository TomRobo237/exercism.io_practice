import re
def abbreviate(words):
    return ''.join([ x[0].upper() for x in re.split(r'_|\ |-',words) if x ])
