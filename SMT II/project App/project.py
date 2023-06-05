import tkinter as tk

window = tk.Tk()
window.title("Aplikasi Sederhana")

label = tk.Label(text="Selamat datang di Aplikasi Sederhana!")
label.pack()

button = tk.Button(text="Klik Saya!")
button.pack()

window.mainloop()