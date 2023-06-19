# KALKULATOR SEDERHANA

def penjumlahan ():
    bil1 = int(input("Bilangan pertama: "))
    bil2 = int(input("Bilangan kedua: "))
    jumlah = bil1 + bil2
    print("hasil penjumlahan : %d" %jumlah)

def kali():
    bil1 = int(input("Bilangan pertama: "))
    bil2 = int(input("Bilangan kedua: "))
    perkalian = bil1 * bil2
    print("hasil perkalian : %d" %perkalian)

def bagi():
    bil1 = int(input("Bilangan pertama: "))
    bil2 = int(input("Bilangan kedua: "))
    pembagian = bil1 / bil2
    print("hasil pembagian : %d" %pembagian)

def kurang():
    bil1 = int(input("Bilangan pertama: "))
    bil2 = int(input("Bilangan kedua: "))
    pengurangan = bil1 - bil2
    print("hasil pengurangan : %d" %pengurangan)

def perpangkatan():
    bil1 = int(input("Bilangan pertama: "))
    bil2 = int(input("Bilangan kedua: "))
    pangkat = bil1**bil2
    print("hasil pangkat : %d" %pangkat)

while True:
    print("===========Kalkulator Sederhana===========")
    print()
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pembagian")
    print("4. Pengurangan")
    print("5. Pangkat")
    print()
    a = int(input("Masukkan pilihan anda: "))
    if a == 1:
        penjumlahan()
    elif a == 2:
        kali()
    elif a == 3:
        bagi()
    elif a == 4:
        kurang()
    elif a == 5:
        perpangkatan()
    else:
        print("pilihan yang anda masukkan tidak valid")

    ulangi = input("Apakah Anda ingin mengulangi program? (ya/tidak): ")
    if ulangi.lower() != "ya":
        break



