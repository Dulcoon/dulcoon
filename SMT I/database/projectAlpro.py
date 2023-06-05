import mysql.connector
import os
# from fungsi import *


def show_menu(db):
  print("=== APLIKASI PENCATATAN TRANSAKSI ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

    
  #clear screen
  os.system("cls")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    sql = "SELECT * FROM tb_transaksi"
    cursor.execute(sql)
    if cursor.rowcount < 0:
      print("Tidak ada data")
    else:
      prety()
  elif menu == "3":
    update(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_valen"
  )

  def insert_data(db):
    nama_barang = input("Masukan nama barang: ")
    banyak_barang = int(input("Masukan banyak barang: "))
    harga_satuan = int(input("masukkan harga satuan "))
    harga_total = banyak_barang*harga_satuan
    timestamp = dt
    val = (nama_barang, banyak_barang, harga_satuan, harga_total, timestamp)
    sql = "INSERT INTO tb_transaksi (nama_barang, banyak_barang, harga_satuan, harga_total, timestamp) VALUES (%s, %s, %s,%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))
    input("Press [ENTER] to continue...")

def prety():
    sql = "SELECT * FROM tb_transaksi"
    cursor.execute(sql)
    pt = from_db_cursor(cursor)
    print(pt)
    input("Press [ENTER] to continue...")


def search_data(db):
    keyword = str(input("Kata Kunci : "))
    sql = "SELECT * FROM tb_transaksi WHERE nama_barang LIKE %s OR banyak_barang like %s"
    val = ("%{}".format(keyword),"%{}".format(keyword))
    cursor.execute(sql, val)
    pt = from_db_cursor(cursor)
    print(pt)
    input("Press [ENTER] to continue...")

def update(db):
    prety()
    id_transaksi = int(input("pilih id transaksi> "))
    nama_barang =  input("Masukan nama barang: ")
    banyak_barang = int(input("Masukan banyak barang: "))
    harga_satuan = int(input("masukkan harga satuan "))
    harga_total = banyak_barang*harga_satuan
    timestamp = dt
    sql = "UPDATE tb_transaksi SET nama_barang=%s, banyak_barang=%s, harga_satuan=%s, harga_total=%s, timestamp=%s WHERE id_transaksi=%s"
    val = (nama_barang, banyak_barang, harga_satuan, harga_total, timestamp, id_transaksi)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

def delete_data(db):
    prety()
    i = int(input("Ketik <1> untuk menghapus semua data dalam satu baris tabel \nKetik <2> untuk menghapus data tertentu dalam satu baris"))
    if i == 1:
        id_transaksi = input("pilih id transaksi> ")
        sql = "DELETE FROM tb_transaksi WHERE id_transaksi=%s"
        val = (id_transaksi,)
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil diubah".format(cursor.rowcount))
    else:
        # kolom = input("nama kolom yang ingin anda ubah : ")
        # dBaru = input("masukkan data yang ingin dihapus : ")
        # val = (kolom, dBaru)
        cursor.execute("DELETE FROM tb_transaksi WHERE nama_barang='sdf'")
        db.commit()
        print("{} data berhasil diubah".format(cursor.rowcount))


cursor = db.cursor()
while(True):
    show_menu(db)