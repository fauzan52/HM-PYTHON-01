angka = input ('Masukkan angka = ')

if angka.isnumeric() :
    print (int(angka)+5)
elif angka.isalpha() :
    print ('Yang ada masukkan huruf')
else :
    print ('Tidak valid')