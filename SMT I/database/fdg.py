import mysql.connector

# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = ""
# )
# if db.is_connected:
#     print("jsbdbcb")



db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_valen"
)
cursor = db.cursor()
sql = """CREATE TABLE tb_transaksi (
  id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
  nama_barang VARCHAR(50),
  banyak_barang INT(3),
  harga_satuan INT(20),
  harga_total INT(20),
  timestamp DATETIME(6)
)
"""
cursor.execute(sql)
print("oke")






    if pl == "y":

    else:
      print("Detail Pesanan : ")
      if nambah==0:
        print("satu pesanan")
        print("Jenis Paket = ",jenis_paket,"\nBanyak pesanan",banyak_pesanan,"\nharga total =",harga_total)
      elif nambah>0:
        print("multipel pesanan")
        if paketA==True:
          print("Jenis Paket = ",jenis_paket1,"\nBanyak pesanan",banyak_pesanan1,)
          subtot1=20000*banyak_pesanan1
        elif paketB==True:
          print("Jenis Paket = ",jenis_paket2,"\nBanyak pesanan",banyak_pesanan2,)
          subtot2=30000*banyak_pesanan2
        elif paketC==True:
          print("Jenis Paket = ",jenis_paket3,"\nBanyak pesanan",banyak_pesanan3,)
          subtot3=55000*banyak_pesanan3
        elif paketD==True:
          print("Jenis Paket = ",jenis_paket4,"\nBanyak pesanan",banyak_pesanan4,)
          subtot4=105000*banyak_pesanan4
        elif paketE==True:
          print("Jenis Paket = ",jenis_paket5,"\nBanyak pesanan",banyak_pesanan5,)
          subtot5=270000*banyak_pesanan5
        harga_total=subtot1+subtot2+subtot3+subtot4+subtot5
        print("harga Total : Rp",harga_total)
        