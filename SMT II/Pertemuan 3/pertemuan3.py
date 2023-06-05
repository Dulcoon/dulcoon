# # Michael Valensio One Febian
# # NIM 5220411200

# """
# LIST
# """
# # Mengambil dan melakukan output setiap item
# angka = [1,2,3,4,5,6,7,8,9]
# for item in angka:
#     print(item) 
    
# # mengahpus data pada list (dengan pop)
# print("Data baru")
# angka.pop(2)
# for item in angka:
#     print(item) 
    
# # mengahpus data pada list (dengan remove)
# print("Data baru")
# angka.remove(1)
# for item in angka:
#     print(item) 
    
    
# # mengganti nomor handphone india menjadi indonsia\
# no_hp = ["+108478347","+6228936728","+102973","+1083467834"]
# noHpIndo = []
# for i in range(len(no_hp)):
#     if no_hp[i].startswith("+10"):
#         no_hp[i] = "+62" + no_hp[i][3:]
# print(no_hp)

# # dengan replace
# for i in range(len(no_hp)):
#     if no_hp[i].startswith("+10"):
#        no_hp[i].replace("+10", "+62") 
       
# print("Versi ku",no_hp)

# # dengan list baru
# for item in no_hp:
#     if item.startswith("+10"):
#        noHpIndo.append(item.replace("+10", "+62"))
#     else:
#         noHpIndo.append(item)
# print(noHpIndo)

"""
1. menagmbil data yang ada di list
2. Melakukan kondisi dengan kriteria
3. 
"""


"""
DICTIONARY
"""

buku = {
    'Indonesia' : {
        "Judul" : "Laskar Pelangi",
        "Jumlah_halaman" : 90
    },
    "Amerika" : {
        "Judul" : "Harry Potter",
        "Jumlah_halaman" : 90
    }
}

# print(buku["Indonesia"]["Judul"])
# for key in buku:
#     print(f"{key} -> {buku[key]} halaman")

for negara, info_buku in buku.items():
    judul = info_buku['Judul']
    halaman = info_buku['Jumlah_halaman']
    print(f"{negara} -> {judul} dan punya {halaman} halaman")