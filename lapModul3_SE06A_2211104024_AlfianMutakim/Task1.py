# Menentukan huruf vokal atau konsonan

huruf = str(input("Masukkan Huruf : "))
if (huruf=='a' or huruf=='i' or huruf=='u' or huruf=='e' or huruf=='o' 
    or huruf=='A' or huruf=='I' or huruf=='U' or huruf=='E' or huruf=='O'):
    print("Huruf", huruf, "Merupakan Huruf Vokal")
else:
    print("Huruf", huruf, "Merupakan Huruf Konsonan")