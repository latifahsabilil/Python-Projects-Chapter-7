try:
    namafile = input("Masukkan nama file: ")
    bacafile = open(namafile)
    print("Isi file", namafile, " adalah: ")
    file = bacafile.read()
    print(file)
except FileNotFoundError:
    print('File tidak ditemukan')
