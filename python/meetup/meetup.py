import datetime
import calendar

FIRST_WEEK = list(range(1, 8))
SECOND_WEEK = [x + 7 for x in FIRST_WEEK]
THIRD_WEEK = [x + 7 for x in SECOND_WEEK]
FOURTH_WEEK = [x + 7 for x in THIRD_WEEK]
FIFTH_WEEK = [x + 7 for x in FOURTH_WEEK]
TEENTHS_DATES = list(range(13, 20))
WEEKS = [FIRST_WEEK, SECOND_WEEK, THIRD_WEEK, FOURTH_WEEK, FIFTH_WEEK, TEENTHS_DATES]
WEEK_WORDS = ['1st', '2nd', '3rd', '4th', '5th','teenth']
DAY_NAMES = [x for x in calendar.day_name]


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    day = DAY_NAMES.index(day_of_week)
    if week == 'last':
        dates = [x for x in calendar.Calendar().itermonthdays2(year, month)]
        dates.reverse()
        for x, y in dates:
            if y == day and x != 0:
                return datetime.date(year, month, x)
    else:
        week_list = WEEKS[WEEK_WORDS.index(week)]
        for x, y in calendar.Calendar().itermonthdays2(year, month):
            if y == day and x in week_list:
                return datetime.date(year, month, x)
        raise MeetupDayException("Day ain't real!")
