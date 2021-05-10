def counter():
    import datetime
    a = datetime.datetime.now()
    b = datetime.datetime(a.year+1, 1, 1)
    c = b - a
    hours = c.seconds // 3600
    minutes = c.seconds // 60 - hours * 60
    days = int(c.days)

    if days // 10:
        if days == 10 or days == 11 or days == 12 or days == 13 or days == 14:
            day = 'дней'
        elif days % 10 == 1:
            day = 'день'
        elif days % 10 == 2 or days % 10 == 3 or days % 10 == 4:
            day = 'дня'
        elif days % 10 == 5 or days % 10 == 6 or days % 10 == 7 or days % 10 == 8 or days % 10 == 9 or days % 10 == 0:
            day = 'дней'
    else:
        if days % 10 == 1:
            day = 'день'
        elif days % 10 == 2 or days % 10 == 3 or days % 10 == 4:
            day = 'дня'
        elif days % 10 == 5 or days % 10 == 6 or days % 10 == 7 or days % 10 == 8 or days % 10 == 9 or days % 10 == 0:
            day = 'дней'

    if hours // 10:
        if hours == 10 or hours == 11 or hours == 12 or hours == 13 or hours == 14:
            hour = 'часов'
        elif hours % 10 == 1:
            hour = 'час'
        elif hours % 10 == 2 or hours % 10 == 3 or hours % 10 == 4:
            hour = 'часа'
        elif hours % 10 == 5 or hours % 10 == 6 or hours % 10 == 7 or hours % 10 == 8 or hours % 10 == 9 or hours % 10 == 0:
            hour = 'часов'
    else:
        if hours % 10 == 1:
            hour = 'час'
        elif hours % 10 == 2 or hours % 10 == 3 or hours % 10 == 4:
            hour = 'часа'
        elif hours % 10 == 5 or hours % 10 == 6 or hours % 10 == 7 or hours % 10 == 8 or hours % 10 == 9 or hours % 10 == 0:
            hour = 'часов'

    if minutes // 10:
        if minutes == 10 or minutes == 11 or minutes == 12 or minutes == 13 or minutes == 14:
            minute = 'минут'
        elif minutes % 10 == 1:
            minute = 'минута'
        elif minutes % 10 == 2 or minutes % 10 == 3 or minutes % 10 == 4:
            minute = 'минуты'
        elif minutes % 10 == 5 or minutes % 10 == 6 or minutes % 10 == 7 or minutes % 10 == 8 or minutes % 10 == 9 or minutes % 10 == 0:
            minute = 'минут'
    else:
        if minutes % 10 == 1:
            minute = 'минута'
        elif minutes % 10 == 2 or minutes % 10 == 3 or minutes % 10 == 4:
            minute = 'минуты'
        elif minutes % 10 == 5 or minutes % 10 == 6 or minutes % 10 == 7 or minutes % 10 == 8 or minutes % 10 == 9 or minutes % 10 == 0:
            minute = 'минут'
    lst = [str(c.days), str(day), str(hours), str(hour), str(minutes), str(minute)]
    answer = " ".join(lst)
    return answer
