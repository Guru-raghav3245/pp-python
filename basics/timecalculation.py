def getDigitCountand0(num):
    digit_count = 0
    while True:
        num = int(num) / 10
        if num <= 0:
            break
        else:
            digit_count += 1
    return digit_count

def time(list):
    ans = []
    for x in range(len(list)):
        y = 0
        distance = list[x][y + 1] - list[x][y]
        speed = list[x][y + 2]

        mins = (distance / speed) * 60
        secs = (mins - int(mins)) * 60
        ans.append(int(mins))
        ans.append(int(secs))

    return ans


def time_format(list_nested, start_time):
    dist_speed_chart2 = []
    hour = 0
    min = 0
    sec = 0
    dist_speed_chart2 = list_nested
    my_time = time(list_nested)
    print(my_time)
    if getDigitCountand0(start_time) == 4:
        start_time = str(start_time)
        min = str(min)
        sec = str(sec)
        min += str(start_time[2:4])
        hour = str(start_time[0:2])
    else:
        hour = start_time
    for x in range(len(my_time)):
        min = int(min)
        sec = int(sec)
        min += int(my_time[x][3])
        sec += int(my_time[x][4])

        if getDigitCountand0(min) < 2:
            min = "0" + str(min)
        if getDigitCountand0(sec) < 2:
            sec = "0" + str(sec)
        if int(sec) >= 60:
            sec = int(sec) - 60
            min += 1
        if int(min) >= 60:
            start_time = int(start_time)
            start_time += 1
            min = min - 60
    #while int(hour) < 24:
        if int(hour) >= 24:
            hour = int(hour) - 24
        if sec == 0:
            sec = "00"
        if hour == 0:
            hour = "00"
        if min == 0:
            min = "00"
        complete = str(hour) + str(min) + str(sec)
        print(complete)
        dist_speed_chart2[x].append(complete)
    return dist_speed_chart2

def speed(time, distance):
    if type(time) != tuple:
        print("Please give time in tuple")
    else:
        # Getting hours
        sec = time[-1] / 60
        min = time[-2] + sec
        min = min / 60
        hour = time[0] + min
        speed = distance / hour
        print(speed, "KMPH")

def onlytime(distance, speed):
    mins = (distance / speed) * 60
    print(mins)
    secs = (mins - int(mins)) * 60
    print(int(mins), "mins", int(secs), "secs")