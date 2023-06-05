from prettytable import from_db_cursor
import mysql.connector
from datetime import datetime
dt = datetime.now()
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_valen"
)
cursor = db.cursor()

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
    i = int(input("Ketik <1> untuk menghapus semua data dalam satu baris tabel \nKetik <2> untuk menghapus semua data"))
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
        sql = "DELETE FROM tb_transaksi WHERE id_transaksi, nama_barang, banyak_barang, harga_satuan, harga_total, timestamp"
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil diubah".format(cursor.rowcount))
# def cari_data(db):
#     cursor = db.cursor()

#     sql = "SELECT HOURS(timestamp) FROM tb_transaksi"
#     cursor.execute(sql)



# print(cari_data(db))
    
    
# def fungsi_tkinter():
#     cursor = db.cursor()
#     sql = "SELECT * FROM tb_transaksi"
#     cursor.execute(sql)


#     r = tk.Tk()
#     r.title("Riwayat Transaksi")
#     r.geometry("600x300")

#     # membuat tampilan rapi
#     tree = ttk.Treeview(r)
#     tree['show']='headings'

#     # tema tabel
#     s = ttk.Style(r)
#     s.theme_use("winnative")

#     # 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'

#     # pendefinisian kolom
#     tree["columns"]=("id_transaksi","nama_barang","banyak_barang","harga_satuan","harga_total","timestamp")

#     # pendefinisian lebar setiap kolom
#     tree.column("id_transaksi", width=100, minwidth=100, anchor=tk.CENTER)
#     tree.column("nama_barang", width=100, minwidth=100, anchor=tk.CENTER)
#     tree.column("banyak_barang", width=100, minwidth=100, anchor=tk.CENTER)
#     tree.column("harga_satuan", width=100, minwidth=100, anchor=tk.CENTER)
#     tree.column("harga_total", width=100, minwidth=100, anchor=tk.CENTER)
#     tree.column("timestamp", width=150, minwidth=150, anchor=tk.CENTER)

#     # bagian heading dari tabel
#     tree.heading("id_transaksi", text="Id Transaksi", anchor=tk.CENTER)
#     tree.heading("nama_barang", text="Nama Barang", anchor=tk.CENTER)
#     tree.heading("banyak_barang", text="Banyak Barang", anchor=tk.CENTER)
#     tree.heading("harga_satuan", text="Harga Satuan", anchor=tk.CENTER)
#     tree.heading("harga_total", text="Harga Total", anchor=tk.CENTER)
#     tree.heading("timestamp", text="Timestamp", anchor=tk.CENTER)

#     # syntax untuk menampilkan tabel
#     i = 0
#     for ro in cursor :
#         tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
#         i = i + 1

#     # membuat scroll bar dibawah tabel
#     hsb = ttk.Scrollbar(r,orient="horizontal")
#     hsb.configure(command=tree.xview)
#     tree.configure(xscrollcommand=hsb.set)
#     hsb.pack(fill=X,side=BOTTOM)

#     tree.pack()

#     r.mainloop()