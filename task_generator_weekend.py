from datetime import timedelta, date

def weekend_generator(start, end):
    while start < end:
        if start.weekday() < 5:
            start = start + timedelta(days=1)
        else:
            yield start
            start = start + timedelta(days=1)
