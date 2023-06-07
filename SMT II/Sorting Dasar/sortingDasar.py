import os
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range (i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def descend_bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] < my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def selection_sort(my_list):
    for i in range (len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def descend_selection_sort(my_list):
    for i in range(len(my_list) - 1):
        max_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] > my_list[max_index]:
                max_index = j
        if i != max_index:
            temp = my_list[i]
            my_list[i] = my_list[max_index]
            my_list[max_index] = temp
    return my_list


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (temp < my_list[j] and j > -1):
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

def descend_insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (temp > my_list[j] and j > -1):
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = temp
    return my_list

def menuu():
    while True:
        os.system("cls")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Keluar")
        menu = input("Pilih Menu (1-3) : ")
        if menu == "1":
            my_list = []
            while True:
                try:
                    data = int(input("Masukkan Data (Int Only) :"))
                except ValueError:
                    print("Data must be integer!")
                else:
                    my_list.append(data)
                    yk = input("Ingin memasukkan data lagi ? ")
                    if yk.lower() == "y":
                        continue
                    else:
                        while True:
                            os.system("cls")
                            print("1. Ascending")
                            print("2. Descending")
                            print("3. Kembali Ke Menu")
                            ipt = input(">> ")
                            if ipt == "1":        
                                print("Data Telah Berhasil Diurutkan")
                                print(bubble_sort(my_list))
                            elif ipt == "2":
                                print("Data Telah Berhasil Diurutkan")
                                print(descend_bubble_sort(my_list))
                            elif ipt == "3":
                                menuu()
                            else:
                                print("Menu salah!")
                                continue
                            os.system("pause")
        if menu == "2":
            my_list = []
            while True:
                try:
                    data = int(input("Masukkan Data (Int Only) :"))
                except ValueError:
                    print("Data must be integer!")
                else:
                    my_list.append(data)
                    yk = input("Ingin memasukkan data lagi ? ")
                    if yk.lower() == "y":
                        continue
                    else:
                        while True:
                            os.system("cls")
                            print("1. Ascending")
                            print("2. Descending")
                            print("3. Kembali Ke Menu")
                            ipt = input(">> ")
                            if ipt == "1":        
                                print("Data Telah Berhasil Diurutkan")
                                print(selection_sort(my_list))
                            elif ipt == "2":
                                print("Data Telah Berhasil Diurutkan")
                                print(descend_selection_sort(my_list))
                            elif ipt == "3":
                                menuu()
                            else:
                                print("Menu salah!")
                                continue
                            os.system("pause")
        if menu == "3":
            my_list = []
            while True:
                try:
                    data = int(input("Masukkan Data (Int Only) :"))
                except ValueError:
                    print("Data must be integer!")
                else:
                    my_list.append(data)
                    yk = input("Ingin memasukkan data lagi ? ")
                    if yk.lower() == "y":
                        continue
                    else:
                        while True:
                            os.system("cls")
                            print("1. Ascending")
                            print("2. Descending")
                            print("3. Kembali Ke Menu")
                            ipt = input(">> ")
                            if ipt == "1":        
                                print("Data Telah Berhasil Diurutkan")
                                print(insertion_sort(my_list))
                            elif ipt == "2":
                                print("Data Telah Berhasil Diurutkan")
                                print(descend_insertion_sort(my_list))
                            elif ipt == "3":
                                menuu()
                            else:
                                print("Menu salah!")
                                continue
                            os.system("pause")
        if menu == "4":
            print("Terimakasih")
            exit()
        else:
            print("Menu Salah!")
        os.system("pause")

if __name__=="__main__":
    menuu()