dist_speed_chart = [[0, 3, 21], [3, 5, 30], [5, 8, 40], [8, 12, 60]]
def time(list):
    ans = []
    for x in range(len(list)):
        y = 0
        distance = list[x][y + 1] - list[x][y]
        speed = list[x][y + 2]

        mins = (distance / speed) * 60
        secs = (mins - int(mins)) * 60
        ans.append(int(mins))
        ans.append(int(secs))

    return ans
print(time(dist_speed_chart))