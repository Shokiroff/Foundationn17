import os
import mysql.connector
os.system("cls")
class Baza:
    def __init__(self):
        self.data=mysql.connector.connect(user='root',password='root',host='localhost')
        self.cur=self.data.cursor()
        self.cur.execute("CREATE DATABASE IF NOT EXISTS meva;")
        self.data.commit()
        self.data=mysql.connector.connect(user='root',password='root',host='localhost',
                                        database='meva')

    def create_table(self,name_table):
        kur=self.data.cursor()
        kur.execute(f"""Create table if not exists {name_table}
                    (id int primary key auto_increment,nomi text,narxi int,navi varchar(50))""")
        self.data.commit()                                        

    def input_data(self,count,name_table):
        kur=self.data.cursor()
        sql=f"""INSERT INTO {name_table}(nomi ,narxi, navi) Values (%s, %s, %s)"""
        for x in range(count):
            nomi=input("\n Nomi: ")
            narxi=int(input("Narxi: "))
            navi=(input("Turi: "))
            kur.execute(sql,(nomi,narxi,navi))
            self.data.commit()
    

    def show_talaba(self,name_table):
        kur=self.data.cursor()
        kur.execute(f"Select * from {name_table}")
        result=kur.fetchall()
        for x in result:
            for y in x:
                print(y,end="\t")
            print("\n")

    def surov1(self,name_table,a,b):
        kur=self.data.cursor()
        kur.execute(f"SELECT * from {name_table} where narxi >= {a} and narxi <= {b} ")
        natija=kur.fetchall()
        for i in natija:
            print(i)
    
    


baz=Baza()
# baz.create_table("meva")
baz.surov1("meva",10000,20000)
# baz.input_data(10,"meva")
# baz.show_talaba("meva")



# class Baza:
#     def __init__(self):
#         self.data=mysql.connector.connect(user='root',password='root',host='localhost')
#         self.cur=self.data.cursor()
#         self.cur.execute("CREATE DATABASE IF NOT EXISTS meva;")
#         self.data.commit()
#         self.data=mysql.connector.connect(user='root',password='root',host='localhost',
#                                         database='bozor')

#     def create_table(self,name_table):
#         kur=self.data.cursor()
#         kur.execute(f"""Create table if not exists {name_table}
#                     (id int primary key auto_increment,meva_nomi text,meva_narxi int,meva_turi varchar(50))""")
#         self.data.commit()                                        

#     def input_data(self,count,name_table):
#         kur=self.data.cursor()
#         sql=f"""INSERT INTO {name_table}(meva_nomi ,meva_narxi, meva_turi) Values (%s, %s, %s)"""
#         for x in range(count):
#             nomi=input("\n Nomi: ")
#             narxi=int(input("Narxi: "))
#             navi=(input("Turi: "))
#             kur.execute(sql,(nomi,narxi,navi))
#             self.data.commit()
    

#     def show_talaba(self,name_table):
#         kur=self.data.cursor()
#         kur.execute(f"Select * from {name_table}")
#         result=kur.fetchall()
#         for x in result:
#             for y in x:
#                 print(y,end="\t")
#             print("\n")

#     # def surov1(self,name_table,a,b):
#     #     kur=self.data.cursor()
#     #     kur.execute(f"SELECT * from {name_table} where narxi >= {a} and narxi <= {b} ")
#     #     natija=kur.fetchall()
#     #     for i in natija:
#     #         print(i)


# baz=Baza()
# baz.create_table("meva")
# # baz.surov1("meva",10000,20000)
# baz.input_data(2,"meva")
# baz.show_talaba("meva")



