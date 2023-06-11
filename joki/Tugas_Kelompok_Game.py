# Melky sinun Usen (Ketua)       (5220411190)
# Theodorus Richard Dakhi        (5220411195)
# Dionisius Lexy Putra Winanta   (5220411194)
# M.Syam Soerya Pratama          (5190411594)

import random
import os
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def input_data_diri():
    nama = input("Masukkan Nama: ")
    tahun_lahir = int(input("Masukkan Tahun Lahir: "))
    if is_leap_year(tahun_lahir):
        print("Tahun {} merupakan TAHUN KABISAT".format(tahun_lahir))
    else:
        print("Tahun {} bukan merupakan TAHUN KABISAT".format(tahun_lahir))
    return nama

def game_penjumlahan():
    score = 0
    lives = 3

    while lives > 0:
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        hasil = x + y

        print("Hasil dari {} + {} adalah: ".format(x, y), end="")
        jawaban = int(input())

        if jawaban == hasil:
            score += 2
            print("Hore... benar!!! Skor Anda {} (lives: {})".format(score, lives))
        else:
            score -= 2
            lives -= 1
            print("Wah... salah!!! Skor Anda {} (lives: {})".format(score, lives))

    print("(GAME OVER)")

def game_pengurangan():
    score = 0
    lives = 3

    while lives > 0:
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        hasil = x - y

        print("Hasil dari {} - {} adalah: ".format(x, y), end="")
        jawaban = int(input())

        if jawaban == hasil:
            score += 2
            print("Hore... benar!!! Skor Anda {} (lives: {})".format(score, lives))
        else:
            score -= 2
            lives -= 1
            print("Wah... salah!!! Skor Anda {} (lives: {})".format(score, lives))

    print("(GAME OVER)")

def game_perkalian():
    score = 0
    lives = 3

    while lives > 0:
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        hasil = x * y

        print("Hasil dari {} * {} adalah: ".format(x, y), end="")
        jawaban = int(input())

        if jawaban == hasil:
            score += 2
            print("Hore... benar!!! Skor Anda {} (lives: {})".format(score, lives))
        else:
            score -= 2
            lives -= 1
            print("Wah... salah!!! Skor Anda {} (lives: {})".format(score, lives))

    print("(GAME OVER)")

def game_pembagian():
    score = 0
    lives = 3

    while lives > 0:
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        hasil = x / y

        print("Hasil dari {} / {} adalah: ".format(x, y), end="")
        jawaban = int(input())

        if jawaban == hasil:
            score += 2
            print("Hore... benar!!! Skor Anda {} (lives: {})".format(score, lives))
        else:
            score -= 2
            lives -= 1
            print("Wah... salah!!! Skor Anda {} (lives: {})".format(score, lives))

    print("(GAME OVER)")

def game_modulus():
    score = 0
    lives = 3

    while lives > 0:
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        hasil = x % y

        print("Hasil dari {} % {} adalah: ".format(x, y), end="")
        jawaban = int(input())

        if jawaban == hasil:
            score += 2
            print("Hore... benar!!! Skor Anda {} (lives: {})".format(score, lives))
        else:
            score -= 2
            lives -= 1
            print("Wah... salah!!! Skor Anda {} (lives: {})".format(score, lives))

    print("(GAME OVER)")


def main():
    nama = input_data_diri()

    while True:
        print("\nMenu pilihan level:")
        print("1. Level 1 (Penjumlahan)")
        print("2. Level 2 (Pengurangan)")
        print("3. Level 3 (Perkalian)")
        print("4. Level 4 (Pembagian)")
        print("5. Level 5 (Modulus)")
        print("6. Exit")

        pilihan = int(input("Pilih nomor pilihan: "))

        if pilihan == 1:
            game_penjumlahan()
            os.system("pause")
            os.system("cls")
        elif pilihan == 2:
            game_pengurangan()
            os.system("pause")
            os.system("cls")
        elif pilihan == 3:
            game_perkalian()
            os.system("pause")
            os.system("cls")
        elif pilihan == 4:
            game_pembagian()
            os.system("pause")
            os.system("cls")
        elif pilihan == 5:
            game_modulus()
            os.system("pause")
            os.system("cls")
        elif pilihan == 6:
            print("Terima kasih telah bermain!")
            break
        else:
            print("Maaf pilihan Anda salah")
            break
        

        lanjut = input("Apakah Anda ingin melanjutkan game? (y/n): ")
        if lanjut.lower() == 'y':
            continue
        else:
            print("Bacot yatim")
            break


if __name__ == '__main__':
    main()
