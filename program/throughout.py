import csv

filename = "rapat.csv"
start_time = None
end_time = None
total_bytes = 0

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header row
    for row in csvreader:
        time_str = row[1]
        length_str = row[5]
        if time_str != "" and length_str != "":
            time = float(time_str)
            length = int(length_str)
            if start_time is None:
                start_time = time
            end_time = time
            total_bytes += length

if start_time is not None and end_time is not None:
    duration = end_time - start_time
    throughput_bytes = total_bytes / duration
    throughput_bits = throughput_bytes * 8
    throughput_kbps = throughput_bits / 1000
    print("Total bytes: {} bytes".format(total_bytes))
    print("Time span: {:.6f} seconds".format(duration))
    print("Throughput: {:.2f} bytes/s".format(throughput_bytes))
    print("Throughput: {:.2f} bit/s".format(throughput_bits))
    print("Throughput: {:.2f} kb/s".format(throughput_kbps))
else:
    print("Tidak ada data yang valid.")
