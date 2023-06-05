import os
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
list_nama = ['melky', 'hezran', 'dion', 'theo', 'tama']

def tampilDgForList2():
    for i in list2:
        print(i)

def tampilDgForListNama():
    for j in list_nama:
        print(j)

def tampilIndex():
    print("tampil list yang mana?\n 1. list2 \n 2. listNama")
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
        # list2
    if pl == 1:
        bnykData = len(list2)
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
                print("Isi list2 indeks ke-",ik, "adalah: {}".format(list2[ik]))
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
                print("Isi list2 indeks ke-",ik, "adalah: {}".format(list2[ik]))
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
    print("tampil list yang mana?\n 1. list2 \n 2. listNama")
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
        # list2
    if pl == 1:
        bnykData = len(list2)
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
                # print("Isi list2 indeks ke-",ik, "adalah: {}".format(list2[ik]))
                print("Menampilkan data 'List 2' dari data ke",batasAwal+1,"sampai data ke",batasAkhir,)
                print(list2[batasAwal:batasAkhir])
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
        # bnykData = len(list2)
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
                # print("Isi list2 indeks ke-",ik, "adalah: {}".format(list2[ik]))
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
    print("tampil list yang mana?\n 1. list2 \n 2. listNama")
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
        # list2
    if pl == 1:
        bnykData = len(list2)
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
                list2[dataUbh]=newData
                print("data ke ",dataUbh,"berhasil diupdate")
                print("Berikut merupakan update data terbaru :\n",list2)
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
                list2[dataUbh]=newData
                print("data ke ",dataUbh,"berhasil diupdate")
                print("Berikut merupakan update data terbaru :\n",list2)
                while True:
                        il = str(input("Ingin update data lagi ? <yes/no> "))
                        if il.lower() == 'yes':
                            updateData()
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
        print("6. Keluar")
        x = input("Masukkan Menu : ")
        if x == "1":
            tampilDgForList2()
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
            os.system("cls")
            exit()

if __name__ == "__main__":
  while(True):
    menu()
