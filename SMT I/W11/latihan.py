from mysql import connector
connect = connector.connect(
    host="localhost",
    user="root",
    password="",
)

# buat  kursor
cursor = connect.cursor()

# lakukan eksekusi query, dengan membuat database
cursor.execute("CREATE DATABASE praktikum_alpro_sabtu;")

# tampilkan database
cursor.execute("SHOW DATABASES;")

# lakukan iterasi dari hasil query
for db in cursor:
    print(db[0])

# tutup cursor dan tutup koneksi untuk membersihkan port
cursor.close()
connect.close()