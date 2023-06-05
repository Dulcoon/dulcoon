import mysql.connector
import os
from prettytable import from_db_cursor
import matplotlib.pyplot as plt


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_valen"
)
cursor = db.cursor()

def tampil(db):
  cursor = db.cursor()
  query = 'SELECT * FROM tb_niali'
  cursor.execute(query)
  sales = cursor.fetchall()

  npm = []
  rata2 = []
  for sale in sales:
    npm.append(sale[2])
    rata2.append(sale[8])

  plt.plot(npm, rata2)
  plt.xlabel('Nama')
  plt.ylabel("Rata-Rata")
  plt.title('Grafik Rata-rata nilai siswa')
  plt.show()

  # sql = "SELECT (NPM) FROM tb_niali"
  # cursor.execute(sql)
  # sales = cursor.fetchall()





ulang = True
while ulang == True:
  NPM = int(input("Masukkan NPM : "))
  nama = input("Masukkan Nama : ")
  nilaia = int(input("Masukkan nilaia : "))
  nilaib = int(input("Masukkan nilaib : "))
  nilaic = int(input("Masukkan nilaic : "))
  nilaid = int(input("Masukkan nilaid : "))
  nilaie = int(input("Masukkan nilaie : "))
  rata = (nilaia + nilaib + nilaic + nilaid + nilaie) / 5


  val = (NPM, nama, nilaia, nilaib, nilaic, nilaid, nilaie, rata)
  sql = "INSERT INTO tb_niali (NPM, Nama, Nilai_A, Nilai_B, Nilai_C, Nilai_D, Nilai_E, rata_rata) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
  cursor.execute(sql, val,)
  db.commit()
  a = input("Input lagi? <y/n>")
  if a == 'y':
    ulang = True
  else :
    ulang = False
    tampil(db)
    



# NPM, Nama, Nilai A, Nilai B, Nilai C, Nilai D, Nilai E