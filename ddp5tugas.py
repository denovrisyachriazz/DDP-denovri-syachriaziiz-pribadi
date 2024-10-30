#soal no satu

kendaraan = ["mio",
"motor", "200cc", "hitam", "roda2"]
kendaraan.append("5.000.000")
kendaraan.append("matic")
print(kendaraan)
kendaraan.insert (2, "yamaha")
print(kendaraan)

#soal no dua

pilihan = int(input("""Pilih nomor pilihan:
1. Menghitung luas Persegi
2. Menghitung luas Lingkaran
3. Menghitung luas segitiga"""))

match pilihan:

    case 1:
         print("Menghitung luas Persegi")
         s = int(input("Masukkan nilai sisi: "))
         luasPersegi = s * s
         print(f"Luas persegi dengan sisi {s} adalah {luasPersegi}")
    case 2:
        print("Menghitung luas Lingkaran")
        pi = 1,14
        r = int(input("Masukkan nilai jari-jari"))
        luasLingkaran = p1 * r ** 2
        print(f"Luas     lingkaran dengan jari-jari (r) adalah {luasLingkaran}")
    case 3:
        print("Menghitung luas Segitiga")
        alas = int(input("Masukkan nilai alas: "))
        tinggi = int(input("Masukkan nilai tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")
    case _:
        print("input tidak valid")