import Rally_time_speed_chart
import Digit_count_function
ans = []
start_time = input("Enter start time - ")
dist_speed_chart = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
dist_speed_chart2 = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
final = dist_speed_chart
num = Rally_time_speed_chart.time(dist_speed_chart)
print(num)


for x in range(len(num)):
    min = num[x][3]
    sec = num[x][4]
    if Digit_count_function.getDigitCountand0(num[x][3]) < 2:
         num[x][3] = "0" + str(num[x][3])
    if Digit_count_function.getDigitCountand0(num[x][4]) < 2:
        num[x][4] = "0" + str(num[x][4])

    if int(sec) >= 60:
        sec = 00
        min += 1
    if int(min) >= 60:
        start_time += 1
        min = 00
    if int(start_time) >= 24:
        start_time = "00"

    print(start_time)
    complete = str(start_time) + str(num[x][3]) + str(num[x][4])
    print(complete)
    dist_speed_chart2[x].append(complete)

print(dist_speed_chart2)



