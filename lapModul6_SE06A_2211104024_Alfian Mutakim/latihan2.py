# Latihan perbandingan bilangan function
print('-------')
def bilangan1(bil1, bil2):
    if bil1 > bil2:
        print("bilangan yang lebih besar adalah ", bil1)
    elif bil1==bil2:
        print("idak ada bilangan yang paling besar")
    else:
        print("bilangan yang lebih besar adalah ", bil2)

awal = int(input("Masukkan Bilangan 1 : "))
akhir = int(input("Masukkan Bilangan 2 : "))
bilangan1(awal, akhir)