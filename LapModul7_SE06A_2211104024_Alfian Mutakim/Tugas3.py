def addbuku():
    jumlah = int(input("Masukkan total buku: "))
    buku = []
    while jumlah > 0:
        nama = input("judul buku ke-{}: ".format(jumlah))
        buku.append(nama)
        jumlah = jumlah - 1

    while True:
        panggil(buku)
        jumlah = jumlah - 1
        if jumlah < 0:
            break


# Urutkan Data buku - insertion sort
def insertion_sort(arraybuku):
    buku = arraybuku
    for i in range(1, len(arraybuku)):
        item = arraybuku[i]
        j = i - 1

        while j >= 0 and arraybuku[j] >= item:
            arraybuku[j + 1] = arraybuku[j]
            j -= 1

        arraybuku[j + 1] = item

    return arraybuku


buku = []
# print("Before: {}".format(buku))
# insertion_sort(buku)
# print("After: {}".format(buku))


# Urutkan Data buku - insertion sort descending
def insertion_sort_Descending(arraybuku):
    buku = arraybuku
    for i in range(1, len(arraybuku)):
        item = arraybuku[i]
        j = i - 1
        while j >= 0 and arraybuku[j] <= item:
            arraybuku[j + 1] = arraybuku[j]
            j -= 1

        arraybuku[j + 1] = item

    return arraybuku


buku = []
# print("Before: {}".format(buku))
# insertion_sort_Descending(buku)
# print("After: {}".format(buku))


# Menu
def panggil(arraybuku):
    print("\n<======= Urutkan? ========>")
    print("1. Metode Ascending")
    print("2. Metode Descending")
    pilih = int(input("Pilih: "))

    if pilih == 1:
        insertion_sort(arraybuku)
    else:
        insertion_sort_Descending(arraybuku)

    print("Sorted array: {}".format(arraybuku))


addbuku()
