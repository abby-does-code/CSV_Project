import csv

import datetime as dt  # MAGIC!

#!) Handle error checking using try and except
# 2) change file to use death valley data

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
# This skips the header row
print(type(header_row))


# Looking at index value as well as column header; what index value is associte with what record
# The Enumerate() function returns both index of each item adn the value of each item as you loop through a list


for index, header in enumerate(header_row):
    print("Index:", index, "Column Header:", header)


highs = []
dates = []
lows = []

# Version 2 (in class):
somedate = "2010-02-18"
converted_date = dt.datetime.strptime(somedate, "%Y-%m-%d")
# This is an example of how the converted datetime works; use the dt.datetime to make datetime work on your weird computer

"""
#VERSION 1
for row in csv_file:
    highs.append(int(row[4]))  # Adjust for death valley file
    converted_date = dt.datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)
    lows.append(int(row[5]))


# Oh no! error with a literal in the csv file.
# Try and except allows us to re-route the code if we have bad information in the file.
# So here's what we do:
"""

# VERSION 2
for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = dt.datetime.strptime(row[2], "%Y-%m-%d")

    except ValueError:
        print(
            f"Missing data for {converted_date}"
        )  # "f" lets you write print statement w/out + and , and whatever
        # Literal string interpretation

    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)


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
# Draws labels diagonally to prevent overlapping

plt.show()
