import csv
import math

filename = "ksa.csv"
total_delay = 0
num_delays = 0
last_arrival_time = None

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header row
    for row in csvreader:
        time_str = row[1]
        if time_str != "":
            time = float(time_str)
            if last_arrival_time is not None:
                delay = time - last_arrival_time
                total_delay += delay
                num_delays += 1
            last_arrival_time = time

if num_delays > 0:
    average_delay = total_delay / num_delays
    print("Total delay: {:.6f} detik".format(total_delay))
    print("Rata-rata delay: {:.6f} detik".format(average_delay))
else:
    print("Tidak ada delay yang ditemukan.")
