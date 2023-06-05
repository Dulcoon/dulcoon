import random
import time
import threading
import os
import pyfiglet

def soalPertanyaan(level):
    if level == 1:
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        operasi = random.choice(['+', '-'])
        pertanyaan = f"Berapa hasil dari {angka1} {operasi} {angka2}? "
        jawaban = eval(str(angka1) + operasi + str(angka2))
    elif level == 2:
        angka1 = random.randint(1, 5)
        angka2 = random.randint(1, 5)
        pertanyaan = f"Berapa hasil dari {angka1} * {angka2}? "
        jawaban = angka1 * angka2
    elif level == 3:
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 5)
        pertanyaan = f"Berapa hasil dari {angka1} / {angka2}? (dibulatkan menjadi 2 tempat desimal) "
        jawaban = round(angka1 / angka2, 2)
    else:
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        pertanyaan = f"Berapa hasil dari {angka1} % {angka2}? "
        jawaban = angka1 % angka2

    return pertanyaan, jawaban

def play_again():
    choice = input("Do you want to play again? (yes/no) ").lower()
    return choice == "yes"

def game_over():
    print("Game over!")

import sys




def print_welcome_screen():
    print("=" * 63)
    print(" "*23, "Welcome to")
    print("=" * 63)
    ascii_art = pyfiglet.figlet_format("MATH GAMES!")
    print(ascii_art)
    print("=" * 63)
    print("Prepare yourself to dive into the world of math!")
    print("=" * 63)

def rule():
    # print("Welcome to the Math Game!")
    print("- Anda akan diberi pertanyaan matematika.")
    print("- Untuk setiap jawaban benar akan diberi 1 point.")
    print("- anda memiliki 5 nyawa. Setiap jawaban yang salah nyawa akan berkurang satu.")
    print("- Anda hanya diberi waktu 5 detik sebelum waktu habis")
    print("  Dan jawaban anda dianggap salah. ")

def main():
    level = 1
    skor = 0
    nyawa = 5


    print_welcome_screen()
    input("Press [ENTER] To Check the Rule...")
    rule()
    input("Are you Ready?... Press [ENTER]")
    os.system("cls")
    name = input("Masukkan Nama: ")
    birth_year = int(input("Masukkan Tahun Lahir: "))

    # pengecekan tahun kabisat
    if birth_year % 400 == 0:
        kabisatStatus = "tahun kabisat"
    elif birth_year % 100 == 0:
        kabisatStatus = "bukan tahun kabisat"
    elif birth_year % 4 == 0:
        kabisatStatus = "tahun kabisat"
    else:
        kabisatStatus = "bukan tahun kabisat"

    print(f"Tahun {birth_year} merupakan {kabisatStatus}")
    print("Let's start!")
    input("Tekan [ENTER] Saat Anda Sudah Siap Bermain....")
    os.system("cls")
    while nyawa > 0:
        print(f"\nLevel {level} | Score: {skor} | Lives: {nyawa}")
        pertanyaan, jawaban = soalPertanyaan(level)
        print(pertanyaan)

        jawaban_user = input("Jawaban Anda: ")

        try:
            jawaban_user = float(jawaban_user)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if t.is_alive():
            # Hitungan mundur masih berjalan, pengguna memberikan jawaban
            if jawaban_user == jawaban:
                skor += 1
                print("Benar!")
                input("Press [ENTER] To Continue...")
                os.system("cls")
            else:
                nyawa -= 1
                print("Jawaban Salah!")
                print(f"The Benar jawaban is {jawaban}.")
                print(f"You have {nyawa} nyawa left.")
                input("Press [ENTER] To Continue...")
                os.system("cls")
        else:
            # Waktu habis, dianggap jawaban salah
            nyawa -= 1
            print("Time's up! Wrong jawaban!")
            print(f"The Benar jawaban is {jawaban}.")
            print(f"You have {nyawa} nyawa left.")
            input("Press [ENTER] To Continue...")
            os.system("cls")

        if nyawa == 0:
            game_over()
            if play_again():
                level = 1
                skor = 0
                nyawa = 5
                print("Let's play again!")
            else:
                print("Thank you for playing. Goodbye!")

if __name__ == "__main__":
    main()
