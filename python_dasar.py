#Struktur Dasar Program Python
# Ini adalah komentar
print("Hello, Python!")  # Perintah untuk mencetak teks
#Komentar
# Ini adalah komentar satu baris

"""
Ini komentar multi-baris.
Biasa dipakai untuk dokumentasi.
"""
#Indentasi 
if True:
    print("Kode ini berada di dalam blok if")
    print("Masih di dalam blok if")
print("Kode ini sudah di luar blok if")
#Input dan Output
nama = input("Rhevan: ")
print("Halo,", nama)
#Struktur Program dengan Fungsi
def main():
    print("Hello dari fungsi main!")

if __name__ == "__main__":
    main()

#Tipe Data Dasar
# Integer
umur = 25
print(type(umur))  # <class 'int'>
# Float
tinggi = 170.5
print(type(tinggi))  # <class 'float'>
# String(str)
nama = "Rhevan"
print(type(nama))  # <class 'str'>
# Boolean(bool)
is_active = True
print(type(is_active))  # <class 'bool'>
# List
buah = ["apel", "jeruk", "mangga"]
print(type(buah))  # <class 'list'>
# Tuple
warna = ("merah", "hijau", "biru")
print(type(warna))  # <class 'tuple'>
# Dictionary(dict)
mahasiswa = {"nama": "Rhevan", "umur": 16, "jurusan": "RPL"}
print(type(mahasiswa))  # <class 'dict'>
# Set
angka = {1, 2, 3, 3, 4}
print(angka)  # {1, 2, 3, 4}
print(type(angka))  # <class 'set'>
#Konversi Tipe Data
angka = {1, 2, 3, 3, 4}
print(angka)  # {1, 2, 3, 4}
print(type(angka))  # <class 'set'>
