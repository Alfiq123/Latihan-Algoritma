print("""
  ___                  _     ___  _  _                               
 |   \  ___  _ _  ___ | |_  | _ )(_)| | __ _  _ _   __ _  __ _  _ _  
 | |) |/ -_)| '_|/ -_)|  _| | _ \| || |/ _` || ' \ / _` |/ _` || ' \ 
 |___/ \___||_|  \___| \__| |___/|_||_|\__,_||_||_|\__, |\__,_||_||_|
                                                   |___/             """)

print("""
Deret bilangan :
    a. 1 2 3 4 5 6 7 8 9 10
    b. 10 9 8 7 6 5 4 3 2 1 0
    c. 1 4 9 16 25 36 49 64 81 100
    d. 1 3 5 7 9 11 13 15
    e. 0 2 4 6 8 10 12 14 16
    f. 1 4 7 10 13 16 19 22
    g. 100 81 64 49 36 25 16 9 4 1 0
    h. 60 55 50 45 40 35 30 25 20 15 10
    i. 1 3 6 10 15 21 28 36 45 55
    j. 1 2 6 24 120 720 5040 40320 362880 3628800
""")

total = 0

pilihan_deret = str(input("Masukkan Huruf yang ingin dipilih: ")).lower()
while pilihan_deret not in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"):
    print("✨ Tolong masukkan huruf yang benar! ✨")
    pilihan_deret = str(input("Masukkan Huruf yang ingin dipilih: ")).lower()

# A. Normal (1, 2, 3).
if pilihan_deret == "a":
    for i in range(1, 11):
        print(i)

# B. Normal tapi kebalik (3, 2, 1).
elif pilihan_deret == "b":
    for i in range(10, -1, -1):
        print(i)

# C. Setiap suku ke-n dipangkatkan 2.
elif pilihan_deret == "c":
    for i in range(1, 11):
        print(i ** 2)

# D. Angka Ganjil, Mulai dari 1.
elif pilihan_deret == "d":
    for i in range(1, 16, 2):
        print(i)

# E. Angka Genap, Mulai Dari 0.
elif pilihan_deret == "e":
    for i in range(0, 17, 2):
        print(i)

elif pilihan_deret == "f":
    for i in range(1, 23, 3):
        print(i)

elif pilihan_deret == "g":
    for i in range(11):
        print(f"{(10 - i) ** 2}")

elif pilihan_deret == "h":
    for i in range(60, 0, -5):
        print(i)

elif pilihan_deret == "i":
    for i in range(1, 11):
        print(f"{i * (i + 1) / 2:.0f}")

elif pilihan_deret == "j":
    faktorial = 1
    for i in range(1, 11):
        faktorial *= i
        print(faktorial)
