import Rally_time_speed_chart
import Digit_count_function
ans = []
start_time = input("Enter start time - ")
dist_speed_chart = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
dist_speed_chart2 = []
#dist_speed_chart3 = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60], [12, 20, 20], [20, 30, 50]]
dist_speed_chart3 =  [[0, 3, 23], [3, 9, 50], [9, 22, 20], [22, 46, 34], [46, 55, 24], [55, 104, 40], [104, 162, 40], [162, 193, 50], [193, 197, 20 ]]
hour = 0
min = 0
sec = 0
dist_speed_chart2 = dist_speed_chart3
num = Rally_time_speed_chart.time(dist_speed_chart3)
print(num)
if Digit_count_function.getDigitCountand0(start_time) == 4:
    start_time = str(start_time)
    min = str(min)
    sec = str(sec)
    min += str(start_time[2:4])
    hour = str(start_time[0:2])
else:
    hour = start_time
for x in range(len(num)):
    min = int(min)
    sec = int(sec)
    min += int(num[x][3])
    sec += int(num[x][4])

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
    #while int(hour) < 24:
    if int(hour) >= 24:
        hour = int(hour) - 24
    if sec == 0:
        sec = "00"
    if hour == 0:
        hour = "00"
    if min == 0:
        min = "00"

    print(min, sec)
    complete = str(hour) + str(min) + str(sec)
    print(complete)
    dist_speed_chart2[x].append(complete)

print( [[0, 3, 23, 7, 49], [3, 9, 50, 7, 11], [9, 22, 20, 39, 0], [22, 46, 34, 42, 21], [46, 55, 24, 22, 30], [55, 104, 40, 73, 30], [104, 162, 40, 87, 0], [162, 193, 50, 37, 12], [193, 197, 20, 12, 0]])
print(dist_speed_chart2)



