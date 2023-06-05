import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

cursor = database.cursor()
a = str(input("Masukkan Nama Databasae yang ingin anda buat : "))
cursor.execute("CREATE DATABASE %s"%a)
print("Database telah dibuat!")

cursor.execute("SHOW DATABASES;")

for db in cursor:
    print(db[0])

cursor.close()
database.close()





# def update_data(db):
#   cursor = db.cursor()
#   show_data(db)
#   customer_id = input("pilih id customer> ")
#   name = input("Nama baru: ")
#   address = input("Alamat baru: ")

#   sql = "UPDATE tb_transaksi SET name=%s, address=%s WHERE customer_id=%s"
#   val = (name, address, customer_id)
#   cursor.execute(sql, val)
#   db.commit()
#   print("{} data berhasil diubah".format(cursor.rowcount))


# def delete_data(db):
#   cursor = db.cursor()
#   show_data(db)
#   customer_id = input("pilih id customer> ")
#   sql = "DELETE FROM tb_transaksi WHERE customer_id=%s"
#   val = (customer_id,)
#   cursor.execute(sql, val)
#   db.commit()
#   print("{} data berhasil dihapus".format(cursor.rowcount))
#  