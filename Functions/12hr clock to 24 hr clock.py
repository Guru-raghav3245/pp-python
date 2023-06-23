# Converts 12hr clock to 24hr clock
def time_conversion(time):
    time = time.split()
    time = "".join(time)
    hour = int(time[0] + time[1])
    amorpm = input("AM OR PM - ")
    amorpm = amorpm.upper()
    if amorpm == "PM":
        hour += 12
    if hour == 24:
        hour = "00"

    hour = str(hour)
    time1 = hour + ":" + time[2:4] + ":" + time[4:6]

    return time1


if __name__ == "__main__":
    time_str = input("Enter time - ")
    time_parts = time_conversion(time_str)
    print(time_parts)