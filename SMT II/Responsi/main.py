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

# def countdown_timer(seconds):
#     print("waktu")
#     for i in range(seconds, 0, -1):
#         sys.stdout.write(f"{i}\r")
#         # sys.stdout.flush()
#         time.sleep(1)


# def countdown(t):
#     real = t
#     while t > 0:
#         CURSOR_UP = '\033[F'
#         ERASE_LINE = '\033[K'
#         if t == real:
#             print(ERASE_LINE + 'Duration: {}s'.format(t), end='\r', flush=True)
#         else:
#             print(CURSOR_UP + ERASE_LINE + 'Duration: {}s'.format(t), end='\r', flush=True)
#         time.sleep(1)
#         t -= 1


def countdown(t):
    real = t
    while t > 0:
        CURSOR_UP = '\033[F'
        ERASE_LINE = '\033[K'
        if t == real:
            print(ERASE_LINE + 'Duration : {}s'.format(t))
        else:
            print(CURSOR_UP + ERASE_LINE + 'Duration : {}s'.format(t))
        time.sleep(1)
        t -= 1

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

        # Memulai hitungan mundur dalam thread terpisah
        t = threading.Thread(target=countdown, args=(5,))
        t.start()

        jawaban_user = input("Jawaban Anda: ")

        # Menghentikan hitungan mundur jika pengguna memberikan jawaban sebelum waktu habis
        t.join(timeout=0)

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
                # input("Press [ENTER] To Continue...")
                os.system("cls")
            else:
                nyawa -= 1
                print("Jawaban Salah!")
                print(f"The Benar jawaban is {jawaban}.")
                print(f"You have {nyawa} nyawa left.")
                # input("Press [ENTER] To Continue...")
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
