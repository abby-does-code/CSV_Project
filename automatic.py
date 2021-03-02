import csv
import matplotlib
import datetime as dt


open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
print(type(header_row))


lows_index_no = header_row.index("TMIN")
highs_index_no = header_row.index("TMAX")
dates_index_no = header_row.index("DATE")


## list.index('thing')


dates = []
highs = []
lows = []

for row in csv_file:
    highs.append(int(row([header_row.index("TMAX")])))
    converted_date = dt.datetime.strptime(row[header_row.index("DATE")], "%Y-%m-%d")
    dates.append(converted_date)
    lows.append(row[header_row.index("TMIN")])

print(lows[:10])
# print(highs[:10])

dates2 = []
highs2 = []
lows2 = []
"""
for row in csv_file2:
    highs2.append(row[header_row2.index("TMAX")])
    converted_date = dt.datetime.strptime(row[header_row2.index("DATE")], "%Y-%m-%d")
    dates2.append(converted_date)
    lows2.append(row[header_row2.index("TMIN")])


import matplotlib.pyplot as plt

# fig = plt.figure()


plt.plot(dates, highs, c="red")  # plt is the actual graph object
plt.plot(dates, lows, c="blue")

plt.title("Daily high and low temperatures -  2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)

plt.tick_params(axis="both", labelsize=12)

# fig.autofmt_xdate()
# Draws labels daigonnaly to prevent overlapping

plt.show()


fig = plt.figure()

fig, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[0].plot(dates, lows, c="blue")
a[1].plot(dates2, highs2, c="red")
a[1].plot(dates2, lows2, c="blue")

plt.show()
"""