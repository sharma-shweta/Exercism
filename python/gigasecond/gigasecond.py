from datetime import datetime, timedelta

ONE_GIGA_SECOND = 10**9

def add_gigasecond(date_time):
	return date_time + timedelta(seconds=ONE_GIGA_SECOND)