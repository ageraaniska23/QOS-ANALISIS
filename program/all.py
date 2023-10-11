import csv
import math

filename = "ksa.csv"
total_packets = 0
lost_packets = 0
total_delay = 0
num_delays = 0
last_arrival_time = None
total_jitter = 0
num_jitter = 0

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
                if num_delays > 1:
                    jitter = ((num_jitter - 1) / num_jitter) * total_jitter + ((abs(delay - total_jitter / num_jitter)) / num_jitter)
                    total_jitter += math.pow((delay - total_jitter / num_jitter), 2)
                    num_jitter += 1
                else:
                    total_jitter += math.pow(delay, 2)
                    num_jitter += 1
            last_arrival_time = time
        info = row[6]
        if "TCP" in info and "Previous segment not captured" in info:
            lost_packets += 1
        total_packets += 1

if total_packets > 0:
    lost_percentage = (lost_packets / total_packets) * 100
    print("Total paket: {}".format(total_packets))
    print("jumlah Packet : {}".format(lost_packets))
    print("Persentase packet loss: {:.2f}%".format(lost_percentage))
else:
    print("Tidak ada paket yang terdeteksi.")

if num_delays > 0:
    average_delay = total_delay / num_delays
    print("Total delay: {:.6f} detik".format(total_delay))
    print("Rata-rata delay: {:.6f} detik".format(average_delay))
    if num_jitter > 1:
        print("Total jitter: {:.6f} detik".format(total_jitter))
      
    else:
        print("Tidak ada jitter yang ditemukan.")
else:
    print("Tidak ada delay atau jitter yang ditemukan.")
