import csv

filename = "rapat.csv"
total_packets = 0
lost_packets = 0

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # skip header row
    for row in csvreader:
        info = row[6]
        if "TCP" in info and "Previous segment not captured" in info:
            lost_packets += 1
        total_packets += 1

if total_packets > 0:
    lost_percentage = (lost_packets / total_packets) * 100
    print("Total paket: {}".format(total_packets))
    print("Paket yang hilang: {}".format(lost_packets))
    print("Persentase paket yang hilang: {:.2f}%".format(lost_percentage))
else:
    print("Tidak ada paket yang terdeteksi.")

    