import MySQLdb 
def mysql_connection():
    return MySQLdb.connect(
        host="localhost",
        user="root",
        password="",
        database="db_alproplt"
    )

import matplotlib.pyplot as plt
def run():
    try:
        prodi = ["Matematika", "Statistika"]
        jumlah_mhs = [108, 134]

        plt.figure(figsize=(12,7))
        plt.bar(prodi, jumlah_mhs, color="lightcoral")

        plt.title("Jumlah Mahasiswa Per Program Studi", size=16)
        plt.ylabel("Jumlah Mahasiswa", size=14)
        plt.xticks(size=12)
        plt.yticks(size=12)

        plt.show()
        sql = "INSERT INTO tb_survei (prodi, jumlah_mhs) VALUES (%s, %s)"
        val = (prodi, jumlah_mhs)
        myConnection = mysql_connection()
        cursor = myConnection.cursor()
        cursor.execute(sql, val)
        print("data tersimpan")
        myConnection.commit()

    except Exception as e:
        print(e)
        print("data tidak tersimpan")


if __name__ == "__main__":
    run()