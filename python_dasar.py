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

#Operator
# Operator Aritmatika
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
# Operator Perbandingan
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True
# Operator Logika
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
#Operator Penugasan
x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x /= 4
print(x)  # 6.0
#Operator Keanggotaan(Membership)
buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)      # True
print("pisang" not in buah) # True
#Operator Identitas
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (b menunjuk objek yang sama dengan a)
print(a is c)     # False (c objek berbeda walau isinya sama)
print(a == c)     # True (nilai isinya sama)

#Control Flow
# Percabangan (if, elif, else)
nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")
# Output: B
# Perulangan (for, while)
# Perulangan for
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

# Output:
# apel
# jeruk
# mangga
# Perulangan while
count = 0
while count < 5:
    print("Hitung:", count)
    count += 1

# Output:
# Hitung: 0
# Hitung: 1
# Hitung: 2
# Hitung: 3
# Hitung: 4
# Break dan Continue
for i in range(1, 6):
    if i == 3:
        continue  # lewati angka 3
    if i == 5:
        break     # hentikan loop saat i == 5
    print(i)

# Output:
# 1
# 2
# 4

#Function
# Membuat Function Sederhana
def sapa():
    print("Halo, selamat datang di Python!")

# Memanggil function
sapa()
# Function dengan Parameter
def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Rhevan")
sapa_nama("Pebrian")
# Function dengan Return Value
def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)
# Default Parameter
def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Rhevan")  # Menggunakan parameter
sapa_orang()        # Menggunakan default
# Function dengan Banyak Argumen (*args dan *kwargs)
# *args
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)  # Bisa input banyak angka


# **kwargs
def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Rhevan", umur=16, kota="Subang")

#List, Tuple, dan Set
# List
# Membuat list
buah = ["apel", "jeruk", "mangga"]

# Akses elemen
print(buah[0])   # apel

# Menambah elemen
buah.append("pisang")

# Mengubah elemen
buah[1] = "anggur"

# Menghapus elemen
buah.remove("mangga")

print(buah)
# Tuple
# Membuat tuple
warna = ("merah", "hijau", "biru")

# Akses elemen
print(warna[1])   # hijau

# Tuple tidak bisa diubah
# warna[0] = "kuning"  # Error

# Tapi bisa diakses dengan loop
for w in warna:
    print(w)
#Set
# Membuat set
angka = {1, 2, 3, 3, 4, 5}

print(angka)  # {1, 2, 3, 4, 5} (duplikat otomatis hilang)

# Menambah elemen
angka.add(6)

# Menghapus elemen
angka.remove(2)

# Operasi himpunan
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}

print(ganjil | genap)   # Union
print(ganjil & genap)   # Intersection
print(ganjil - genap)   # Difference

#Dictionaries
# Membuat dictionary sederhana
mahasiswa = {
    "nama": "Rhevan",
    "umur": 20,
    "jurusan": "Teknik Informatika"
}

print(mahasiswa)
# Mengakses Data
print(mahasiswa["nama"])    # Rhevan
print(mahasiswa.get("umur")) # 20
# Menambahkan dan Mengubah Data
mahasiswa["angkatan"] = 2028   # Menambah data baru
mahasiswa["umur"] = 21         # Mengubah value umur

print(mahasiswa)
# Menghapus Data
mahasiswa.pop("jurusan")   # Menghapus dengan key
del mahasiswa["nama"]      # Menghapus dengan del

print(mahasiswa)
# Iterasi Dictionary
for key, value in mahasiswa.items():
    print(key, ":", value)
# Nested Dictionary
kampus = {
    "mahasiswa1": {"nama": "Rhevan", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])  # Rhevan
