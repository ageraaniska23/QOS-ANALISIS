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
start_time = None
end_time = None
total_bytes = 0

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header row
    for row in csvreader:
        time_str = row[1]
        length_str = row[5]
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
        info = row[6]
        if "TCP" in info and "Previous segment not captured" in info:
            lost_packets += 1
        total_packets += 1
        
        if length_str != "":
            length = int(length_str)
            if start_time is None:
                start_time = time
            end_time = time
            total_bytes += length

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
    if num_jitter > 0:
        average_jitter = total_jitter / num_jitter
        print("Rata-rata JITTER: {:.6f} detik".format(average_jitter))
    else:
        print("Tidak ada jitter yang ditemukan.")
else:
    print("Tidak ada delay atau jitter yang ditemukan.")

if start_time is not None and end_time is not None:
    duration = end_time - start_time
    throughput_bytes = total_bytes / duration
    throughput_bits = throughput_bytes * 8
    print("Total bytes: {} bytes".format(total_bytes))
    print("Time span: {:.6f} seconds".format(duration))
    print("Throughput: {:.2f} bytes/s \n= {:.2f} bit/s".format(throughput_bytes, throughput_bits))
else:
    print("Tidak ada data yang valid.")
