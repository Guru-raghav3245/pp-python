import Rally_mins_and_seconds
ans = []
start_time = input("Enter start time - ")
dist_speed_chart = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
dist_speed_chart2 = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
final = dist_speed_chart
num = Rally_mins_and_seconds.time(dist_speed_chart)
print(num)
complete = ""
mins = 0
secs = 0
def getDigitCountand0(number):
    digit_count = 0
    while int(number) > 0:
        number = int(number / 10)
        digit_count += 1
    return digit_count

for x in range(len(num)):
    min = num[x][3]
    sec = num[x][4]
    print(mins)
    print(secs)
    '''
    if getDigitCountand0(int(start_time)) == 2:
        if int(start_time) >= 24:
            start_time = "00"
        complete = str(start_time) + str(num[x][3]) + str(num[x][4])

    elif getDigitCountand0(int(start_time)) == 4:
        sub = float(start_time) / 100
        hour = int(sub)
        min = sub - int(start_time)
        num[x][3] += int(min * 100)'''
    if getDigitCountand0(mins) < 2:
        mins = "0" + str(mins)

    if getDigitCountand0(secs) < 2:
        num[x][4] = "0" + str(secs)

    if int(secs) >= 60:
        secs = 00
        mins += 1
    if int(mins) >= 60:
        start_time += 1
    complete = str(start_time) + str(mins) + str(secs)
    dist_speed_chart2[x].append(complete)

print(dist_speed_chart2)

print(int(num[0][3]) + int(num[1][3]))

