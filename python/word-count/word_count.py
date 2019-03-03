import re
from collections import defaultdict

WHITESPACE_REGEX = r' |_|\t|\n|,'
STRIP_PATTERN = '.?!@$%^&,"\':'

def word_count(phrase):
    words = [ x.strip(STRIP_PATTERN).lower() for x in re.split(WHITESPACE_REGEX, phrase)]
    count = defaultdict(int)
    for i in words:
        if i:
            count[i] +=1
    return dict(count)
