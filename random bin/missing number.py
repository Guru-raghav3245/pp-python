series = [-1, -2, -4, -5]
x = 0
t = 0
if series[-1] + 1 < 0:
    a = -(series[-1] + 1)
else:
    a = series[-1] + 1
for i in range(a):
    x = x + i
    i += 1
    print(i)
print(x)

for y in range(len(series)):
    t = t + series[y]
print(t)

print("The missing number is -", x - t)  
