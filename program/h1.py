import csv
import matplotlib.pyplot as plt

# Membaca file CSV KSA
with open('h1.csv', 'r') as file1:
    reader1 = csv.reader(file1)

    # Membaca header
    header1 = next(reader1)

    # Membuat dictionary kosong untuk menyimpan nilai indeks KSA
    indeks_dict1 = {}

    # Looping melalui setiap baris data
    for row in reader1:
        # Mendapatkan nilai parameter, nilai, indeks, dan kategori
        parameter = row[0]
        nilai = float(row[1])
        indeks = row[2]
        kategori = row[3]

        # Menambahkan nilai indeks ke dictionary dengan kategori sebagai key
        if kategori not in indeks_dict1:
            indeks_dict1[kategori] = [(parameter, nilai)]
        else:
            indeks_dict1[kategori].append((parameter, nilai))

    # Membaca file CSV Ruang Rapat
    with open('h2.csv', 'r') as file2:
        reader2 = csv.reader(file2)

        # Membaca header
        header2 = next(reader2)

        # Membuat dictionary kosong untuk menyimpan nilai indeks Ruang Rapat
        indeks_dict2 = {}

        # Looping melalui setiap baris data
        for row in reader2:
            # Mendapatkan nilai parameter, nilai, indeks, dan kategori
            parameter = row[0]
            nilai = float(row[1])
            indeks = row[2]
            kategori = row[3]

            # Menambahkan nilai indeks ke dictionary dengan kategori sebagai key
            if kategori not in indeks_dict2:
                indeks_dict2[kategori] = [(parameter, nilai)]
            else:
                indeks_dict2[kategori].append((parameter, nilai))

    # Membuat diagram garis untuk file CSV KSA
    for kategori, data in indeks_dict1.items():
        # Mengurutkan data berdasarkan parameter
        data.sort(key=lambda x: x[0])

        # Membuat dua list terpisah untuk parameter dan nilai
        parameter_list = [x[0] for x in data]
        nilai_list = [x[1] for x in data]

        # Membuat diagram garis dengan warna merah
        plt.plot(parameter_list, nilai_list, label=kategori, color='red')

    # Membuat diagram garis untuk file CSV Ruang Rapat
    for kategori, data in indeks_dict2.items():
        # Mengurutkan data berdasarkan parameter
        data.sort(key=lambda x: x[0])

        # Membuat dua list terpisah untuk parameter dan nilai
        parameter_list = [x[0] for x in data]
        nilai_list = [x[1] for x in data]

        # Membuat diagram garis dengan warna biru
        plt.plot(parameter_list, nilai_list, label=kategori, color='blue')

    # Menambahkan legenda, label sumbu, dan judul
    plt.legend()
    plt.xlabel("Parameter")
    plt.ylabel("Indeks")
    plt.title("Statistik Indeks KSA dan Ruang Rapat")

    # Menampilkan diagram garis
    plt
