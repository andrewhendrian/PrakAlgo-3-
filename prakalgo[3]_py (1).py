# -*- coding: utf-8 -*-
"""PrakAlgo[3].py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13L9PkfyWHR8GlnaWELe0JjmOJZUlMf8r
"""

print('@@@@ @@   @ @@@@@  @@@@  @@@@@@ @       @')
print('@  @ @ @  @ @    @ @   @ @      @       @')
print('@@@@ @  @ @ @    @ @   @ @@@@@@ @   @   @')
print('@  @ @   @@ @    @ @@@@  @      @   @   @')
print('@  @ @    @ @@@@@  @   @ @@@@@@ @@@@@@@@@')

angka_awal = int(input("Masukkan angka awal: "))
angka_akhir = int(input("Masukkan angka akhir: "))

if angka_awal > angka_akhir:
    angka_awal, angka_akhir = angka_akhir, angka_awal

i = angka_awal
j = angka_akhir

while i <= j:
    print(f"{i} | {j}")
    i+=1
    j-=1

print('@@@@ @@   @ @@@@@  @@@@  @@@@@@ @       @')
print('@  @ @ @  @ @    @ @   @ @      @       @')
print('@@@@ @  @ @ @    @ @   @ @@@@@@ @   @   @')
print('@  @ @   @@ @    @ @@@@  @      @   @   @')
print('@  @ @    @ @@@@@  @   @ @@@@@@ @@@@@@@@@')
def hitung_kembalian(total_harga, jumlah_uang):
    if total_harga > jumlah_uang:
        print("Uang yang diberikan kurang dari total harga belanja.")
        return

    kembalian = jumlah_uang - total_harga
    print(f"Kembalian: {kembalian}")

    uang_kertas = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    print("Rincian kembalian:")
    i = 0
    while kembalian > 0 and i < len(uang_kertas):
        lembar_uang = uang_kertas[i]
        if kembalian >= lembar_uang:
            jumlah_lembar = kembalian // lembar_uang
            kembalian %= lembar_uang
            print(f"uang {lembar_uang} Rupiah : {jumlah_lembar} lembar")
        i += 1

total_harga = int(input("Masukkan total harga belanjaan: "))
jumlah_uang = int(input("Masukkan jumlah uang: "))

hitung_kembalian(total_harga, jumlah_uang)

