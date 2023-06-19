# print("====PROGRAM MENCARI KPK====")
# # mendefinisikan fungsi
# def hitung_kpk(x, y):
#     # mencari bilangan terbesar antara x dan y
#     if x > y:
#         terbesar = x
#     else:
#         terbesar = y
#     while True:
#         # mencari kelipatan dari bilangan terbesar
#         if (terbesar % x == 0) and (terbesar % y == 0):
#             kpk = terbesar
#             break
#         terbesar += 1
#     return kpk

# nilai1 = int(input("Masukkan bilangan pertama: "))
# nilai2 = int(input("Masukkan bilangan kedua: "))
# print("Hasil KPK= ", hitung_kpk(nilai1, nilai2))

# inisialisasi variabel
n = 5
sum = 0

# iterasi untuk menghitung jumlah
for i in range(1, n+1):
    sum += i

# mencetak hasil
print("Jumlah 5 bilangan pertama pada deret adalah:", sum)

