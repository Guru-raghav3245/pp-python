import Mins_seconds
import Rally_Time_Function
import Digit_count_function
dist_speed_chart = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
star = "*"
dash = "_"
flag_off = input("Enter start time - ")
print(star*20, "RALLY TIME TABLE", star*20, "\n", dash*55)
ans = Rally_Time_Function.time_format(dist_speed_chart, flag_off)
if Digit_count_function.getDigitCountand0(flag_off) == 4:
    print("The FLAG OFF time is ", flag_off[0:2], ":", flag_off[2:4], ":", "00")
if Digit_count_function.getDigitCountand0(flag_off) == 6:
    print("The FLAG OFF time is ", flag_off[0:2], ":", flag_off[2:4], ":", flag_off[4:7])
if Digit_count_function.getDigitCountand0(flag_off) == 2:
    print("The FLAG OFF time is ", flag_off[0:2], ":", "00", ":", "00")
print(dash*55)
print("From", "   To", "   Avg speed", "   Time", "   Arrival time")
print(dash*55)
print("KM", "     KM", "   KM/HR", "     hh:mm:ss ", "  hh:mm:ss ")
print(dash*55)
for x in range(len(ans)):

    if int(ans[x][4]) >= 60:
        ans[x][4] = ans[x][4] - 60
        ans[x][3] += 1
    if int(ans[x][3]) >= 60:
        start_time = int(start_time)
        start_time += 1
        ans[x][3] = ans[x][3] - 60
    if ans[x][4] == 0:
        ans[x][4] = "00"
    if ans[x][3] == 0:
        ans[x][3] = "00"
    if Digit_count_function.getDigitCountand0(ans[x][0]) < 2:
        ans[x][0] = "0" + str(ans[x][0])

    if Digit_count_function.getDigitCountand0(ans[x][1]) < 2:
        ans[x][1] = "0" + str(ans[x][1])

    if Digit_count_function.getDigitCountand0(ans[x][2]) < 2:
        ans[x][2] = "0" + str(ans[x][2])

    if Digit_count_function.getDigitCountand0(ans[x][4]) < 2:
        ans[x][3] = "0" + str(ans[x][3])

    print(ans[x][0], "\t", "\t", ans[x][1], "\t", ans[x][2], "\t", ans[x][3], ans[x][4], "\t", "\t", ans[x][5])



