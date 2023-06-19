
print("===== PROGRAM SEDERHANA MENGHITUNG JUMLAH TOTAL BILANGAN =====")
a = int(input("Masukkan angka: "))
total = 0
print("Total Nilai = ", end="")
for i in range(1, a+1):
    total += i
    if i == 1:
        print(str(i), end="")
    else:
        print(" + "+str(i), end="")
print(" = "+str(total))