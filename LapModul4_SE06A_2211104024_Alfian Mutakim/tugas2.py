print("===== PROGRAM SEDERHANA MENGHITUNG PANGKAT =====")
angka = int(input("Masukkan bilangan bulat: "))
pangkat = int(input("Masukkan pencacah: "))
x = 1
for i in range(pangkat):
    x *= angka
print("Hasil dari bilangan yang dimasukkan adalah: " + str(x))
