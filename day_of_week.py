def day_of_week (string):
    import math
    my_month, day, year = string.split(" ")
    months = {"March": 1,
              "April": 2,
              "May": 3,
              "June": 4,
              "July": 5,
              "August": 6,
              "September": 7,
              "October": 8,
              "November": 9,
              "December": 10,
              "January": 11,
              "February": 12}
    weeks = {"Sunday": 0,
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6}
    # Get the appropriate month as an int using a dictionary
    month = months[my_month]
    day = int(day)
    # The first two characters of the year
    century = int(year[0] + year[1])
    # The last two characters of the year
    year = int(year[2] + year[3])
    # If month > 10 (i.e january or february then substract one year)
    if month > 10:
        year = year - 1
    # Calculation
    w = (day + math.floor(2.6*month - 0.2) -2*century + year + math.floor(year/4) + math.floor(century/4))%7
    for day in weeks:
        if weeks[day] == w:
            return day