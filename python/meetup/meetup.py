import datetime
from calendar import Calendar, day_name

positionTable = {
    '1st': 0,
    '2nd': 1,
    '3rd': 2,
    '4th': 3,
    '5th': 4,
    'last': -1,
    'teenth': 2
}

def meetup_day(year, month, day, position):
	dates = Calendar().itermonthdates(year, month)
	if position != 'teenth':
		dates = list(filter(lambda _date:_date.month==month, dates))
	dates = list(filter(lambda _date:day_name[_date.weekday()]==day, dates))
	return dates[positionTable[position]]
