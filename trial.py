dist_speed_chart2 = []
start_time = input("Enter start time - ")
hour = 0
min = 0
sec = 0
dist_speed_chart2 = list_nested
my_time = Rally_time_speed_chart.time(list_nested)
print(my_time)
testing = my_time
for x in my_time:
    testing.append(x)
if Digit_count_function.getDigitCountand0(start_time) == 4:
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

    if Digit_count_function.getDigitCountand0(min) < 2:
        min = "0" + str(min)
    if Digit_count_function.getDigitCountand0(sec) < 2:
        sec = "0" + str(sec)
    if int(sec) >= 60:
        sec = sec - 60
        min += 1
    if int(min) >= 60:
        start_time = int(start_time)
        start_time += 1
        min = min - 60
    # while int(hour) < 24:
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

