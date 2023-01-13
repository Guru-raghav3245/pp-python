dist_speed_chart = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
def time(list):
    for x in range(len(list)):
        y = 0
        distance = list[x][y + 1] - list[x][y]
        speed = list[x][y + 2]

        mins = (distance / speed) * 60
        print(mins)
        secs = (mins - int(mins)) * 60
        print(int(mins), "mins", int(secs), "secs")
        list[x].append(int(mins))
        list[x].append(int(secs))

    return list

print(time(dist_speed_chart))

