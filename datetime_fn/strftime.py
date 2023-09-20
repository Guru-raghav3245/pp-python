# Converts an int date into a str date, opposite of strftime
import datetime
str_d = datetime.datetime.strftime(datetime.datetime.now(), "%b %d,%Y")
print(str_d)