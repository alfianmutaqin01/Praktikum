# cari bilangan genap
print("Mencari Bilanggan Genap")
# Meminta input range maksimal dari user
max_range = int(input("Masukkan bilangan maksimal: "))

# Menampilkan semua bilangan genap dari range 2 hingga max_range
for i in range(2, max_range+1, 2):
    print(i)
