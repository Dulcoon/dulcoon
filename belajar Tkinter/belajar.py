import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()

window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Aplikasi Sederhana")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# frame input
input_frame = ttk.Frame(window)
# grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)


# komponen-komponen
# 1. Label untuk nama depan
namaDepanLabel = ttk.Label(input_frame,text="Nama Depan :")
namaDepanLabel.pack(padx=10,fill="x",expand=True)
# 2. Entry untuk nama depan
namaDepanEntry = ttk.Entry(input_frame, textvariable = NAMA_DEPAN)
namaDepanEntry.pack(padx=10,fill="x",expand=True)
# 3. Label untuk nama belakang
namaBelakangLabel = ttk.Label(input_frame,text="Nama Belakang :")
namaBelakangLabel.pack(padx=10,fill="x",expand=True)
# 4. Entry untuk nama belakang
namaBelakangEntry = ttk.Entry(input_frame, textvariable = NAMA_BELAKANG)
namaBelakangEntry.pack(padx=10,fill="x",expand=True)
# 5. Tombol 

def tombolClick():
    var1 = NAMA_DEPAN.get()
    var2 = NAMA_BELAKANG.get()
    pesan = "Halooo",var1,var2,"Selamat Aplikasi Sederhana mu Udah jadi"
    showinfo(title="Output",message=pesan)

tombolSapa = ttk.Button(input_frame, text="Sapa",command=tombolClick)
tombolSapa.pack(fill="x",expand=True,padx=10,pady=10)


window.mainloop()