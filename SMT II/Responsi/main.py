# Michael Valensio One Febian   (5220411200)
# Hezran Arkee Malaiga          (5220411215)
# Muhammad Rossi Pratama        (5220411211)
# Nadhif Atha Satria Wibowo     (5220411186)

# Package random digunakkan untuk meng-generate angka random di rentang tertentu.
# Package time dan threading digunakkan untuk melakukan countdown saat user menginputkan jawaban.
# Package os untuk merapikan terminal dan membuat lebih interaktif.
# Package pyfiglet digunakan untuk membuat teks ASCII art.


import random
import time
import threading
import os
import pyfiglet
 

# function untuk menampilkan pertanyaan berdasarkan skor dan level
def soalPertanyaan(skor, level):
    print("=" * 63)
    ascii_art = pyfiglet.figlet_format(" MATH GAMES!")
    print(ascii_art)
    print("=" * 63)
    if skor <= 10:
        level = 1
        print("Pertanyaan Level 1")
        angka1 = random.randint(-100, 100)
        angka2 = random.randint(-100, 100)
        operasi = random.choice(['+', '-'])
        pertanyaan = f"Berapa hasil dari {angka1} {operasi} {angka2}? "
        jawaban = eval(str(angka1) + operasi + str(angka2))
    elif skor >= 11 and skor <= 20:
        level = 2
        print("Pertanyaan Level 2")
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        pertanyaan = f"Berapa hasil dari {angka1} * {angka2}? "
        jawaban = angka1 * angka2
    elif skor >= 21 and skor <= 30:
        level = 3
        print("Pertanyaan Level 3")
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 5)
        pertanyaan = f"Berapa hasil dari {angka1} / {angka2}? (dibulatkan menjadi 2 tempat desimal) "
        jawaban = round(angka1 / angka2, 2)
    elif skor >= 31:
        level = 4
        print("Pertanyaan Level 4")
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        pertanyaan = f"Berapa hasil dari {angka1} % {angka2}? "
        jawaban = angka1 % angka2

    return pertanyaan, jawaban, level

# untuk menanyakan user ingin bermain lagi atau tidak
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
    print("1) Anda akan diberi pertanyaan matematika.")
    print("2) Untuk setiap jawaban benar maka skor akan bertambah 2,")
    print("   dan berkurang 2 jika jawaban salah atau waktu habis")
    print("3) Anda memiliki 3 nyawa. Setiap jawaban yang salah atau waktu habis, maka nyawa akan berkurang satu.")
    print("4) Anda hanya diberi waktu 10 detik sebelum waktu habis")
    print("   Dan jawaban anda dianggap salah (walaupun jawaban yang anda inputkan benar). ")

# untuk melakukan countdown selagi user menginputkan jaawaban
def countdown():
    for i in range(10, 0, -1):
        pass

# main program
def play():
    level = 0
    skor = 0
    nyawa = 3
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
            skor -= 2
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
            skor += 2
            print("Benar!")
            input("Press [ENTER] To Continue...")
            os.system("cls")
        else:
            nyawa -= 1
            skor -= 2
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
