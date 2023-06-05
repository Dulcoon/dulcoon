
import os

class Cookie():
    def __init__(self, color):
        self.color = color
        # self.size = size

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie("Green")
cookie_two = Cookie("Blue")

print("Cookie one colour is" ,cookie_one.get_color())
print("Cookie two colour is ",cookie_two.get_color())

while True:
    a = input("Do you want to change the color? <yes/no> ")
    if a.lower() == 'yes':
        b = int(input("which Cookie? (Cookie 1 or 2) >> "))
        if b == 1:
            print("Cookie 1 will be changed")
            color = input("Please input the color : ")
            cookie_one.set_color(color)
            print(f"The color has been changed to {color}")
            print(f"Cookie one is now {cookie_one.get_color()}")
        elif b == 2:
            print("Cookie 2 will be changed")
            color = input("Please input the color : ")
            cookie_two.set_color(color)
            print(f"The color has been changed to {color}")
            print(f"Cookie two is now {cookie_two.get_color()}")
    elif a.lower() == 'no':
        os.system("cls")
        exit()
    else:
        print("we dont understand")

# cookie_one.set_color("Yellow")
# print("The color has been changed !")




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
