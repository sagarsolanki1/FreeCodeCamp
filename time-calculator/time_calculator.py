def add_time(start, duration, day = ""):
    start_split = start.split()
    t1 = list(map(int, start_split[0].split(":")))
    t2 = list(map(int, duration.split(":")))
    time_in_24 = [0,0]
    time_addition = [0,0]
    lst_of_day = ["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
    count = 0
    new_time = ""
    # converting time into 24 hour
    if start_split[1] == "AM" and t1[0] == 12:
        time_in_24[0], time_in_24[1] = 0, t1[1]
    elif start_split[1] == "AM":
        time_in_24[0], time_in_24[1] = t1[0], t1[1]
    elif start_split[1] == "PM" and t1[0] == 12:
        time_in_24[0], time_in_24[1] = t1[0], t1[1]
    else:
        time_in_24[0], time_in_24[1] = t1[0]+12, t1[1]
    # adding time
    if time_in_24[0] + t2[0] < 24 :
        if time_in_24[1] + t2[1] < 60:
            time_addition[0], time_addition[1] = time_in_24[0] + t2[0], time_in_24[1] + t2[1]
        elif time_in_24[1] + t2[1] == 60:
            time_addition[0], time_addition[1] = time_in_24[0] + t2[0] + 1, 0
        elif time_in_24[1] + t2[1] > 60:
            if time_in_24[0] + t2[0] + 1 > 24:
                time_addition[0], time_addition[1] = time_in_24[0] + t2[0] + 1,time_in_24[1] + t2[1] - 60
                count = 1
            elif time_in_24[0] + t2[0] + 1 < 24:
                time_addition[0], time_addition[1] = time_in_24[0] + t2[0] + 1,time_in_24[1] + t2[1] - 60
    elif time_in_24[0] + t2[0] > 24:
        if time_in_24[1] + t2[1] < 60:
            time_addition[0], time_addition[1] = (time_in_24[0] + t2[0])%24, time_in_24[1]+t2[1]
            count = int((time_in_24[0] + t2[0])/24)
        elif time_in_24[1] + t2[1] == 60:
            time_addition[0], time_addition[1] = (time_in_24[0] + t2[0])%24 + 1, 0
            count = int((time_in_24[0] + t2[0] + 1)/24)
        elif time_in_24[1] + t2[1] > 60:
            if (time_in_24[0] + t2[0] + 1)%24 == 0:
                time_addition[0], time_addition[1] = 0, time_in_24[1] + t2[1] - 60
            else:
                time_addition[0], time_addition[1] = (time_in_24[0] + t2[0])%24 + 1, time_in_24[1] + t2[1] - 60
            count = int((time_in_24[0] + t2[0] + 1)/24)
    # converting time in 24hrs to 12 hrs
    if time_addition[0] < 12:
        if time_addition[0] == 0 :
            new_time = "12" + ":" + str(f"{time_addition[1]:02}") + " AM"
        else :
            new_time = f"{time_addition[0]}" + ":" + str(f"{time_addition[1]:02}") + " AM"
    else :
        if time_addition[0] == 12 :
            new_time = "12" + ":" + str(f"{time_addition[1]:02}") + " PM"
        else :
            new_time = f"{time_addition[0] - 12}" + ":" + str(f"{time_addition[1]:02}") + " PM"
    if count == 0:
        if day != "":
            new_time += ", " + day.capitalize()
        else:
            pass
    elif count == 1:
        if day != "":
            index = lst_of_day.index(day.lower())
            if index + 2 > 6 :
                new_time += ", " + lst_of_day[(index + 1)%7].capitalize() + " (next day)"
            else:
                new_time += ", " + lst_of_day[index + 2].capitalize() + " (next day)"
        else:
            new_time += " (next day)"
    elif count > 1 :
        if day != "":
            index = lst_of_day.index(day.lower())
            if index + count > 7:
                new_time += ", " + lst_of_day[index - count%7 - 2].capitalize() + f" ({count} days later)"
            else :
                new_time += ", " + lst_of_day[index + 2].capitalize() + f" ({count} days later)"
        else:
            new_time += f" ({count} days later)"
    return new_time