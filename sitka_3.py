import csv
import datetime as dt  # MAGIC!

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# Looking at index value as well as column header; what index value is associte with what record

# The Enumerate() function returns both index of each item adn the value of each item as you loop through a list

for index, header in enumerate(header_row):
    print("Index:", index, "Column Header:", header)

# output is  a tuple!

highs = []
dates = []
lows = []


# Version 2 (in class):
somedate = "2010-02-18"
converted_date = dt.datetime.strptime(somedate, "%Y-%m-%d")
# This is an example of how the converted datetime works; use the dt.datetime to make datetime work on your weird computer

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = dt.datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)
    lows.append(int(row[6]))


# ctrl + option + n to run code


import matplotlib.pyplot as plt


fig = plt.figure()


plt.plot(dates, highs, c="red")  # plt is the actual graph object
plt.plot(dates, lows, c="blue")

plt.title("Daily high and low temperatures -  2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)

plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()
# Draws labels daigonnaly to prevent overlapping

plt.show()

##ASSIGNMENT!##

fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
