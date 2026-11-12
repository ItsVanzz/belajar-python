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

#Class dan Object(OOP Dasar)
# Membuat Class Sederhana
# Membuat class
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")

# Membuat object dari class
mhs1 = Mahasiswa("Rhevan", "Teknik Informatika")
mhs2 = Mahasiswa("Siti", "Sistem Informasi")

# Memanggil method
mhs1.sapa()
mhs2.sapa()
# Atribut dan Method
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

pp = PersegiPanjang(5, 3)
print("Luas:", pp.luas())
print("Keliling:", pp.keliling())
# Encapsulation
class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  # private attribute

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        self.__saldo += jumlah

akun = BankAccount(1000)
akun.setor(500)
print("Saldo:", akun.lihat_saldo())

#Encapsulation
# Public, Protected, dan Private
# Public
#self.nama
# Protected
#self._alamat
# Private
#self.__saldo
# Encapsulation dengan Private Attribute
class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal  # private attribute

    # getter
    def lihat_saldo(self):
        return self.__saldo

    # setter
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")

# Membuat objek
akun = BankAccount(1000)

# Mengakses saldo lewat method (bukan langsung)
print("Saldo awal:", akun.lihat_saldo())

akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())

akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())

#Inherritance
# Contoh Inheritance Dasar
# Parent class
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan ini memiliki suara.")

# Child class
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} mengeong: Meow!")

class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

# Membuat objek dari class turunan
kucing = Kucing("Tom")
anjing = Anjing("Spike")

kucing.suara()
anjing.suara()
# Menambahkan Method Baru di Subclass
class Burung(Hewan):
    def suara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):
        print(f"{self.nama} sedang terbang!")
        
burung = Burung("Rio")
burung.suara()
burung.terbang()
# Menggunakan super() untuk Akses Parent 
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")

class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, jurusan, tahun_masuk):
        super().__init__(nama, jurusan)   # memanggil constructor parent
        self.tahun_masuk = tahun_masuk

    def info(self):
        super().info()  # memanggil method parent
        print(f"Tahun Masuk: {self.tahun_masuk}")

maba = MahasiswaBaru("Andi", "Informatika", 2025)
maba.info()

#Polymorphism
# Polymorphism Pada Method
class Kucing:
    def suara(self):
        return "Meow"

class Anjing:
    def suara(self):
        return "Guk guk"

# Polymorphism in action
hewan = [Kucing(), Anjing()]

for h in hewan:
    print(h.suara())
# Polymorphism Dengan Inheritance
class Hewan:
    def suara(self):
        return "Hewan bersuara"

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Semua objek diperlakukan sama sebagai 'Hewan'
daftar_hewan = [Kucing(), Anjing(), Hewan()]

for h in daftar_hewan:
    print(h.suara())
# Polymorphism Dengan Fungsi
def cetak_suara(hewan):
    print(hewan.suara())

cetak_suara(Kucing())
cetak_suara(Anjing())
# Polymorphism dengan Built-in Functions
print(len("Python"))   # string
print(len([1, 2, 3]))  # list
print(len({"a": 1, "b": 2}))  # dictionary

#Abstraction
# Abstraction dengan Abstract Class
from abc import ABC, abstractmethod

# Abstract class
class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

# Subclass yang mengimplementasikan abstract method
class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Tidak bisa langsung membuat object dari class abstract
# h = Hewan()  # Error!

# Hanya bisa dari subclass
k = Kucing()
a = Anjing()

print(k.suara())
print(a.suara())
# Abstraction di Dunia Nyata
from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")

class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")

# Menggunakan abstraction
def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)

# Memanggil dengan berbagai metode
proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Dana(), 75000)

#Exception Handling
#error tanpa exception handling
# Membagi angka dengan nol
 #angka = 10
 #hasil = angka / 0
 #print("Hasil:", hasil)
 
 #ZeroDivisionError: division by zero
# Menangani Exception dengan try-except
try:
    angka = 10
    hasil = angka / 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
# Menangani Banyak Jenis Error
try:
    data = int("abc")   # error konversi string ke int
except ValueError:
    print("Error: Data tidak valid!")
except ZeroDivisionError:
    print("Error: Tidak boleh membagi dengan nol!")
# Menggunakan else dan finally
try:
    angka = 10 / 2
except ZeroDivisionError:
    print("Error: Tidak bisa bagi nol!")
else:
    print("Perhitungan berhasil, hasil:", angka)
finally:
    print("Selesai memproses.")
# Membuat Exception Sendiri
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    else:
        print("Umur valid:", umur)

try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)

#File Handling
# Membuka dan Membaca File
# Membaca isi file
file = open("data.txt", "r")  # "r" = read
print(file.read())
file.close()
# Membaca File Baris per Baris
file = open("data.txt", "r")
for baris in file:
    print(baris.strip())  # strip() untuk hapus newline
file.close()
# Menulis ke File
# Menulis file baru atau menimpa file lama
file = open("data.txt", "w")
file.write("Halo, ini data baru!\n")
file.write("Baris kedua...\n")
file.close()
# Menambah Data ke File
# Menambah data di akhir file
file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()
# Contoh Program Lengkap
# Menulis file
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# Menambah data
with open("contoh.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

# Membaca file
with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())

#Module
# Membuat Module 
# matematika.py

# Menggunakan Module
# main.py
import matematika

print(matematika.tambah(2, 3))   # Output: 5
print(matematika.kali(4, 5))     # Output: 20
# Import dengan Alias
import matematika as m

print(m.tambah(10, 5))   # Output: 15
# Import Fungsi Tertentu
from matematika import tambah

print(tambah(7, 3))   # Output: 10
# Build-in Modules
import math

print(math.sqrt(16))   # Akar kuadrat → 4.0
print(math.pi)         # Nilai π → 3.141592653589793

#Package
# Struktur Package
#my_package/
#│
#├── __init__.py
#├── operasi.py
#├── geometri.py
# Menggunakan Package
from my_package import operasi, geometri

print(operasi.kurang(10, 4))        # Output: 6
print(geometri.luas_persegi(5))     # Output: 25
# Import Fungsi Tertentu dari Package
from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print(kurang(20, 7))          # Output: 13
print(luas_persegi(8))        # Output: 64
# Package di Python Standar Library
import os
print(os.getcwd())   # Menampilkan direktori kerja saat ini
import datetime
print(datetime.date.today())  # Menampilkan tanggal hari ini
