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

#Variabel
# Membuat variabel
nama = "Rhevan"
umur = 16
tinggi = 162
is_active = True

print(nama)      # Rhevan
print(umur)      # 16
print(tinggi)    # 162
print(is_active) # True
# Aturan penamaan
# contoh yang benar
first_name = "Budi"
total_harga = 10000
# contoh yang salah
# 2nama = "Salah"     # ❌ diawali angka
# class = "Informatika" # ❌ keyword Python
# Multiple Assignment
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30
#juga bisa memberika nilai yang sama ke beberapa variabel sekaligus
x = y = z = 100
print(x, y, z)  # 100 100 100
# Mengecek Tipe Data Variabel
nama = "Rhevan"
umur = 16
tinggi = 162

print(type(nama))   # <class 'str'>
print(type(umur))   # <class 'int'>
print(type(tinggi)) # <class 'float'>
x = 10
print(x)  # 10

del x
# print(x)  # ❌ Error karena variable sudah dihapus

#Konstanta
# konvensi penulisan konstanta
PI = 3.14159
MAX_USERS = 100
APP_NAME = "Aplikasi Belajar Python"
# walaupun  secara teknis nilai tersebut masih bisa diubah, developer sebaiknya tidak mengubahnya karena melanggar konvensi penamaan konstanta.
#PI = 3.14  # ❌ Secara aturan Python boleh, tapi sebaiknya jangan dilakukan
# Konstanta di Dalam Module
# constants.py
PI = 3.14159
GRAVITY = 9.8
MAX_RETRY = 3
# lalu, konstanta tersebut bisa digunakan di file python lain dengan cara mengimpor:
from constants import PI, GRAVITY, MAX_RETRY

print("Nilai PI:", PI)
print("Gravitasi:", GRAVITY)
print("Maksimum Percobaan:", MAX_RETRY)
# Contoh Penggunaan Konstanta
TAX_RATE = 0.1  # 10% pajak

harga_barang = 50000
total = harga_barang + (harga_barang * TAX_RATE)

print("Total harga:", total)


