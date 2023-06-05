import mysql.connector
from datetime import datetime
dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
import os
from prettytable import from_db_cursor
import matplotlib.pyplot as plt
from getpass import getpass




db = mysql.connector.connect(
  host="localhost",
  user="root",  
  passwd="",
  database="db_valen"
)
cursor = db.cursor()


def login():
    # memanggil data username dan password, kemudian disimpan di variabel nama1, 2, 3 agar bisa dipanggil
    # untuk dilakukkan validasi
    sql1 = "SELECT username FROM tb_user WHERE nama_kasir='Mbak Kasir 1'"
    cursor.execute(sql1,)
    nama1=cursor.fetchall()[0][0]

    sql1 = "SELECT username FROM tb_user WHERE nama_kasir='Mbak Kasir 2'"
    cursor.execute(sql1,)
    nama2=cursor.fetchall()[0][0]

    sql1 = "SELECT username FROM tb_user WHERE nama_kasir='Mbak Kasir 3'"
    cursor.execute(sql1,)
    nama3=cursor.fetchall()[0][0]

    sql1 = "SELECT password FROM tb_user WHERE nama_kasir='Mbak Kasir 1'"
    cursor.execute(sql1,)
    pass1=cursor.fetchall()[0][0]

    sql1 = "SELECT password FROM tb_user WHERE nama_kasir='Mbak Kasir 2'"
    cursor.execute(sql1,)
    pass2=cursor.fetchall()[0][0]

    sql1 = "SELECT password FROM tb_user WHERE nama_kasir='Mbak Kasir 3'"
    cursor.execute(sql1,)
    pass3=cursor.fetchall()[0][0]


    # buat beberapa variabel dibawah menjadi variabel global agar bisa daipanggil di funct yang lain
    global kasirIndikator1, kasirIndikator3, kasirIndikator2, kasir1, kasir2, kasir3

    print("="*70)
    print("Silahkan Login Menggunakan Username Dan Password yang Valid")
    print("="*70)

    # menggunakan looping while agar apabila username atau password yang
    # dimasukkan salah, maka akan diminta memasukkan user dan password ulang
    # tanpa terjadinya eror
    ulanggggg = True
    while ulanggggg==True :
        user = input("Masukkan Username : ")
        passw = getpass("Masukkan Password : ")
        # validasi user dan password
        if user == nama1 and passw == pass1:
            kasirIndikator1 = True
            kasirIndikator2 = False
            kasirIndikator3 = False
            kasir1 = "Mbak Kasir 1"
            print("anda berhasil login sebagai Mbak Kasir 1")
            input("Press [ENTER} to continue")
            os.system("cls")
            while (True):
                show_menu(db)
                ulanggggg=False
                

        elif user == nama2 and passw == pass2:
            
            kasirIndikator1 = False
            kasirIndikator2 = True
            kasirIndikator3 = False
            kasir2 = "Mbak Kasir 2"
            print("anda berhasil login sebagai Mbak Kasir 2")
            input("Press [ENTER} to continue")
            os.system("cls")
            while (True):
                show_menu(db)
                ulanggggg=False
                
        
        elif user == nama3 and passw == pass3:
            
            kasirIndikator3 = True
            kasirIndikator2 = False
            kasirIndikator1 = False
            kasir3 = "Mbak Kasir 3"
            print("anda berhasil login sebagai Mbak Kasir 3")
            input("Press [ENTER} to continue")
            os.system("cls")
            while (True):
                show_menu(db)
                ulanggggg=False


        else:
            print("Username atau password salah! \nlogin gagal")
            input("Press [ENTER} to continue")
            os.system("cls")
            ulanggggg=True

def menu_kasir(db):
      print("""
      v^v^v^vv^v^v^vv^v^v^vv^v^v^vv^v^v^v^vv^v^v^v^vv^v
      
      List Paket Yang Tersedia 
      
      v^v^v^vv^v^v^vv^v^v^vv^v^v^vv^v^v^v^vv^v^v^v^vv^v

      1. Paket Kere Hore (1 Ayam KAEPCHI + KokaKola) : Rp 20.000
      2. Paket Single (1 Ayam KAEPCHI (+Nasi) + KokaKola) : Rp 30.000
      3. Paket Couple (2 Porsi Ayam KAEPCHI (+Nasi) + 2 KokaKola) : Rp 55.000
      4. Paket Sekeluarga (4 Porsi Ayam KAEPCHI (+Nasi) + 4 KokaKola) : Rp 105.000
      5. Paket Se-RT (10 Porsi Ayam KAEPCHI (+Nasi) + 10 KokaKola + 5 Friench Fries) : Rp 270.000

      ==============================
        """
      )
      # menggunakan looping while agar user (kasir) bisa menginputkan beberapa pesanan
      # sekaligus
      ulang = True
      namaPelanggan = input("Masukkan Nama Pelanggan : ")
      while ulang==True :
        jp = int(input("Masukan jenis paket: "))
        banyak_pesanan = int(input("Masukan banyak pesanan: "))
        if jp == 1:
          cursor=db.cursor()
          jenis_paket = "Paket Kere Hore"
          harga_satuan = 20000
          id_paket = 111
          sub_total = banyak_pesanan*harga_satuan
          harga_total = sub_total
          val = (namaPelanggan, jenis_paket, banyak_pesanan, sub_total,)
          sql = "INSERT INTO tb_detil (nama_pelanggan, jenis_paket, banyak_pesanan, sub_total) VALUES (%s, %s, %s, %s)"
          cursor.execute(sql, val)
          db.commit()
          timestamp = dt
          if kasirIndikator1 == True:
            kasir=kasir1
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator2 == True:
            kasir=kasir2
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator3 == True:
            kasir=kasir3
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()

        elif jp == 2:
          cursor=db.cursor()
          jenis_paket = "Paket Single"
          harga_satuan = 30000
          id_paket = 112
          sub_total = banyak_pesanan*harga_satuan
          harga_total = sub_total
          val = (namaPelanggan, jenis_paket, banyak_pesanan, sub_total)
          sql = "INSERT INTO tb_detil (nama_pelanggan, jenis_paket, banyak_pesanan, sub_total) VALUES (%s, %s, %s, %s)"
          cursor.execute(sql, val)
          db.commit()
          timestamp = dt
          if kasirIndikator1 == True:
            kasir=kasir1
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator2 == True:
            kasir=kasir2
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator3 == True:
            kasir=kasir3
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()

        elif jp == 3:
          cursor=db.cursor()
          jenis_paket = "Paket Couple"
          harga_satuan = 55000
          id_paket = 113
          sub_total = banyak_pesanan*harga_satuan
          harga_total = sub_total
          val = (namaPelanggan, jenis_paket, banyak_pesanan, sub_total)
          sql = "INSERT INTO tb_detil (nama_pelanggan, jenis_paket, banyak_pesanan, sub_total) VALUES (%s, %s, %s, %s)"
          cursor.execute(sql, val)
          db.commit()
          timestamp = dt
          if kasirIndikator1 == True:
            kasir=kasir1
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator2 == True:
            kasir=kasir2
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator3 == True:
            kasir=kasir3
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()

        elif jp == 4:
          cursor=db.cursor()
          jenis_paket = "Paket Sekeluarga"
          harga_satuan = 105000
          id_paket = 114
          sub_total = banyak_pesanan*harga_satuan
          harga_total = sub_total
          val = (namaPelanggan, jenis_paket, banyak_pesanan, sub_total)
          sql = "INSERT INTO tb_detil (nama_pelanggan, jenis_paket, banyak_pesanan, sub_total) VALUES (%s, %s, %s, %s)"
          cursor.execute(sql, val)
          db.commit()
          timestamp = dt
          if kasirIndikator1 == True:
            kasir=kasir1
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator2 == True:
            kasir=kasir2
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator3 == True:
            kasir=kasir3
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()

        elif jp == 5:
          cursor=db.cursor()
          jenis_paket = "Paket Se-Rt"
          harga_satuan = 275000
          id_paket = 115
          sub_total = banyak_pesanan*harga_satuan
          harga_total = sub_total
          val = (namaPelanggan, jenis_paket, banyak_pesanan, sub_total)
          sql = "INSERT INTO tb_detil (nama_pelanggan, jenis_paket, banyak_pesanan, sub_total) VALUES (%s, %s, %s, %s)"
          cursor.execute(sql, val)
          db.commit()
          timestamp = dt
          if kasirIndikator1 == True:
            kasir=kasir1
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator2 == True:
            kasir=kasir2
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()
          elif kasirIndikator3 == True:
            kasir=kasir3
            val = (id_paket, namaPelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, kasir)
            sql = "INSERT INTO tb_transaksi (id_paket, nama_pelanggan, jenis_paket, banyak_pesanan, harga_satuan, harga_total, timestamp, nama_kasir) VALUES (%s,%s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, val,)
            db.commit()

        print("Detail Pesanan:")
        sql = "SELECT * FROM tb_detil"
        cursor.execute(sql)
        pt = from_db_cursor(cursor)
        print(pt)
        sql1 = "SELECT SUM(sub_total) FROM tb_detil"
        cursor.execute(sql1)
        total_harga=cursor.fetchall()[0][0]
        print("Total harga : Rp",total_harga)
        
        pl = str(input("Ingin Pesan lagi ? <y/n>"))
        if pl == 'y':
          ulang = True
        else:
          ulang = False
          pembayaran(db)
          

def pembayaran(db):
  sql1 = "SELECT SUM(sub_total) FROM tb_detil"
  cursor.execute(sql1)
  total_harga=cursor.fetchall()[0][0]

  ulang_uang=True
  while ulang_uang==True:
    up = int(input("masukkan jumlah uang pelanggan (pilih 0 utk cancel pesanan) : "))
    if up == 0:
      os.system("cls")
      cursor.execute("TRUNCATE TABLE tb_detil")
      db.commit() 
      menu_kasir(db)

    if up < total_harga:
      print("uang anda kurang!")
      ulang_uang=True
      input("Press [ENTER] to continue...")

    else:
      ulang_uang=False
      os.system("cls")
      print("================================================")  
      print("==================S T R U K=====================")  
      print("================================================")  
      sql = "SELECT * FROM tb_detil"
      cursor.execute(sql)
      pt = from_db_cursor(cursor)
      print(pt)
      sql1 = "SELECT SUM(sub_total) FROM tb_detil"
      cursor.execute(sql1)
      total_harga=cursor.fetchall()[0][0]
      db.commit()
      print("Total Harga : Rp",total_harga,"\nUang Anda : Rp",up)
      
      if up>total_harga:
        kembalian=up-total_harga
        print("Kembalian = ",kembalian)
      print("================================================")  
      print("============T E R I M A K A S I H===============") 
      cursor.execute("TRUNCATE TABLE tb_detil")
      db.commit() 
      ulang_uang=False
      input("Press [ENTER] to continue...")
      os.system("cls")




def riwayat_transaksi(db):
    a = int(input("1. Tampilkan Semua Riwayat\n2. Berdasarkan Tanggal Transaksi\n3. Urut berdasarkan waktu(dari yang paling baru)\n4. Tampilkan grafik penjualan Selama Tahun 2023\n5. Tampilkan grafik persentase penjualan berdasarkan jenis paket \n0. Back\n>>"))
    os.system("cls")
    if a == 1:
      cursor = db.cursor()
      sql = "SELECT * FROM tb_transaksi"
      cursor.execute(sql)
      pt = from_db_cursor(cursor)
      if cursor.rowcount <= 0:
        print("tidak ada data")
      else:
        print("====================TAMPILAN SEMUA RIWAYAT=======================")
        print(pt)
        input("Press [ENTER] to continue...")
        os.system("cls")
    elif a == 2:
      cursor = db.cursor()
      lagi = True
      while lagi == True:
        tanggal = input("Masukkan tanggal (format -> YYYY-MM-DD) :")
        sql = "SELECT * FROM tb_transaksi WHERE DATE(timestamp) = %s"
        val = (tanggal,)
        cursor.execute(sql, val)
        pt = from_db_cursor(cursor)
        if cursor.rowcount <= 0 :
          print("tidak ada data")
          input("Press [ENTER] to continue...")
          lagi = True

        else :
          lagi = False
          print("===========TAMPILAN RIWAYAT BERDASARKAN TANGGAL==============")
          print(pt)
          input("Press [ENTER] to continue...")
          os.system("cls")
    elif a == 3:
      cursor = db.cursor()
      sql = "SELECT * FROM tb_transaksi ORDER BY timestamp DESC"
      cursor.execute(sql)
      pt = from_db_cursor(cursor)
      print("========TAMPILAN RIWAYAT BERDASARKAN URUTAN WAKTU (DARI YANG PALING BARU)==========")
      print(pt)
      input("Press [ENTER] to continue...")
      os.system("cls")
    elif a == 4:
      # januari
      cursor = db.cursor()
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '01' AND YEAR(timestamp) = '2022' "
      cursor.execute(sql)
      total_penjualan1=cursor.fetchall()[0][0]

      # Februari
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '02' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan2=cursor.fetchall()[0][0]

      # Maret
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '03' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan3=cursor.fetchall()[0][0]

      # April
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '04' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan4=cursor.fetchall()[0][0]

      # Mei
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '05' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan5=cursor.fetchall()[0][0]

      # Juni
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '06' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan6=cursor.fetchall()[0][0]
      
      # Juli
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '07' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan7=cursor.fetchall()[0][0]
      
      # Aagustus
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '08' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan8=cursor.fetchall()[0][0]
      
      # September
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '09' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan9=cursor.fetchall()[0][0]
      
      # Oktober
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '10' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan10=cursor.fetchall()[0][0]
      
      # November
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '11' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan11=cursor.fetchall()[0][0]
      
      # Desember
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE MONTH(timestamp) = '12' AND YEAR(timestamp) = '2022'  "
      cursor.execute(sql)
      total_penjualan12=cursor.fetchall()[0][0]

      # bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
      # Total = [total_penjualan1,total_penjualan2,total_penjualan3,total_penjualan4,total_penjualan5,total_penjualan6,total_penjualan7,total_penjualan8,total_penjualan9,total_penjualan10,total_penjualan11,total_penjualan12]
      data = {"Januari":total_penjualan1, "Februari":total_penjualan2, "Maret":total_penjualan3, "April":total_penjualan4, "Mei":total_penjualan5, "Juni":total_penjualan6, "Juli":total_penjualan7, "Agustus":total_penjualan8, "September":total_penjualan9, "Oktober":total_penjualan10, "November":total_penjualan11, "Desember":total_penjualan12}
      os.system("cls")
      # plt.figure(figsize=(12,7))
      # plt.bar(data.keys(), data.values, color="indigo")

      fig, ax = plt.subplots()
      ax.bar(data.keys(), data.values(), color='indigo')

      ax.set_xticklabels(data.keys())

      for i, v in enumerate(data.values()):
        ax.text(i, v, str(v), color='black', fontweight='bold')

      # plt.title("Penjualan Selama tahun 2022", size=16, bbox={'facecolor':'0.8', 'pad':9})
      plt.title("Penjualan Selama tahun 2022")
      plt.ylabel("Banyak Penjualan", size=14)
      plt.xlabel("Bulan", size=14)
      # plt.xticks(size=12)
      # plt.yticks(size=12)

      plt.show()
          
      input("Press [ENTER] to continue...")
      os.system("cls")
    elif a == 5:
      cursor = db.cursor()
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE id_paket = '111' "
      cursor.execute(sql)
      total_penjualan=cursor.fetchall()[0][0]
      db.commit()
    
      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE id_paket = '112' "
      cursor.execute(sql)
      total_penjualan1=cursor.fetchall()[0][0]
      db.commit()

      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE id_paket = '113' "
      cursor.execute(sql)
      total_penjualan2=cursor.fetchall()[0][0]
      db.commit()

      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE id_paket = '114' "
      cursor.execute(sql)
      total_penjualan3=cursor.fetchall()[0][0]
      db.commit()

      sql = "SELECT SUM(banyak_pesanan) FROM tb_transaksi WHERE id_paket = '115' "
      cursor.execute(sql)
      total_penjualan4=cursor.fetchall()[0][0]
      db.commit()

      labels = ['Paket Kere Hore', 'Paket Single', 'Paket Couple', 'Paket Sekeluarga', 'Paket Se-Rt']
      data = [total_penjualan, total_penjualan1, total_penjualan2, total_penjualan3, total_penjualan4]

      colors = ["#1f77b4", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

      explode = (0, 0, 0, 0, 0)  

      plt.pie(data='linewidth', explode=3, labels='edgecolor', colors='white', labeldistance=1, wedgeprops = { },
      autopct='%1.1f%%', shadow=False, startangle=140)
      plt.title("Grafik Penjualan\n" + "Berdasarkan Jenis Paket")
      plt.show()

      input("Press [ENTER] to continue...")
      os.system("cls")
    elif a == 6:
      cursor = db.cursor()
      ulangii = True
      while ulangii == True:
        nama = input("Masukkan Nama Pelanggan :")
        sql = "SELECT * FROM tb_transaksi WHERE nama_pelanggan = %s"
        val = (nama,)
        cursor.execute(sql, val)
        pt = from_db_cursor(cursor)
        if cursor.rowcount <= 0 :
          print("tidak ada data")
          input("Press [ENTER] to continue...")
          ulangii = True

        else :
          ulangii = False
          print("===========TAMPILAN RIWAYAT BERDASARKAN NAMA==============")
          print(pt)
          cl = input("mau cari lagi?<y/n>")
          if cl == 'y' or 'Y':
            ulangii = True
          else:
            ulangii = False
            break
          # os.system("cls")


    elif a == 0:
      show_menu(db)
def delete_data(db):
    i = int(input("1. Hapus berdasarkan id transaksi\n2. Hapus Semua Riwayat\n0. Back\n>>"))
    if i == 1:
        os.system("cls")
        sql = "SELECT * FROM tb_transaksi"
        cursor.execute(sql)
        pt = from_db_cursor(cursor)
        print("====================TAMPILAN SEMUA RIWAYAT=======================")
        print(pt)
        id_transaksi = int(input("pilih id transaksi> "))
        sql = "DELETE FROM tb_transaksi WHERE id_transaksi=%s"
        val = (id_transaksi,)
        a = str(input("Apakah anda yakin ingin menghapus data ? <y/n>"))
        if a == "y":
            os.system("cls")
            cursor.execute(sql, val)
            db.commit()
            print("{} data berhasil dihapus".format(cursor.rowcount))
        else:
            os.system("cls")
            print("data tidak jadi dihapus")

        input("Press [ENTER] to continue...")
        os.system("cls")
    elif i == 2:
        os.system("cls")
        b = str(input("Apakah anda yakin ingin menghapus semua data ? <y/n>"))
        if b == "y":
            cursor.execute("TRUNCATE TABLE tb_transaksi")
            db.commit()
            print("semua data berhasil dihapus".format(cursor.rowcount))
        else:
            os.system("cls")
            print("data tidak jadi dihapus")
        input("Press [ENTER] to continue...")
        os.system("cls")
    else:
      os.system("cls")
      show_menu(db)



def show_menu(db):
  print("="*70)
  print("Selamat datang di Aplikasi Kasir Mek Donals")
  print("="*70)
  print("1. Menu Utama Kasir")
  print("2. Riwayat Transaksi")
  print("3. Hapus Riwayat Transaksi")
  print("0. Keluar")
  print("---------------------------------------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("cls")

  if menu == "1":
    menu_kasir(db)
  elif menu == "2":
    riwayat_transaksi(db)
  elif menu == "3":
    delete_data(db)
  elif menu == "0":
    okee = str(input("Anda Yakin ingin Keluar? <y/n>"))
    if okee == 'y' or okee == 'Y':
      print("Terimakasih Telah menggunakan program saya")
      exit()
    else:
      print("Perintah keluar dibatalkan")
      input("press [ENTER] to continue")
      os.system("cls")
  else:
    print("Menu salah!")

if __name__=="__main__":
  login()