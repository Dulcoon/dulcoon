# stack = ["dion", "hezran", "melky"]
# stack.append("Theo")
# stack.append("Valen")
# stack.pop()
# res = str(stack)[1:-1]
# print("Stack awal :{}".format(res))

from collections import deque

# queue = deque(["dion", "hezran", "melky"])
# print("Data Sebelum ditambahkan : ",queue)

# queue.append("Melky")
# queue.append("Valen")
# print("queue setelah ditambahkan : ",queue)
# queue.popleft()
# print("queue setelah dihapus : ",queue)

import os
stack = [1, 2, 3, 4, 5 ]
list_nama = ['melky', 'hezran', 'dion', 'theo', 'tama']

def tampilDgForstack():
    for i in stack:
        print(i)

def tampilDgForListNama():
    for j in list_nama:
        print(j)

def tampilIndex():
    print("tampil list yang mana?\n 1. stack \n 2. listNama")
    # ulang=True
    while True:
        try:
            pl = int(input("masukkan pilihan : "))
            if pl > 2 :
                print("Maaf system tidak memahami input anda")
                continue
        except ValueError:
            print("Maaf system tidak memahami input anda")
            continue
        else:
            break
        # stack
    if pl == 1:
        bnykData = len(stack)
        batas = bnykData - 1
        while True:
            try :
                ik = int(input("index ke berapa yang ingin ditampilkan? "))
                if ik > batas or ik < 0 :
                    print("index yang dimasukkan diluar jangkauan data!")
                    continue
            except ValueError:
                print("Maaf kami tidak memahami input anda")
                continue
            else:
                print("Isi stack indeks ke-",ik, "adalah: {}".format(stack[ik]))
                while True:
                        il = str(input("Ingin cari data lagi ? <yes/no> "))
                        if il.lower() == 'yes':
                            tampilIndex()
                        elif il.lower() == 'no':
                            os.system("cls")
                            menu()
                        else:
                            print("we dont understand")
    elif pl == 2:
        bnykData = len(list_nama)
        batas = bnykData - 1
        while True:
            try :
                ik = int(input("index ke berapa yang ingin ditampilkan? "))
                if ik > batas or ik < 0 :
                    print("index yang dimasukkan diluar jangkauan data!")
                    continue
            except ValueError:
                print("Maaf kami tidak memahami input anda")
                continue
            else:
                print("Isi stack indeks ke-",ik, "adalah: {}".format(stack[ik]))
                while True:
                        il = str(input("Ingin cari data lagi ? <yes/no> "))
                        if il.lower() == 'yes':
                            tampilIndex()
                        elif il.lower() == 'no':
                            os.system("cls")
                            menu()
                        else:
                            print("we dont understand")
def tampilIndexAsampaiB():
    print("tampil list yang mana?\n 1. stack \n 2. listNama")
    # ulang=True
    while True:
        try:
            pl = int(input("masukkan pilihan : "))
            if pl > 2 :
                print("Maaf system tidak memahami input anda")
                continue
        except ValueError:
            print("Maaf system tidak memahami input anda")
            continue
        else:
            break
        # stack
    if pl == 1:
        bnykData = len(stack)
        while True:
            try :
                batasAwal = int(input("Masukkan batas awal : "))
                batasAkhir = int(input("Masukkan batas akhir : "))
                # ik = int(input("index ke berapa yang ingin ditampilkan? "))
                if batasAwal < 0 :
                    print("index yang dimasukkan diluar jangkauan data!")
                    continue
                elif batasAkhir > bnykData :
                    print("index yang dimasukkan diluar jangkauan data!")
                    continue
            except ValueError:
                print("Maaf kami tidak memahami input anda")
                continue
            else:
                batasAwal -= 1
                # print("Isi stack indeks ke-",ik, "adalah: {}".format(stack[ik]))
                print("Menampilkan data 'List 2' dari data ke",batasAwal+1,"sampai data ke",batasAkhir,)
                print(stack[batasAwal:batasAkhir])
                while True:
                        il = str(input("Ingin cari data lagi ? <yes/no> "))
                        if il.lower() == 'yes':
                            tampilIndexAsampaiB()
                        elif il.lower() == 'no':
                            os.system("cls")
                            menu()
                        else:
                            print("we dont understand")
    elif pl == 2:
        bnykData = len(list_nama)
        # bnykData = len(stack)
        while True:
            try :
                batasAwal = int(input("Masukkan batas awal : "))
                batasAkhir = int(input("Masukkan batas akhir : "))
                # ik = int(input("index ke berapa yang ingin ditampilkan? "))
                if batasAwal < 0 :
                    print("index yang dimasukkan diluar jangkauan data!")
                    continue
                elif batasAkhir > bnykData :
                    print("index yang dimasukkan diluar jangkauan data!")
                    continue
            except ValueError:
                print("Maaf kami tidak memahami input anda")
                continue
            else:
                batasAwal -= 1
                # print("Isi stack indeks ke-",ik, "adalah: {}".format(stack[ik]))
                print("Menampilkan data 'List 2' dari data ke",batasAwal+1,"sampai data ke",batasAkhir,)
                print(list_nama[batasAwal:batasAkhir])
                while True:
                        il = str(input("Ingin cari data lagi ? <yes/no> "))
                        if il.lower() == 'yes':
                            tampilIndexAsampaiB()
                        elif il.lower() == 'no':
                            os.system("cls")
                            menu()
                        else:
                            print("we dont understand")

def updateData():
    print("tampil list yang mana?\n 1. stack \n 2. listNama")
    # ulang=True
    while True:
        try:
            pl = int(input("masukkan pilihan : "))
            if pl > 2 :
                print("Maaf system tidak memahami input anda")
                continue
        except ValueError:
            print("Maaf system tidak memahami input anda")
            continue
        else:
            break
        # stack
    if pl == 1:
        bnykData = len(stack)
        while True:
            try :
                dataUbh = int(input("Masukkan index data yang ingin diubah : (dimulai dari 0) "))
                newData = input("masukkan data yang baru : ")
                if dataUbh < 0 or dataUbh >= bnykData  :
                    print("index yang dimasukkan diluar jangkauan data!")
                    continue
            except ValueError:
                print("Maaf kami tidak memahami input anda")
                continue
            else:
                stack[dataUbh]=newData
                print("data ke ",dataUbh,"berhasil diupdate")
                print("Berikut merupakan update data terbaru :\n",stack)
                while True:
                        il = str(input("Ingin update data lagi ? <yes/no> "))
                        if il.lower() == 'yes':
                            updateData()
                        elif il.lower() == 'no':
                            os.system("cls")
                            menu()
                        else:
                            print("we dont understand")
    elif pl == 2:
        bnykData = len(list_nama)
        while True:
            try :
                dataUbh = int(input("Masukkan index data yang ingin diubah : (dimulai dari 0) "))
                newData = input("masukkan data yang baru : ")
                if dataUbh < 0 or dataUbh >= bnykData  :
                    print("index yang dimasukkan diluar jangkauan data!")
                    continue
            except ValueError:
                print("Maaf kami tidak memahami input anda")
                continue
            else:
                stack[dataUbh]=newData
                print("data ke ",dataUbh,"berhasil diupdate")
                print("Berikut merupakan update data terbaru :\n",stack)
                while True:
                        il = str(input("Ingin update data lagi ? <yes/no> "))
                        if il.lower() == 'yes':
                            updateData()
                        elif il.lower() == 'no':
                            os.system("cls")
                            menu()
                        else:
                            print("we dont understand")
def tambahData():
    while True:
        try:
            db = int(input("Masukkan Data yang baru : "))
            stack.append(db)
        except ValueError:
            print("we don't understand")
            continue
        else:
            print("Data setelah ditambah kan : \n",stack)
            while True:
                    il = str(input("Ingin tambah data lagi ? <yes/no> "))
                    if il.lower() == 'yes':
                        tambahData()
                    elif il.lower() == 'no':
                        os.system("cls")
                        menu()
                    else:
                        print("we dont understand")

def hapusData():
    while True:
        try:
            print(stack)
            db = int(input("Masukkan index Data yang ingin dihapus : "))
            stack.append(db)
        except ValueError:
            print("we don't understand")
            continue
        else:
            print("Data setelah ditambah kan : \n",stack)
            while True:
                    il = str(input("Ingin tambah data lagi ? <yes/no> "))
                    if il.lower() == 'yes':
                        tambahData()
                    elif il.lower() == 'no':
                        os.system("cls")
                        menu()
                    else:
                        print("we dont understand")


def menu():            
    while True:
        print("Menuu ngasal")
        print("1. Tampilkan List 2")
        print("2. Tampilkan List Nama")
        print("3. Tampilkan Data Berdasarkan Index tertentu")
        print("4. Tampilkan Data Berdasarkan Index a sampai index b")
        print("5. Update Data")
        print("6. Tambah Data")
        print("7. Keluar")
        x = input("Masukkan Menu : ")
        if x == "1":
            tampilDgForstack()
            os.system("pause")
            os.system("cls")
        elif x == "2":
            tampilDgForListNama()
            os.system("pause")
            os.system("cls")
        elif x == '3':
            tampilIndex()
        elif x == '4':
            tampilIndexAsampaiB()
        elif x == '5':
            updateData()
        elif x == '6':
            tambahData()
        elif x == '7':
            os.system("cls")
            exit()

if __name__ == "__main__":
  while(True):
    menu()

