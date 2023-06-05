# # Nama : Michael Valensio One Febian
# NIM : 5220411200

Nama=str(input("Masukkan Nama Anda :"))
pendapatan=float(input("Masukkan jumlah pendapatan Rp :"))
pengeluaran=float(input("Masukkan jumlah pengeluaran Rp :"))
if (pendapatan>pengeluaran):
    profit=pendapatan-pengeluaran
    print("Keuntungan yang didapatkan sebesar Rp" ,profit)
elif(pengeluaran>pendapatan):
     lost=pengeluaran-pendapatan
     print("Kerugian yang didapatkan sebesar Rp" ,lost)
elif(pendapatan==pengeluaran):
     print("Anda tidak untung dan tidak rugi")
     print("Terimakasih")
     