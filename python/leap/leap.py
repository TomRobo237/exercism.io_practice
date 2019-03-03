def is_leap_year( year ):
    return year % 4 == 0 and ( not year % 100 == 0 or year % 400 == 0 )

# Other / older solutions:
# from calendar import isleap as is_leap_year

# # def is_leap_year(year):
    # if year % 4 == 0: 
        # if year % 400 == 0:
            # return True
        # if year % 100 == 0:
            # return False
        # return True
    # return False

# def is_leap_year( year ):
    # if year % 100 == 0 and year %  400 == 0 or not year % 100 == 0 and year % 4 == 0:
        # return True
    # return False
