import csv
from prettytable import PrettyTable
import pandas as pd
import os
from datetime import datetime
waktu_sekarang = datetime.now()
# mengatur format tanggal kedalam HH-BB-TTTT
waktu_format = waktu_sekarang.strftime("%d-%m_%Y")

def tampil_data():
    print("Tanggal     :",waktu_format)
    print("List Mobil Yang Kami Sewakan")
    with open('mobil.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        x = PrettyTable()
        x.field_names = headers
        for row in reader:
            x.add_row(row)
        print(x)


def validasi_plat(plat):
    # fungsi untuk validasi plat nomor mobil
    with open("car.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if plat == row['plat_nomor']:
                if row['status'] == "disewakan":
                    return False
                else:
                    return True
    return False

def hitung_harga(plat, durasi):
    # fungsi untuk menghitung harga total penyewaan
    with open("car.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if plat == row['plat_nomor']:
                harga = int(row['sewa_per_hari']) * int(durasi)
                return harga
    return 0

def sewa_mobil():
    nama = input("Masukkan nama pelanggan: ")
    no_identitas = input("Masukkan no identitas pelanggan: ")
    plat = input("Masukkan plat nomor mobil: ")
    durasi = input("Masukkan durasi penyewaan (dalam hari): ")
    if validasi_plat(plat):
        harga = hitung_harga(plat, durasi)
        print("Harga total penyewaan: Rp. ", harga)
    else:
        print("Maaf, mobil dengan plat tersebut tidak tersedia atau sedang disewakan.")

def show_menu():
  print("="*70)
  print("Selamat datang di Aplikasi Rental Mobil")
  print("="*70)
  print("1. Sewa Mobil")
  print("2. Pengembalian Mobil")
  print("0. Keluar")
  print("---------------------------------------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("cls")

  if menu == "1":
    sewa_mobil()
  elif menu == "2":
    kembalikan()
  elif menu == "0":
    okee = str(input("Anda Yakin ingin Keluar? <y/n>"))
    if okee == 'y' or okee == 'Y':
      print("Terimakasih Telah menggunakan program saya")
      exit()
    else:
      print("Perintah keluar dibatalkan")
      input("press [ENTER] to continue")
      os.system("cls")
    # apabila menu yang diinputkan salah
  else:
    print("Menu salah!")

if __name__ == "__main__":
  while(True):
    show_menu()
