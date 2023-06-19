def hitung(angka):
    if angka ==0:
        print("bilangan yang anda masukkan adalah bilangan nol")
    else:
        if angka%2==0:
         print("bilangan yang anda masukkan adalah bilangan genap")   
        else:
           print("bilangan yang anda masukkan adalah bilangan ganjil")

bilangan = int(input("Masukkan Bilangan : "))
hitung(bilangan)

