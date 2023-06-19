# # Suhu
# print("Menentukan Wujud Air Berdasarkan Suhu")
# t = int(input("Masukan suhu: "))

# if t<= 0:
#     print("Pada Suhu" , t , "Drajad Celcius, Air akan berwujud padat")
# elif t>0 and t<100:
#     print("Pada Suhu" , t , "Drajad Celcius, Air akan berwujud cair")
# else :
#     print("Pada Suhu" , t , "Drajad Celcius, Air akan berwujud uap")



# Code Program :
print("==========INPUT DATA==========")
nama = input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))
#1=Islam, 2=Protestan, 3=Katolik, 4=Hindu, 5=Budha
if(agama==1):
    agama = "Islam"
elif(agama==2):
    agama = "Protestan"
elif(agama==3):
    agama = "Katolik"
elif(agama==4):
    agama = "Hindu"
elif(agama==5):
    agama = "Budha"
else:
    agama = "Agama tidak ditemukan"
print("==========OUTPUT========")
print("Nama: ",nama)
print("Jenis Kelamin: ",jk)
print("Agama: ",agama)