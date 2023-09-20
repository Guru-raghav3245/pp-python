# Allows to pass a date and modify it for our purposes
# Go to python3 datetime on Google for parameters
import datetime
parsed_date = datetime.datetime.strptime("Jan 15, 2018", "%b %d, %Y")
print(parsed_date)
