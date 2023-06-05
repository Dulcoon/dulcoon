from mysql import connector

def create_db():
    connect = connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connect.cursor()

    cursor.execute("CREATE DATABASE praktikum_alpro_sabtu;")

    cursor.execute("SHOW DATABASES;")

    for db in cursor:
        print(db[0])

    cursor.close()
    connect.close()

def create_tb():
    connect = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="praktikum_alpro_sabtu"
    )

    cursor = connect.cursor()

    cursor.execute(
        """
        CREATE TABLE mahasiswa (nim VARCHAR(15), nama VARCHAR(50), umur INT(5), kelas VARCHAR(50));
        """
    )

    cursor.execute("SHOW TABLES;")

    print("Tabel di Database praktikum_alpro_sabtu : ")
    for tb in cursor:
        print(tb[0])

    cursor.close()
    connect.close()

def insert():
    connect = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="praktikum_alpro_sabtu"
    )

    cursor = connect.cursor()

    cursor.execute(
        """
        INSERT INTO mahasiswa VALUES('519021332','Dion','17','Alpro Praktik VI');
        """
    )

    connect.commit()

    cursor.execute("SELECT * FROM mahasiswa;")

    result = cursor.fetchall()

    for data in result:
        print(f"={data[0]} - {data[1]}\t - {data[2]} - {data[3]}")

    cursor.close()
    connect.close()

def update():

    connect = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="praktikum_alpro_sabtu"
    )

    cursor = connect.cursor()

    sql = "UPDATE mahasiswa SET nama = 'Canyon 123' WHERE nim = '519021332'"

    cursor.execute(sql)

    connect.commit()

    print(cursor.rowcount, "record(s) affected")

def delete():
    connect = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="praktikum_alpro_sabtu"
    )

    cursor = connect.cursor()

    sql = "DELETE FROM mahasiswa WHERE nama = 'Mountain 21'"

    cursor.execute(sql)

    connect.commit()

    print(cursor.rowcount, "record(s) deleted")

while True:
 print("\n")
 print("PROGRAM DATABASE")
 print("~~~~~~~~~~~~~~~~~~~~~~")
 print("1.Create Database")
 print("2.Create Table Database")
 print("3.Insert Database")
 print("4.Update Database")
 print("5.Delete Database")
 print("~~~~~~~~~~~~~~~~~~~~~~")
 b=input("\nPilih Menu : ")
 if (b=='1'):
    create_db()
 elif (b=='2'):
    create_tb()
 elif (b=='3'):
    insert()
 elif (b=='4'):
    update()
 elif (b=='5'):
    delete()
 else:
    print("Menu Salah")