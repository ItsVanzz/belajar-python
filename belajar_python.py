print("Halo Python")

#VARIABEL DAN TIPE DATA
# tipe data integers
x = 5
y = 3
z = 5 + 3

print(z)
# tipe data floating numbers
a = 7.5

print(a)

# Variabel string
# menggunakan single quote
myFirstName = 'Rhevan'

# menggunakan double quote
myLastName = "Pebrian"

# penulisan Angka sebagai string
myAge = "16"

# penulisan string multiline
myHobby = """Hobi saya adalah membaca buku."""

# mencetak 2 variabel string dengan perintah print
print(myFirstName + " " + myLastName)
print("Umur saya " + myAge)
print(myHobby)

# Variabel Boolean
# contoh penulisan boolean yang benar
a = True
b = False

print(a)

# contoh penulisan boolean yang salah
# jika dijalankan, pada baris ini akan error
#c = true

#print(c)

#OPERATOR PADA PYTHON
# operator aritmatika
a = 4
b = 2
# Penjumlahan
c = a + b
# Pengurangan
d = a - b
# Perkalian
e = a * b
# Pembagian
f = a / b
# Modulus
g = a % b
# Eksponensial
h = a ** b

# Cetak output
print(c) # 6
print(d) # 2
print(e) # 8
print(f) # 2
print(g) # 0
print(h) # 16

#operator logika
#and:mengembalikan nilai True hanya jika kedua statemen benar
#or:mengembalikan nilai True jika salah satu statemen benar
#not:mengembalikan hasil dari statemen. Mengembalikan False jika statemen True

a = 3
b = 9

# Contoh Penggunaan "and"
print(a < 5 and b > 6) # True
print(a < 5 and b < 6) # False
print(a > 5 and b < 6) # False

# Contoh Penggunaan "or"
print(a < 5 or b > 6) # True
print(a < 5 or b < 6) # True
print(a > 5 or b < 6) # False

# Contoh Penggunaan "not"
print(not(a < 5 or b > 6)) # False
print(not(a > 5 or b < 6)) # True

#KONDISI IF, ELIF, ELSE
#Statemen if else umumnya digunakan untuk mengecek suatu kondisi.
#If
#if bisa digunakan untuk mengecek satu atau banyak kondisi.
#jika pengembalian dari kondisi yang dicek bernilai True, maka statemen if akan dijalankan.
"""
Note:
Penulisan kode di dalam blok atau scope pada Python bergantung pada Indentation (spasi di awal baris). Contoh jika kita ingin 
menulis kode di dalam blok/scope Statemen if, maka penulisanny seperti ini:
"""

# Penulisan yang benar:
if(True):
    print("Benar.") # ada spasi di awal baris (lebih menjorok ke dalam)

# Penulisan yang salah:
#if(True):
#print("Benar.") # tidak ada spasi di awal baris (sejajar dengan kode di atasnya)

x = 5
y = 10

# karena x lebih kecil dari y adalah benar. maka kode di dalam scope statemen if akan dijalankan.
if(x < y):
    print("nilai x lebih kecil dari y.") # ini akan dijalankan

# karena x lebih besar dari y adalah salah. maka kode di dalam scope statemen if tidak akan dijalankan.
if(x > y):
    print("nilai x lebih besar dari y.") # ini tidak akan dijalankan

#Elif
#elif digunakan untuk mengecek kondisi lain jika statemen if bernilai False.
a = 80

# disini kita melakukan pengecekan kedua dan ketiga jika pada statemen if bernilai False. Kode pada blok ini
# akan dijalankan hanya jika statemen elif bernilai True.

# Pengecekan pertama dengan if: if(a > 90)
# Pengecekan kedua dengan elif: elif(a > 70)

if(a > 90):
	print("Dapat nilai A.") # ini tidak akan dijalankan
elif(a > 70):
    print("Dapat nilai B.") # ini akan dijalankan 

#ELSE
#else digunakan untuk mengeksekusi kode jika statemen if dan elif bernilai False.
a = 60

if(a > 90):
	print("Dapat nilai A.") # ini tidak akan dijalankan
elif(a > 70):
    print("Dapat nilai B.") # ini tidak akan dijalankan
else: 
    print("Dapat nilai C.") # ini akan dijalankan

#PERULANGAN PADA PYTHON
#Perulangan digunakan untuk mengeksekusi kode secara berulang-ulang.
#For
#loop_for_1
#Perulangan for digunakan untuk mengeksekusi kode secara berulang-ulang dengan jumlah yang sudah ditentukan.
#Contoh perulangan for untuk mencetak angka 1 sampai
# Mencetak kata "Halo Python" sebanyak 5 kali
for i in range(5):
    print("Halo Python.")
#loop_for_2
# Mencetak semua item pada variabel fruits (lists)
fruits = ['Apple', 'Banana', 'Mango', 'Durian']
for fruit in fruits:
    print(fruit)

# Mencetak semua huruf satu per satu pada kata "Indonesia"
myCountry = "indonesia"
for x in myCountry:
    print(x)

#While
#Perulangan while digunakan untuk mengeksekusi kode secara berulang-ulang selama kondisi bernilai True.
#Contoh perulangan while untuk mencetak angka 1 sampai 5
# Mencetak angka, jika angka lebih kecil dari 5
counter = 0
while counter < 5:
    print(counter)
    counter += 1

#Break dan Continue
#Break digunakan untuk menghentikan perulangan.
#Contoh penggunaan break pada perulangan for
# Menghentikan perulangan jika nilai x adalah 3
# Pada kode di bawah ini, jika nilai x sama dengan 3,
# maka perulangan akan dihentikan. Walaupun seharusnya
# perulangan akan berhenti setelah 5 kali berjalan.
for x in range(5):
    print(x)
    if x == 3:
        break
#Contoh penggunaan break pada perulangan while
# Melewati perulangan jika nilai x adalah angka genap (2, 4, 6 dst)
# Pada kode di bawah ini, hanya akan mencetak angka ganjil 
# karena jika angka adalah genap,maka proses mencetak akan
# kita skip menggunakan keyword "continue"

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

#LIST dan DICTIONARIES 
#List
#list adalah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel.
#list create
# Membuat lists yang berisi nama-nama hewan
animals = ["Ayam", "Bebek", "Cicak"]

# Kita bisa mengakses item di dalam "Lists" berdasarkan urutannya (indexing)
# semisal kita ingin mengakses item "Bebek" (urutan kedua), maka kita bisa menggunakan indexing "1"
# kenapa tidak menggunakan indexing "2"? karena indexing dimulai dari angka 0, bukan 1 (n - 1)

print(animals[1]) # Bebek

# Jika kita ingin mengakses dengan urutan sebaliknya (dari urutan paling akhir),
# kita bisa menggunakan negative indexing
# Jika kita menggunakan indexing "-1", artinya kita mengakses item terakhir
# Jika menggunakan indexing "-2", artinya kita mengakses item kedua dari urutan terakhir

print(animals[-1]) # Cicak
print(animals[-2]) # Bebek

#List add item
animals = ["Ayam", "Bebek", "Cicak"]

# Menambah item pada "Lists" dengan posisi (indexing) terakhir menggunakan function "append"
animals.append("Domba")
print(animals) # ["Ayam", "Bebek", "Cicak", "Domba"]

# Menambah item pada "Lists" dengan posisi (indexing) tertentu menggunakan function "insert"
# Contoh kita ingin menambahkan 1 item dengan posisi ketiga (indexing = 2)

animals.insert(2, "Buaya")
print(animals) # ['Ayam', 'Bebek', 'Buaya', 'Cicak', 'Domba']

#List delete item
animals = ["Ayam", "Bebek", "Cicak"]

# Menghapus item tertentu (Bebek) pada "Lists" dengan method "remove"
animals.remove("Bebek")
print(animals) # ["Ayam", "Cicak"]

# Menghapus item terakhir pada "Lists" dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals) # ["Ayam", "Bebek"]

# Menghapus item berdasarkan posisinya (indexing) pada "Lists" dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop(0)
print(animals) # ["Bebek", "Cicak"]

# Menghapus semua item pada "Lists" dengan method "clear"
animals = ["Ayam", "Bebek", "Cicak"]
animals.clear()
print(animals) # []

#Dictionaries
#dictionaries adalah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel.
#dictionaries create
# Membuat Dictionaries untuk menyimpan informasi biodata seseorang (nama dan umur)
firstPerson = {
   "first_name": "Rhevan",
    "last_name": "Pebrian",
    "age": 10
}

# Untuk mengakses item pada Dictionaries bisa menggunakan 2 cara
# Cara pertama
print(firstPerson['first_name']) # Hana
# Cara kedua dengan method "get"
print(firstPerson.get('age')) # 10

# Untuk mendapatkan semua "keys" dari Dictionaries
print(firstPerson.keys()) # dict_keys(['name', 'age'])

# Untuk mendapatkan semua "values" dari Dictionaries
print(firstPerson.values()) # dict_values(['Hana', 'Malika', 10, 12])

#dictionaries add item
firstPerson = {
   "first_name": "Rhevan",
    "last_name": "Pebrian",
    "age": 10
}

# Menambahkan item ke dalam Dictionaries
# Menambahkan item berat bedan (weight) ke dalam firstPerson
firstPerson['weight'] = 12
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 10, 'weight': 12}

#dictionaries update item
firstPerson = {
   "first_name": "Rhevan",
    "last_name": "Pebrian",
    "age": 10
}

# Ada 2 cara untuk mengubah atau mengupdate sebuah value dari item pada Dictionaries

# Cara Pertama
firstPerson['age'] = 15

# Cara Kedua dengan method "update"
# Jika kita menggunakan cara ini, ketika item yang di update berdasarkan key (age) ditemukan,
# maka akan diupdate.
# Namun jika item belum ada, maka otomatis akan menambahkan item baru
firstPerson.update({"age": 15})
firstPerson.update({"hair_color": "black"})
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 15, 'hair_color': 'black'}

#dictionaries delete item
firstPerson = {
   "first_name": "Rhevan",
    "last_name": "Pebrian",
    "age": 10
}

# Untuk menghapus item dari Dictionaries, kita bisa menggunakan method "pop"
# Kita wajib menambahkan nama "key" jika menggunakan method "pop"
firstPerson.pop("age")
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika'}

# Untuk menghapus semua item, kita bisa menggunakan method "clear"
firstPerson.clear()
print(firstPerson) # {}

#FUNCTION
#Function adalah blok kode yang digunakan untuk mengeksekusi kode tertentu. Function bisa menerima inputan (parameter) dan mengembalikan output (return value).
#Function create
# Membuat function untuk menjumlahkan 2 angka
# Membuat Function baru dengan nama belajar_python
def belajar_python():
    print("Halo")

# Memanggil Function "say_hello"
belajar_python() # Halo

#Function arguments 1
# Membuat Function dengan nama belajar_python yang memiliki satu Arguments "name"
def belajar_python(name):
    print("Halo, Saya %s" % name)

# Memanggil Function belajar_python dengan Arguments "name" berupa string dengan value "Rhevan"
belajar_python("Rhevan") # Halo, Saya Rhevan
#Function arguments 2
# Membuat Function dengan nama belajar_python yang memiliki dua Arguments: "name" dan "age"
def belajar_python(name, age):
    print("Halo, Saya %s. Umur saya %d" % (name, age))

# Memanggil Function belajar_python 
# dengan Arguments "name" berupa string dengan value "Rhevan"
# dan Arguments "age" berupa integer dengan value "16"
belajar_python("Rhevan", 16) # Halo, Saya Rhevan

#Function arbitrary arguments
# Membuat Function dengan nama belajar_python
# yang memiliki Arbitrary Arguments dengan nama "names"
def belajar_python(*names):
    for name in names:
        print("Halo, Saya %s" % name)

# Karena Function di atas memiliki Arbitrary Arguments, 
# maka kita bisa mengirimkan banyak value sebagai Arguments ke dalam Function tersebut
belajar_python("Rhevan", "Fika", "Yudi")

#Function keyword arguments 
def belajar_python(**student):
    print("Halo, Saya %s. Umur Saya %d" % (student['name'], student['age']))

# Memanggil Function belajar_python dengan Arbitrary Keyword Arguments
belajar_python(age=16, name="Rhevan") # Halo, Saya Rhevan. Umur Saya 16

#Function default value arguments
# Membuat Function belajar_python dengan Arguments "name" dan menentukan Default valuenya sebagai "Alien".
def belajar_python(name="Alien"):
    print("Halo, Saya %s" % name)

# Memanggil Function belajar_python tanpa mengirimkan Arguments nya.
belajar_python() # Halo, Saya Alien





