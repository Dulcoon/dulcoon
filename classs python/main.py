# class
class mahasiswa():
    # ini atrribut


    # init
    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim


    #method
    def belajar(self, kondisi):
        print(self.nama,"Sedang Belajar",kondisi)

    def tidur(self, kondisi):
        print(self.nama,"tidur di kelas",kondisi)



# main program
otong = mahasiswa("Otong Surotong", 5220411200)

print(f"Nama Mahasiswa : {otong.nama}\nNIM : {otong.nim}")
otong.belajar("dengan malas")
# ucup.nama = "Michael Ucup"


# otong.belajar("dengan giat")
# ucup.tidur("dengan nyenyak")