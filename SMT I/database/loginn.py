# from projectalproo import *
# import os
# from getpass import getpass

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="db_valen"
# )
# cursor = db.cursor()




# n = 1+1
# # def masuk(kasir):


# def masuk():

#     sql1 = "SELECT username FROM tb_user WHERE nama_kasir='Mbak Kasir 1'"
#     cursor.execute(sql1,)
#     nama1=cursor.fetchall()[0][0]

#     sql1 = "SELECT username FROM tb_user WHERE nama_kasir='Mbak Kasir 2'"
#     cursor.execute(sql1,)
#     nama2=cursor.fetchall()[0][0]

#     sql1 = "SELECT username FROM tb_user WHERE nama_kasir='Mbak Kasir 3'"
#     cursor.execute(sql1,)
#     nama3=cursor.fetchall()[0][0]

#     sql1 = "SELECT password FROM tb_user WHERE nama_kasir='Mbak Kasir 1'"
#     cursor.execute(sql1,)
#     pass1=cursor.fetchall()[0][0]

#     sql1 = "SELECT password FROM tb_user WHERE nama_kasir='Mbak Kasir 2'"
#     cursor.execute(sql1,)
#     pass2=cursor.fetchall()[0][0]

#     sql1 = "SELECT password FROM tb_user WHERE nama_kasir='Mbak Kasir 3'"
#     cursor.execute(sql1,)
#     global pass3
#     pass3=cursor.fetchall()[0][0]




#     print("="*70)
#     print("Silahkan Login Menggunakan Username Dan Password yang Valid")
#     print("="*70)
#     ulanggggg = True
#     while ulanggggg==True :
#         user = input("Masukkan Username : ")
#         passw = getpass("Masukkan Password : ")
#         if user == nama1 and passw == pass1:
#             global kasir
#             kasir = "Mbak Kasir 1"
#             print("anda berhasil login sebagai Mbak Kasir 1")
#             input("Press [ENTER} to continue")
#             # os.system("cls")
#             while (True):
#                 show_menu(db)
#                 ulanggggg=False
                
                
            

#         elif user == nama2 and passw == pass2:
#             global kasir
#             kasir = "Mbak Kasir 2"
#             print("anda berhasil login sebagai Mbak Kasir 2")
#             input("Press [ENTER} to continue")
#             # os.system("cls")
#             while (True):
#                 show_menu(db)
#                 ulanggggg=False
        
#         elif user == nama3 and passw == pass3:
#             global kasir
#             kasir = "Mbak Kasir 3"
#             print("anda berhasil login sebagai Mbak Kasir 3")
#             input("Press [ENTER} to continue")
#             # os.system("cls")
#             while (True):
#                 show_menu(db)
#                 ulanggggg=False


#         else:
#             print("Username atau password salah! \nlogin gagal")
#             input("Press [ENTER} to continue")
#             os.system("cls")
#             ulanggggg=True   

                
# if __name__=="__main__":
#     masuk()