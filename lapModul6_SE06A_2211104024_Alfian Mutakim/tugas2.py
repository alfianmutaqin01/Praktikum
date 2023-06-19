# Menggunakan Function
print('-------')
def keliling_lingkaran(jari):
    keliling = 2 * 3.14 * jari
    return keliling

def luas_lingkaran(jari):
    luas = 3.14 * (jari*jari)
    return luas

s = int(input("Masukkan jari-jari :"))
print("Keliling : %d" % keliling_lingkaran(s))
print("Luas : %d" % luas_lingkaran(s))