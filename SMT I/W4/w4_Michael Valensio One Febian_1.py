# Nama : Michael Valensio One Febian
# NIM : 5220411200

nama=str(input("Siapa Namamu :"))
nilai1=int(input("Masukkan Nilai Alpro Teori Mu :"))
nilai2=int(input("Masukkan Nilai Alpro Praktek Mu :"))
if((nilai1<0) or (nilai2>100) or (nilai1<0) or (nilai2>100)):
     print("Nilai yang anda masukkan tidak valid")
else:
     if ((nilai1>=75) and (nilai2>=70)):
          print("Nama Mahasiswa :",nama)
          print("Nilai Teori :",nilai1)
          print("Nilai Praktek :",nilai2)
          print("Selamat," ,nama, "Anda lulus Alpro semester ini")
          print("Tetap Rendah hati dan jangan sombong")
     else:
          print("Maaf," ,nama,"Anda harus ikut Remidi Alpro")
          print("Terus tingkatkan semangat belajar mu!")
#after if
print("Terimakasih") 

