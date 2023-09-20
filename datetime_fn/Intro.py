import datetime
# Today's Date
date = datetime.datetime.now()
print(date.weekday())  # 0-Monday, 1-Tuesday...

# Calculating how old am I?
years = datetime.datetime.now() - datetime.datetime(2011, 2, 3)
# datetime.datetime.now() - datetime.datetime(2011, 2, 3) gives hours, mins and secs
# years.days/365 because years is in days, and days/ 365 = years
# round because returns in decimal
years = round(years.days/365)
print(years)