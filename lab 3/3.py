def is_magic(day, month, year):
    if day * month == year % 100:
        return True
    return False