from mysql import connector
connect = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="praktikum_alpro_sabtu"
)

# buat  kursor
cursor = connect.cursor()

# buat table
cursor.execute(
    """
    CREATE TABLE mahasiswa ()
    """
)