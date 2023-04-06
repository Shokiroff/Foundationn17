import os 
os.system('cls')

class bankamat:
    __code=1111
    __urinish=3
    __balans=2000000
    def __init__(self,nm,bl):
        self.name=nm
        self.balans=bl
        self.naxt_pul=0
        
        print("Bizning bankdan foydalanganingiz uchun raxmat! ")
    def info(self):
        self.code=input("Pin kodni kiriting: ")
        if self.__code<5 or self.__code:
            print("Naqt pul olish uchun 1 ni bosng: ")
            print("Kartani toldirish uchun 2 ni bosing: ")
            print("Balansni tekshirish uchun 3 ni bosing:  ")

    def n_o(self):
        naxt_pul=int(input("Sizga kerakli pul miqdorini kiriting: "))
        if naxt_pul>=2000000:
            print("Sizni hisobda mablaq yetarliemas")
        else :
            print(f"Marhamat  {naxt_pul} ming sumni oling: ")
    def k_t(self):
        karta_tuldirish=int(input("Mablaqni kiriting: "))
        if karta_tuldirish>=100:
            print(f"Sizning hisobingiz {karta_tuldirish} ga tuldirildi: ")
        else:
            print("Siz yetarli pul kiritmadingiz: ")

    def b_l(self):
        print(f"Sizning hisibingizda {bankamat.__balans} sum bor: ")
    
    def porol(self):
        if bankamat.__urinish==0:
            print("Kartangiz bloklandi") 
        pin_code=int(input("Parolni almashtirish uchun oldingi parolni kiriting: "))
        bankamat.__urinish-=1
        if bankamat.__code==pin_code:
            self.__natija()
        else:
            print("Parol xato kiritildi qaytadan urinib kuring:")
    def __new_posword(self):
        y_p=input("Yangi parolni kiriting: ")
        y_p1=input("Yangi parolni qaytadan kiriting:")
        if y_p!=y_p1:
            print("Qayta terilgan parol mos emas! ")
            return "0"
        return y_p
    def __tekshirilgan_pasword(self):
        a=self.__new_posword()
        return a.isdigit()==a<4
    def __natija(self):
        if self.__tekshirilgan_pasword()==False:
            print("Parol muvaffaqiyatli o'zgartirildi:")
        else:
            print("Parolni uzgartirishda xatolik: ")

bn=bankamat("Ilxom",2000000)
bn.info()
bn.n_o()
bn.k_t()
bn.b_l()

 


