array = []

n = int(input('\nMasukkan Jumlah Mata Kuliah : ')) 
print()

for i in range(n):
    nilai = float(input('Masukkan nilai mata kuliah ke-{} : '.format(i + 1)))
    array.append(nilai)
        # append berarti menambahkan 
    # float = tipe data desimal
    # \n = memberi jarak 1 baris 
    # {} = memasukkan formula misal .format(i + 1)

#rata = sum(array)/n
rata=  sum(array)
rata2= len(array) 

rata_rata = rata/rata2


print()
if rata_rata < 100  and rata_rata  >= 90 :
    print('Hasil Predikat A dengan nilai rata-rata : ', rata_rata)
elif rata_rata < 90 and rata_rata >= 70 :
    print('Hasil Predikat B dengan nilai rata-rata : ', rata_rata)
elif rata_rata < 70 and rata_rata >= 50 :
    print('Hasil Predikat C dengan nilai rata-rata : ', rata_rata)
elif rata_rata < 50 and rata_rata >= 30 :
    print('Hasil Predikat D dengan nilai rata-rata : ', rata_rata)
elif rata_rata < 30 and rata_rata >= 0 :
    print('Hasil Predikat E dengan nilai rata-rata : ', rata_rata)
else:
    print('Nilai tidak valid !')


for x in range(n):
    print('Mata kuliah ke-{}' .format(x), ' : ', (array[x]))