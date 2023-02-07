import Mins_seconds
import Rally_Time_Function
import Digit_count_function
dist_speed_chart = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
star = "*"
dash = "_"
flag_off = input("Enter start time - ")
print(star*20, "RALLY TIME TABLE", star*20,"\n",dash*55 )
ans = Rally_Time_Function.time_format(dist_speed_chart, flag_off)
if Digit_count_function.getDigitCountand0(flag_off) == 4:
    print("The FLAG OFF time is ", flag_off[0:2],":",flag_off[2:4],":","00")
if Digit_count_function.getDigitCountand0(flag_off) == 6:
    print("The FLAG OFF time is ", flag_off[0:2], ":", flag_off[2:4], ":", flag_off[4:7])
if Digit_count_function.getDigitCountand0(flag_off) == 2:
    print("The FLAG OFF time is ", flag_off[0:2],":","00",":","00")





