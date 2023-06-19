print("======Sistem Login Sederhana======")
# inisialisasi variabel
password = "1234"
username = "alfian"
percobaan = 3

# pengguna diminta untuk memasukkan password
while percobaan > 0:
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")
    if input_username and input_password == username and password :
        print("Selamat datang", username,"!")
        break
    else:
        percobaan -= 1
        print("Password salah. Anda memiliki", percobaan, "percobaan lagi.")
else:
    print("Anda telah mencoba 3 kali. Mohon tunggu beberapa saat untuk mencoba lagi.")