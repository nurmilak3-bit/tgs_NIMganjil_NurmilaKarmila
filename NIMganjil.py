def pangkat():
    a = int(input("masukan suatu bilangan bulat : "))
    b = int(input("masukan pangkat yang diinginkan : "))

    hasil = 1
    for i in range(1, b + 1):
        hasil *= a
        print(f"hasil {a} pangkat {i} adalah {hasil}")

def deret():
    n = int(input("Masukkan jumlah N : "))

    hasil = 0
    pembilang = 1
    penyebut = 1
    tanda = 1

    for i in range(n):
        if i == 0:
            hasil += 1
        else:
            pembilang = pembilang + penyebut
            penyebut = pembilang + penyebut
            nilai = pembilang / penyebut
            if tanda == 1:
                hasil -= nilai
            else:
                hasil += nilai
            tanda *= -1

    print(hasil)


while True:
    print("\nNim Ganjil")
    print("1. A pangkat B")
    print("2. Hitung 1 - 2/3 + 5/8 - 13/21 +")
    print("0. keluar")

    pilih = int(input("Masukkan : "))

    if pilih == 1:
        pangkat()
    elif pilih == 2:
        deret()
    elif pilih == 0:
        break
    else:
        print("Pilihan tidak valid")