import csv

filename = "rapat.csv"
total_delay = 0
num_delays = 0
last_arrival_time = None
total_jitter = 0
num_jitter = 0

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  
    for row in csvreader:
        time_str = row[1]
        if time_str != "":
            time = float(time_str)
            if last_arrival_time is not None:
                delay = time - last_arrival_time
                total_delay += delay
                num_delays += 1
                if num_delays > 1:
                    jitter = delay - last_delay
                    total_jitter += jitter
                    num_jitter += 1
                last_delay = delay
            last_arrival_time = time

if num_delays > 0:
    average_delay = total_delay / num_delays
    print("Rata-rata JITTER: {:.6f} milidetik".format(average_delay * 1000))
else:
    print("Tidak ada jitter yang ditemukan.")

    