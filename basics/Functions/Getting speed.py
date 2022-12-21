def speed(time, distance):
    if type(time) != tuple:
        print("Please give time in tuple")
    else:
        # Getting hours
        sec = time[-1] / 60
        min = time[-2] + sec
        min = min / 60
        hour = time[0] + min


speed((1, 59, 60), 0)

