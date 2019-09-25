ordinal_numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
                   'eleventh', 'twelfth']

items = ["and a Partridge in a Pear Tree.",
         "two Turtle Doves, ",
         "three French Hens, ",
         "four Calling Birds, ",
         "five Gold Rings, ",
         "six Geese-a-Laying, ",
         "seven Swans-a-Swimming, ",
         "eight Maids-a-Milking, ",
         "nine Ladies Dancing, ",
         "ten Lords-a-Leaping, ",
         "eleven Pipers Piping, ",
         "twelve Drummers Drumming, "
         ]

verses_concat = [''.join(items[:x+1][::-1]) for x in range(0, len(items))]
verses_concat[0] = verses_concat[0][4:]

def recite(start_verse, end_verse):
    return [f"On the {ordinal_numbers[x]} day of Christmas my true love gave to me: {verses_concat[x]}"
              for x in range(start_verse - 1, end_verse)]
