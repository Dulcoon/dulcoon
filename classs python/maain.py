# mlist = [1,2,3]
# mlist.insert(1,"hi")
# print(mlist)

class Cookie():
    def __init__(self, color, panjang):
        self.color = color
        self.panjang = panjang

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_panjang(self):
        return self.panjang

    def set_panjang(self, panjang):
        self.panjang = panjang

cookie_one = Cookie("Green")
cookie_two = Cookie("Blue")

print("Cookie one colour is" ,cookie_one.get_color())
print("Cookie two colour is ",cookie_two.get_color())




# fungsional
def hitung(bil1, bil2):
    return bil1 + bil2

# prosedural
def hitungProsedural(bil1, bil2):
    print(bil1+bil2)
    
hitungProsedural(1,1)

# class Hero():
#     def __init__(self, inputName, inputHealth, inputArmor):
#         self.name = inputName
#         self.health = inputHealth
#         self.armor = inputArmor
#         # totalHealth = inputHealth + inputArmor
#         self.totalHealth = inputHealth + inputArmor
#         # return totalHealth
        
    
#     def kekuatan(power):
#         return power


# Hero1 = Hero("Satria Baja Besi",95,100)
# Hero1Power = Hero.kekuatan("Kebal Peluru Tembakan")

# Hero2 = Hero("Kura Kura Ninja",80,75)
# Hero2Power = Hero.kekuatan("Lambat tapi ampuh")

# print(f"Nama hero yang Pertama adalah {Hero1.name}\n-->Status\nHealth : {Hero1.health}\nArmor : {Hero1.armor}\nTotal Health : {Hero1.totalHealth}\nHero ini memiliki kekuatan yaitu {Hero1Power}\n"+"="*50)
# print(f"Nama hero yang Kedua adalah {Hero2.name}\n-->Status\nHealth : {Hero2.health}\nArmor : {Hero2.armor}\nHero ini memiliki kekuatan yaitu {Hero1Power}\n"+"="*50)
