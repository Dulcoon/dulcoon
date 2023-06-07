# Michael Valensio One Febian   (5220411200)
# Hezran Arkee Malaiga          (5220411215)
# Muhammad Rossi Pratama        (5220411211)
# Nadhif Atta                   (522041119x)


import random
import time
import threading
import os
import pyfiglet
 

def soalPertanyaan(skor, level):
    print("=" * 63)
    ascii_art = pyfiglet.figlet_format(" MATH GAMES!")
    print(ascii_art)
    print("=" * 63)
    if skor <= 5:
        level = 1
        print("Pertanyaan Level 1")
        angka1 = random.randint(1, 5)
        angka2 = random.randint(1, 10)
        operasi = random.choice(['+', '-'])
        pertanyaan = f"Berapa hasil dari {angka1} {operasi} {angka2}? "
        jawaban = eval(str(angka1) + operasi + str(angka2))
    elif skor >= 6 and skor <= 10:
        level = 2
        print("Pertanyaan Level 2")
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        pertanyaan = f"Berapa hasil dari {angka1} * {angka2}? "
        jawaban = angka1 * angka2
    elif skor >= 11 and skor <= 15:
        level = 3
        print("Pertanyaan Level 3")
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 5)
        pertanyaan = f"Berapa hasil dari {angka1} / {angka2}? (dibulatkan menjadi 2 tempat desimal) "
        jawaban = round(angka1 / angka2, 2)
    elif skor >= 16 and skor <= 20:
        level = 4
        print("Pertanyaan Level 4")
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        pertanyaan = f"Berapa hasil dari {angka1} % {angka2}? "
        jawaban = angka1 % angka2

    return pertanyaan, jawaban, level


def play_again():
    choice = input("Do you want to play again? (yes/no) ").lower()
    return choice == "yes"


def print_welcome_screen():
    green_color = "\033[92m"
    print(green_color + "=" * 63)
    print(" "*23, "Welcome to")
    print("=" * 63)
    ascii_art = pyfiglet.figlet_format(" MATH GAMES!")
    print(ascii_art)
    print("=" * 63)
    print("Prepare yourself to dive into the world of math!")
    print("=" * 63)

def rule():
    print("- Anda akan diberi pertanyaan matematika.")
    print("- Untuk setiap jawaban benar akan diberi 1 point.")
    print("- Anda memiliki 5 nyawa. Setiap jawaban yang salah nyawa akan berkurang satu.")
    print("- Anda hanya diberi waktu 10 detik sebelum waktu habis")
    print("  Dan jawaban anda dianggap salah. ")

def countdown():
    for i in range(10, 0, -1):
        pass

def play():
    level = 0
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
        pertanyaan, jawaban, level = soalPertanyaan(skor, level)
        print(f"\nLevel {level} | Score: {skor} | Lives: {nyawa}")
        print(pertanyaan)

        t = threading.Thread(target=countdown)
        t.start()

        start_time = time.time()
        jawaban_user = input("Jawaban Anda: ")
        elapsed_time = time.time() - start_time

        t.join()

        if elapsed_time > 10:
            nyawa -= 1
            print("Waktu habis! Jawaban dianggap salah.")
            print(f"Anda memiliki {nyawa} Nyawa Tersisa.")
            input("Press [ENTER] To Continue...")
            os.system("cls")
            continue
        try:
            jawaban_user = float(jawaban_user)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if jawaban_user == jawaban:
            skor += 1
            print("Benar!")
            input("Press [ENTER] To Continue...")
            os.system("cls")
        else:
            nyawa -= 1
            print("Jawaban Salah!")
            print(f"Jawaban Yang benar adalah {jawaban}.")
            print(f"Anda memiliki {nyawa} Nyawa Tersisa.")
            input("Press [ENTER] To Continue...")
            os.system("cls")

        if nyawa == 0 or nyawa < 0:
            ascii_art = pyfiglet.figlet_format(" GAME OVER!")
            print(ascii_art)
            print("="*25)
            print(f"Nama       : {name}")
            print(f"Skor Akhir : {skor}")
            print("="*25)
            if play_again():
                level = 1
                skor = 0
                nyawa = 5
                print("Let's play again!")
            else:
                print("Thank you for playing. Goodbye!")

if __name__ == "__main__":
    play()
