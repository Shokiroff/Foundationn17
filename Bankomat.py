import os
os.system("cls")
class parol:
    def __init__(self):
        self.__eskiparol="1234"
        self.__new_pin=None
    def tekshir(self):
        pin=input("Pinni kiriting: ")
        if self.__eskiparol==pin:
            return True
        else:
            return False
    def convert(self):
        self.__new_pin=input("Yangi parolni kiriting: ")
        if self.__new_pin.isdigit() and len(self.__new_pin)>=4:
            yana=input("Parolini qaytadan kiriting: ")
            if self.__new_pin==yana:
                print("Muaffaqiyatli o'zlashtirildi!")
        else:
            print("Pin kod 4ta raqamdan iborat bo'lsin")
class NaqdPul(parol):
    def __init__(self, balans):
        super().__init__()
        self.miqdor=None
        self.balans=balans
    def hisob(self):
        if self.tekshir()==True:
            print(self.balans)
    def naqt(self):
        if self.tekshir()==True:
            self.miqdor=int(input("Qancha miqdordagi pulni naqdlashtirmoqchisiz: "))
        if self.balans>=self.miqdor:
            print(f"Marhamat {self.miqdor} so'm pulni oling ")
            yangi = self.balans - self.miqdor
            self.balans = yangi
            return yangi
        else:
            print("Hisobingizda yetarli mablag' mavjud emas.")

            
bank=parol()
naqd=NaqdPul(200000)
bank.tekshir()
print("Assalomu alaykum bizning bankomatimizga xush kelibsiz. Iltimos menyulardan birini tanlang: ")
print("\n 1.Pin kodni o'zgartirish\n 2.Balans\n 3.Naqt pul yechish\n")
ol=int(input("Tanlovni(1,2,3) ko'rinishida kiriting: "))
match ol:
    case 1:
        bank.convert()
    case 2:
        naqd.hisob()
    case 3:
       naqd.naqt() 
    case _ :
        print("Uzur bizda bunday amal mavjud emas")
        
    