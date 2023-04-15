ages = [13, 7, 8, 10, 9, 11, 12, 13, 15, 17, 17]
final_ans = []
"""
for char in range(len(ages)):
    if ages[char] < 12:
       ans = ages[char]
       final_ans.append(ans)
print(final_ans)"""

ans = [num for num in ages if num < 12]
print(ans)



