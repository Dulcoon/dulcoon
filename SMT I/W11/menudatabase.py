from mysql import connector
connect = connector.connect(
    host="localhost",
    user="root",
    password="",
)

connect = connector.connect(
host="localhost",
user="root",
password="",
database="praktikum_alpro_sabtu"
)

# cursor=connect.cursor()
# sql ="""CREATE TABLE mahasiswaa (
#     nim VARCHAR(15), 
#     nama VARCHAR(50), 
#     umur INT(5), 
#     kelas VARCHAR(50)
#     )
#     """


# cursor.execute(sql)

print("Tabel berhasil dibuat")

def insert(connect):
    nim = input("\nMasukkan NIM :")
    nama = input("\nMasukkan nama :")
    umur = input("\nMasukkan umur :")
    kelas = input("\nMasukkan kelas :")
    val = (nim,nama,umur,kelas)
    cursor=connect.cursor()
    sql="INSERT INTO mahasiswa (nim, nama, umur, kelas) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    connect.commit()
    print("\n{} Data berhasil disimpan".format(cursor.rowcount))

def tampilkan_data(connect):
    print("\n")
    cursor=connect.cursor()
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0 :
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

def ubah_data():
    cursor=connect.cursor()
    tampilkan_data(connect)
    


while True:
    print("1. masukkan data ")
    print("2. tampilkan data")
    print("3. ubah data")
    print("4. hapus data")
    print("0. Keluar  ")
    menu = int(input("Masukkan Menu : "))
    if(menu>4) or (menu<0):
        print("Menu yang anda pilih salah, perhatikan menu yang tersedia, silahkan run ulang!")
        break
    elif menu == 1:
        insert(connect)
    elif menu == 2:
        tampilkan_data(connect)
        
    
os.system("pause")
        
        
                
                                