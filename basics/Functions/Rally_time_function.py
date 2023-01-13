# Getting time with distance and speed
def time(distance, speed):
    mins = (distance / speed) * 60
    print(mins)
    secs = (mins - int(mins)) * 60
    print(int(mins), "mins", int(secs), "secs")



print(time(3, 21))



