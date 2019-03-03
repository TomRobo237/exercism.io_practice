from datetime import timedelta
gigasec = timedelta( seconds = 10 ** 9 )

def add_gigasecond( birth_date ):
    return birth_date + gigasec 
