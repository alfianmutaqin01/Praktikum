
t = int(input("Masukkan Tahun: "))
if t % 4 == 0:
    if t%100 == 0:
        if t%400 == 0:
            print(t,"tahun kabisat")
        else:
            print(t,"bukan tahun kabisat")
    else:
        print(t,"tahun kabisat")
else:
    print(t,"bukan tahun kabisat")
    