# Getting time with distance and speed
def time(distance, speed):
    x = distance / speed
    if type(x) == float:
        hours = int(x)
        y = x - hours
        mins = y * 60
        z = mins - int(mins)
        secs = z * 60
        print("hours = ",hours  , "mins =", mins  ,"  seconds = ",secs)
    else:
        print(int(x))

time(20, 10)



