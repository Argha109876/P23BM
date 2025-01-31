# Aplikasi Kalkulus
# Menyelesaikan masalah dengan kalkulus

# Kamus:

# Sub Program:
# Mencari Turunan dari F:
def Turunan_Polinomial(F):
    T=0
    while T < F[0][2]:
        F[T][0] = F[T][0]*F[T][1]
        F[T][1]-=1
        if F[T][1]==-1:
            F[0][2]-=1
        T += 1
    return F

# Print fungsi polinomial:
def Print_Polinomial(F):
    T = 0
    A = ""
    while T < F[0][2]:
        koefisien = F[T][0]
        pangkat = F[T][1]
        if koefisien == 0:
            T += 1
            continue
        if A == "":
            if pangkat != 0:
                if koefisien > 0:
                    A = str(koefisien) + "X^" + str(pangkat)
                elif koefisien < 0:
                        A = "-" + str(abs(koefisien)) + "X^" + str(pangkat)
            if pangkat == 0:
                if koefisien > 0:
                    A = str(koefisien)
                elif koefisien < 0:
                    A = "-" + str(abs(koefisien))
        else:
            if pangkat != 0:
                if koefisien > 0:
                    A += " + " + str(koefisien) + "X^" + str(pangkat)
                elif koefisien < 0:
                    A += " - " + str(abs(koefisien)) + "X^" + str(pangkat) 
            if pangkat == 0:
                if koefisien > 0:
                    A += " + " + str(koefisien)
                elif koefisien < 0:
                    A += " - " + str(abs(koefisien))
        T += 1
    return A   

# Nilai y=F(x) dari fungsi F
def F_dari_X (F1,x):
    T = 0
    y = 0
    while T < F1[0][2]:
        koefisien = F1[T][0]
        pangkat = F1[T][1]
        if pangkat != 0:
            y += koefisien*(x**pangkat)
        else:
            y += koefisien
        T += 1
    return y
    
# SubProgram Mencari Pembuat nol:
# Orde 0:
def Pembuatnol_orde0(F):
    x = F[0][0]
    return x

# Orde 1:
def Pembuatnol_orde1(F): 
    if F[0][2] == 2 and F[0][1] == 1:
        x = - F[1][0]/F[0][0]
    if F[0][2] == 1:
        if F[0][1] == 1:
            x = 0
    return x

# Orde 2:
def Pembuatnol_orde2(F):
    x1 = 0
    x2 = 0
    if F[0][2] == 3:
        a = F[0][0]
        b = F[1][0]
        c = F[2][0]
        D = b**2 - 4*a*c  
        if D >= 0:
            x1 = (-b + D**0.5) / (2 * a)  
            x2 = (-b - D**0.5) / (2 * a)  
        else:
            x1 = 0  
            x2 = 0
    elif F[0][2] == 2 and F[1][1] == 1:
        a = F[0][0]
        b = F[1][0]
        c = 0
        D = b**2 - 4*a*c
        if(D >= 0):
            x1 = (-b + D**0.5) / (2 * a)
            x2 = (-b - D**0.5) / (2 * a)
        else:
            x1 = 0
            x2 = 0
    elif F[0][2] == 2 and F[1][1] == 0:
        a = F[0][0]
        b = 0
        c = F[1][0]
        D = b**2 - 4*a*c
        if(D >= 0):
            x1 = (-b + D**0.5) / (2 * a)
            x2 = (-b - D**0.5) / (2 * a)
        else:
            x1 = 0
            x2 = 0
    return x1,x2

# Subprogram untuk menyederhanakan pangkat
def Sederhanakan_Pangkat(F):
    T = 0
    while T < F[0][2]:
        U = T + 1
        while U < F[0][2]:
            if F[T][1] == F[U][1]:  
                F[T][0] += F[U][0]  
                for i in range(U, F[0][2] - 1):  
                    F[i][0] = F[i + 1][0]
                    F[i][1] = F[i + 1][1]
                F[0][2] -= 1  
                U -= 1  
            U += 1
        T += 1
    T = 0
    while T < F[0][2]:
        if F[T][0] == 0:
            for i in range(T, F[0][2] - 1):
                F[i][0] = F[i + 1][0]
                F[i][1] = F[i + 1][1]
            F[0][2] -= 1
            T -= 1
        T += 1
    return F

# Sub Program Turunan Logaritma Natural:
def Turunan_Logaritma_Natural(F):
    dF=Turunan_Polinomial(F)
    print("Turunan pertama = ("+Print_Polinomial(dF)+")/("+  Print_Polinomial(F)+")" )

# Turunan Perkalian Polinomial
# Fungsi untuk mencari turunan sebuah polinomial
def hitung_turunan(polinomial):
    if len(polinomial) <= 1:
        return [0]  # Jika polinomial adalah konstanta, turunan adalah 0
    turunan = [polinomial[i] * (len(polinomial) - 1 - i) for i in range(len(polinomial) - 1)]
    return turunan

# Fungsi untuk mencetak polinomial dalam format yang lebih mudah dibaca
def tampilkan_polinomial(polinomial):
    if all(koef == 0 for koef in polinomial):
        return "0"
    hasil = []
    pangkat_tertinggi = len(polinomial) - 1
    for i in range(len(polinomial)):
        koef = polinomial[i]
        pangkat = pangkat_tertinggi - i
        if koef != 0:
            if pangkat == 0:
                hasil.append(f"{koef}")
            elif pangkat == 1:
                hasil.append(f"{koef}X")
            else:
                hasil.append(f"{koef}X^{pangkat}")
    return " + ".join(hasil).replace("+ -", "- ")

# Fungsi untuk menghitung perkalian dua polinomial
def kali_polinomial(polinomial1, polinomial2):
    hasil = [0] * (len(polinomial1) + len(polinomial2) - 1)
    for i in range(len(polinomial1)):
        for j in range(len(polinomial2)):
            hasil[i + j] += polinomial1[i] * polinomial2[j]
    return hasil

# Fungsi untuk menghitung turunan dari perkalian dua fungsi polinomial
# (F * G)' = F' * G + F * G'
def turunan_perkalian(polinomial1, polinomial2):
    turunan_F = hitung_turunan(polinomial1)  # Turunan F(x)
    turunan_G = hitung_turunan(polinomial2)  # Turunan G(x)
    
    # Hitung F' * G dan F * G'
    F_prim_G = kali_polinomial(turunan_F, polinomial2)
    F_G_prim = kali_polinomial(polinomial1, turunan_G)
    
    # Jumlahkan hasil dari F'G + FG'
    hasil_akhir = [0] * max(len(F_prim_G), len(F_G_prim))
    for i in range(len(F_prim_G)):
        hasil_akhir[i] += F_prim_G[i]
    for i in range(len(F_G_prim)):
        hasil_akhir[i] += F_G_prim[i]
    
    return hasil_akhir

#Fungsi untuk mengitung turunan dari pembagian dua fungsi polinomial
# (F/G)'=(F'*G-F*G')/(G)**2
import numpy as np

def hitung_turunan(polinomial):
    n = len(polinomial)
    turunan = np.zeros(n - 1)
    for i in range(1, n):
        turunan[i - 1] = polinomial[i] * i
    return turunan

# Fungsi untuk mengalikan dua polinomial menggunakan matriks
def kali_polinomial(polinomial1, polinomial2):
    hasil_panjang = len(polinomial1) + len(polinomial2) - 1
    hasil = np.zeros(hasil_panjang)
    for i in range(len(polinomial1)):
        for j in range(len(polinomial2)):
            hasil[i + j] += polinomial1[i] * polinomial2[j]
    return hasil

# Fungsi untuk mengurangi dua polinomial menggunakan matriks
def kurangi_polinomial(polinomial1, polinomial2):
    panjang = max(len(polinomial1), len(polinomial2))
    pol1 = np.pad(polinomial1, (panjang - len(polinomial1), 0))
    pol2 = np.pad(polinomial2, (panjang - len(polinomial2), 0))
    return pol1 - pol2

# Fungsi untuk menghitung turunan dari pembagian dua polinomial
def turunan_pembagian(polinomial1, polinomial2):
    turunan_F = hitung_turunan(polinomial1)  # F'
    turunan_G = hitung_turunan(polinomial2)  # G'

    # Hitung F'*G dan F*G'
    F_prim_G = kali_polinomial(turunan_F, polinomial2)
    F_G_prim = kali_polinomial(polinomial1, turunan_G)

    # Hitung pembilang: F'*G - F*G'
    pembilang = kurangi_polinomial(F_prim_G, F_G_prim)

    # Hitung penyebut: G^2
    penyebut = kali_polinomial(polinomial2, polinomial2)

    return pembilang, penyebut

# Program Menurunkan Fungsi Berpangkat (Metode Substitusi) atau Aturan Rantai
# Fungsi untuk mencari turunan sebuah polinomial
def hitung_turunan(polinomial):
    if len(polinomial) <= 1:
        return [0]  # Jika polinomial adalah konstanta, turunan adalah 0
    turunan = [polinomial[i] * (len(polinomial) - 1 - i) for i in range(len(polinomial) - 1)]
    return turunan

# Fungsi untuk mencetak polinomial dalam format yang lebih mudah dibaca
def tampilkan_polinomial(polinomial):
    if all(koef == 0 for koef in polinomial):
        return "0"
    hasil = []
    pangkat_tertinggi = len(polinomial) - 1
    for i in range(len(polinomial)):
        koef = polinomial[i]
        pangkat = pangkat_tertinggi - i
        if koef != 0:
            if pangkat == 0:
                hasil.append(f"{koef}")
            elif pangkat == 1:
                hasil.append(f"{koef}X")
            else:
                hasil.append(f"{koef}X^{pangkat}")
    return " + ".join(hasil).replace("+ -", "- ")

# Fungsi untuk menghitung turunan dari (f(x))^k menggunakan aturan rantai
def turunan_perkalian(fx, k):
    # Hitung turunan dari f(x)
    turunan_F = hitung_turunan(fx)
    
    # Menyusun hasil dalam bentuk k(f(x))^(k-1) * f'(x)
    f_of_x = tampilkan_polinomial(fx)
    turunan_of_f = tampilkan_polinomial(turunan_F)
    
    # Menyusun ekspresi turunan
    if len(fx) == 2:  # Bentuk linear
        # Koefisien f(x) adalah koefisien pertama untuk linear
        koef_f = fx[0]
        du_dx = f"{koef_f}"
        hasil_turunan = f"{k * koef_f}({f_of_x})^{k-1}"
    else:  # Bentuk kuadrat atau lebih tinggi
        # Koefisien f(x) adalah koefisien pertama untuk kuadrat
        koef_f = fx[0]
        du_dx = f"{koef_f}"
        hasil_turunan = f"{k}({tampilkan_polinomial(turunan_F)})({f_of_x})^{k-1}"

    return hasil_turunan, du_dx

# Algoritma Utama
# Memilih Program yang ingin dijalankan
print("Selamat Datang di Aplikasi Kalkulus!")
print()
print("List Program :")
print("1. Mencari Data Penting fungsi polinomial orde 2 atau orde 3")
print("2. Mencari Turunan suatu Fungsi dasar")
print("3. Menghitung luas diantara dua fungsi (Belum Tersedia)")
print("4. Menghitung volume benda (Belum Tersedia)")
print("5. Mencari Penambahan dan peluruhan eksponensial (Belum Tersedia)")
print()
Program = int(input("Pilih Program yang akan dijalankan = "))
print()

# Program 1 (Mencari Data Penting):
if Program == 1:
    # Input Banyak konstanta 
    R = int(input("Masukkan total variabel x (Termasuk konstanta tanpa X) = "))
    F = [[0 for j in range(3)] for i in range(R)]
    F[0][2] = R

    # Print Aturan Penting
    print()
    print("Aturan Penting!!")
    print("1. Untuk Konstanta tanpa x, beri pangkat 0")
    print("2. Jangan memasukkan pangkat di bawah 0")
    print()

    # Input Fungsi:
    for i in range(R):
        F[i][0]= float(input("Masukkan konstanta variabel x-"+str(i+1)+" = "))
        F[i][1]= int(input("Masukkan pangkat variabel x-"+str(i+1)+" = "))

    # Mengurutkan pangkat dari yang paling besar
    # Pisahkan kolom 1, kolom 2, dan kolom 3
    kolom_1 = [row[0] for row in F]
    kolom_2 = [row[1] for row in F]
    kolom_3 = [row[2] for row in F]

    # Gabungkan menjadi list of list (kolom_1, kolom_2)
    Gabungan = [[kolom_1[i], kolom_2[i]] for i in range(len(kolom_1))]

    # Mengurutkan berdasarkan kolom 2
    urutan = sorted(Gabungan, key=lambda x: x[1], reverse=True)

    # Langkah 4: Pisahkan kembali menjadi kolom-kolom dan gabungkan kembali
    kolom_1_urut = [row[0] for row in urutan]
    kolom_2_urut = [row[1] for row in urutan]

    # Gabungkan kembali kolom-kolom menjadi matriks
    F = [[kolom_1_urut[i], kolom_2_urut[i], kolom_3[i]] for i in range(len(kolom_1_urut))]
    F = Sederhanakan_Pangkat(F)
    
    # Print data penting
    print()
    print("Data Penting :")
    print()
    print("Fungsi:")
    print("Fungsi awal = ", Print_Polinomial(F))

    # Jika fungsi orde 2
    if F[0][1] == 2 :
        # Menyalin fungsi pertama untuk dipakai mencari titik kritis:
        F1 = [[x for x in row] for row in F]

        # Mencari turunan pertama fungsi:
        F = Turunan_Polinomial(F)
        print("Turunan Pertama = ", Print_Polinomial(F))

        # Mencari Pembuat nol, titik kritis, dan kemonotonan
        x = Pembuatnol_orde1(F)
        y =  F_dari_X (F1,x)
        if F1[0][0] >= 0:
            Monoton1 = "Fungsi monoton naik pada [" +str(x)+ ",Tak hingga]"
            Monoton2 = "Fungsi monoton turun pada [- Tak hingga, "+str(x)+ "]"
            Kritis = "Titik Minimum = "+str(y)
        if F1[0][0] < 0:
            Monoton1 = "Fungsi monoton naik pada [- Tak hingga, "+ str(x)+ "]"
            Monoton2 = "Fungsi monoton turun pada [" +str(x)+ ",Tak hingga]"
            Kritis = "Titik Maksimum = ", y

        # Mencari turunan kedua
        F = Turunan_Polinomial(F)
        print("Turunan Kedua = ", Print_Polinomial(F))
        print()
        
        # Print data kemonotonan
        print("Kemonotonan :")
        print(Monoton1)
        print(Monoton2)
        print(Kritis)
        print()

        # Mencari pembuat nol dan kecekungan
        x = Pembuatnol_orde0(F)
        print("Kecekungan :")
        print("Fungsi bernilai konstan ", x)
        if x >0:
            print("Sehingga Fungsi selalu cekung ke atas")
        if x <0:
            print("Sehingga Fungsi selalu cekung ke bawah")
        if x ==0:
            print("Sehingga Fungsi tidak memiliki kecekungan")

            
    # Jika fungsi orde 3
    elif F[0][1] == 3 :
        # Menyalin fungsi pertama untuk dipakai mencari titik kritis:
        F1 = [[x for x in row] for row in F]

        # Mencari turunan pertama fungsi:
        F = Turunan_Polinomial(F)
        print("Turunan Pertama = ", Print_Polinomial(F))
        
        # Mencari Pembuat nol, titik kritis, dan kemonotonan
        x1,x2 = Pembuatnol_orde2(F)
        if x1==0 and x2==0:
            print("Tidak ada akar pembuat nol")
            print("Fungsi tidak memiliki titik kritis")
            if F[0][0] > 0 :
                print("Fungsi selalu monoton naik di seluruh bilangan real")
            if F[0][0] < 0 :
                print("Fungsi selalu monoton turun di seluruh bilangan real")
        else:
            print("Pembuat nol =")
            print("x1 = ", x1)
            print("x2 = ", x2)
            x = x1
            y1 = F_dari_X (F1,x)
            x = x2
            y2 = F_dari_X (F1,x)
            print("Titik kritis pertama = [", x1, " , ", y1, "]")
            print("Titik kritis kedua = [", x2, " , ", y2, "]")
            if x1>x2:
                kritis_kiri= y2
                kritis_kanan= y1
                if kritis_kanan>kritis_kiri:
                    print("Fungsi monoton turun pada [- Tak hingga, ", x2, "]")
                    print("Fungsi monoton naik pada [",x2, x1, "]")
                    print("Fungsi monoton turun pada [", x1, ",Tak hingga]")
                    print("Minimum lokal terjadi pada [", x2, " , ", y2, "]")
                    print("Maksimum lokal terjadi pada [", x1, " , ", y1, "]")
                else:
                    print("Fungsi monoton naik pada [- Tak hingga, ", x2, "]")
                    print("Fungsi monoton turun pada [",x2, x1, "]")
                    print("Fungsi monoton naik pada [", x1, ",Tak hingga]")
                    print("Minimum lokal terjadi pada [", x1, " , ", y1, "]")
                    print("Maksimum lokal terjadi pada [", x2, " , ", y2, "]")
            elif x2>x1:
                kritis_kiri= y1
                kritis_kanan= y2
                if kritis_kanan>kritis_kiri:
                    print("Fungsi monoton turun pada [- Tak hingga, ", x1, "]")
                    print("Fungsi monoton naik pada [",x1, x2, "]")
                    print("Fungsi monoton turun pada [", x2, ",Tak hingga]")
                    print("Minimum lokal terjadi pada [", x1, " , ", y1, "]")
                    print("Maksimum lokal terjadi pada [", x2, " , ", y2, "]")
                    
                else:
                    print("Fungsi monoton naik pada [- Tak hingga, ", x1, "]")
                    print("Fungsi monoton turun pada [",x1, x2, "]")
                    print("Fungsi monoton naik pada [", x2, ",Tak hingga]")
                    print("Minimum lokal terjadi pada [", x2, " , ", y2, "]")
                    print("Maksimum lokal terjadi pada [", x1, " , ", y1, "]")
            else: 
                x = x1 + 1
                y = F_dari_X (F1,x)
                if y>y1:
                    print("Fungsi monoton naik di seluruh bilangan real")
                if y<y1:
                    print("Fungsi monoton turun di seluruh bilangan real")
        print()
        
        # Mencari turunan kedua
        F = Turunan_Polinomial(F)
        print("Turunan Kedua = ", Print_Polinomial(F))
        
        # Mencari pembuat nol dan kecekungan
        x = Pembuatnol_orde1(F)
        print("Pembuat nol =", x)
        y =  F_dari_X (F1,x)
        print("Titik Belok adalah = [", x, " , ", y,"]")
        x1 = x + 1
        yz = F_dari_X (F1,x)
        if yz>y:
            print("Fungsi cekung ke bawah pada [- Tak hingga, ", x, "]")
            print("Fungsi cekung ke atas pada [", x, ",Tak hingga]")
        if yz<y:
            print("Fungsi cekung ke atas pada [- Tak hingga, ", x, "]")
            print("Fungsi cekung ke bawah pada [", x, ",Tak hingga]") 

# Program 2 (Kalkulator Turunan):
if Program == 2:
    print("Kalkulator Turunan :")
    print("1. Fungsi Polinomial")
    print("2. Perkalian 2 Fungsi")
    print("3. Pembagian 2 Fungsi")
    print("4. Fungsi Berpangkat")
    print("5. Fungsi Logaritma Natural")
    print()
    kalkulator = int(input("Pilih Tipe Fungsi : "))
    print()
    
    # Tipe Fungsi Polinomial:
    if kalkulator == 1:
        # Input Banyak konstanta 
        R = int(input("Masukkan total variabel x (Termasuk konstanta tanpa X) = "))
        F = [[0 for j in range(3)] for i in range(R)]
        F[0][2] = R
        # Input Fungsi:
        for i in range(R):
            F[i][0]= float(input("Masukkan konstanta variabel x-"+str(i+1)+" = "))
            F[i][1]= int(input("Masukkan pangkat variabel x-"+str(i+1)+" = "))

        # Mengurutkan pangkat dari yang paling besar
        # Pisahkan kolom 1, kolom 2, dan kolom 3
        kolom_1 = [row[0] for row in F]
        kolom_2 = [row[1] for row in F]
        kolom_3 = [row[2] for row in F]

        # Gabungkan menjadi list of list (kolom_1, kolom_2)
        Gabungan = [[kolom_1[i], kolom_2[i]] for i in range(len(kolom_1))]

        # Mengurutkan berdasarkan kolom 2
        urutan = sorted(Gabungan, key=lambda x: x[1], reverse=True)

        # Langkah 4: Pisahkan kembali menjadi kolom-kolom dan gabungkan kembali
        kolom_1_urut = [row[0] for row in urutan]
        kolom_2_urut = [row[1] for row in urutan]

        # Gabungkan kembali kolom-kolom menjadi matriks
        F = [[kolom_1_urut[i], kolom_2_urut[i], kolom_3[i]] for i in range(len(kolom_1_urut))]
        F = Sederhanakan_Pangkat(F)
        F = Turunan_Polinomial(F)
        print()
        print("Turunan Pertama = ", Print_Polinomial(F))
        
    # Tipe Fungsi Perkalian 2 fungsi:
    if kalkulator == 2:
        # Panduan input dari pengguna
        print("\nPanduan Input:")
        print("1. Input koefisien dimulai dari orde tertinggi hingga orde terendah.")
        print("2. Pisahkan setiap koefisien dengan spasi.")
        print("   Contoh untuk 3X^2 + 2X - 5, inputkan: 3 2 -5\n")

        # Input koefisien polinomial dari pengguna
        print("Masukkan koefisien untuk fungsi F(x) (dari orde tertinggi ke terendah):")
        polinomial_F = list(map(float, input().split()))

        print("Masukkan koefisien untuk fungsi G(x) (dari orde tertinggi ke terendah):")
        polinomial_G = list(map(float, input().split()))

        # Hitung turunan masing-masing polinomial
        turunan_F = hitung_turunan(polinomial_F)
        turunan_G = hitung_turunan(polinomial_G)

        # Hitung turunan dari perkalian kedua polinomial
        hasil_turunan_perkalian = turunan_perkalian(polinomial_F, polinomial_G)

        # Tampilkan hasil
        print(f"\nFungsi F(x): {tampilkan_polinomial(polinomial_F)}")
        print(f"Fungsi G(x): {tampilkan_polinomial(polinomial_G)}")
        print(f"Turunan F(x): {tampilkan_polinomial(turunan_F)}")
        print(f"Turunan G(x): {tampilkan_polinomial(turunan_G)}")
        print(f"Turunan (F * G)(x): {tampilkan_polinomial(hasil_turunan_perkalian)}")
    
    #Fungsi untk turunan pembagian 2 fungsi
    if kalkulator == 3:
    #Panduan untuk Pengguna
        print("\n--- Turunan Pembagian Polinomial ---")
        print("Panduan Input:")
        print("1. Input koefisien dimulai dari orde tertinggi hingga orde terendah.")
        print("2. Pisahkan setiap koefisien dengan spasi.")
        print("   Contoh untuk 3x^2 + 2x - 5, inputkan: 3 2 -5\n")
    # Input polinomial F(x) dan G(x)
        print("Masukkan koefisien untuk fungsi F(x) (orde tertinggi ke terendah):")
        polinomial_F = np.array(list(map(float, input().split())))
        print("Masukkan koefisien untuk fungsi G(x) (orde tertinggi ke terendah):")
        polinomial_G = np.array(list(map(float, input().split())))
    # Hitung turunan masing-masing
        turunan_F = hitung_turunan(polinomial_F)
        turunan_G = hitung_turunan(polinomial_G)
        # Hitung turunan pembagian
        pembilang, penyebut = turunan_pembagian(polinomial_F, polinomial_G)
    # Tampilkan hasil
        print(f"\nFungsi F(x): {tampilkan_polinomial(polinomial_F)}")
        print(f"Fungsi G(x): {tampilkan_polinomial(polinomial_G)}")
        print(f"Turunan F(x): {tampilkan_polinomial(turunan_F)}")
        print(f"Turunan G(x): {tampilkan_polinomial(turunan_G)}")
        print(f"Turunan (F/G)(x): ({tampilkan_polinomial(pembilang)}) / ({tampilkan_polinomial(penyebut)})")
        
    # Tipe Fungsi Polinomial Berpangkat
    if kalkulator == 4:
        # Panduan input dari pengguna
        print("\nPanduan Input:")
        print("1. Formula yang akan digunakan adalah sebagai berikut:")
        print("         d/dx (f(x))^k = k . (f(x))^k-1 . f'(x)")
        print("2. f(x) merupakan polinomial")
        print("3. Input koefisien dimulai dari orde tertinggi hingga orde terendah.")
        print("4. Pisahkan setiap koefisien dengan spasi.")
        print("   Contoh untuk 3X^2 + 2X - 5, inputkan: 3 2 -5\n")

        # Input untuk polinomial f(x) dan nilai k
        polinomial_F = list(map(float, input("Masukkan koefisien untuk fungsi F(x) (dari orde tertinggi ke terendah): ").split()))
        k = float(input("Masukkan nilai k: "))

        # Hitung turunan dari (f(x))^k
        hasil_turunan, du_dx = turunan_perkalian(polinomial_F, k)

        # Menampilkan hasil
        print(f"\nf(x)                : {tampilkan_polinomial(polinomial_F)}")
        print(f"f'(x)               : {du_dx}")
        print(f"Turunan (f(x))^{k}  : {hasil_turunan}")


    # Tipe Fungsi Logaritma Natural:
    if kalkulator == 5:
        # Memsukkan fungsi numerus 
        print("tentukan fungsi numerus f(x) untuk menghitung turunan ln[f(x)]" )
        R = int(input("Masukkan total variabel x (Termasuk konstanta tanpa X) = "))
        F = [[0 for j in range(3)] for i in range(R)]
        F[0][2] = R
        
        # Input Fungsi:
        for i in range(R):
            F[i][0]= float(input("Masukkan konstanta variabel x-"+str(i+1)+" = "))
            F[i][1]= int(input("Masukkan pangkat variabel x-"+str(i+1)+" = "))

        # Mengurutkan pangkat dari yang paling besar
        # Pisahkan kolom 1, kolom 2, dan kolom 3
        kolom_1 = [row[0] for row in F]
        kolom_2 = [row[1] for row in F]
        kolom_3 = [row[2] for row in F]

        # Gabungkan menjadi list of list (kolom_1, kolom_2)
        Gabungan = [[kolom_1[i], kolom_2[i]] for i in range(len(kolom_1))]

        # Mengurutkan berdasarkan kolom 2
        urutan = sorted(Gabungan, key=lambda x: x[1], reverse=True)

        # Langkah 4: Pisahkan kembali menjadi kolom-kolom dan gabungkan kembali
        kolom_1_urut = [row[0] for row in urutan]
        kolom_2_urut = [row[1] for row in urutan]

        # Gabungkan kembali kolom-kolom menjadi matriks
        F = [[kolom_1_urut[i], kolom_2_urut[i], kolom_3[i]] for i in range(len(kolom_1_urut))]
        F = Sederhanakan_Pangkat(F)
        
        print("") #jeda agar terlihat rapi

        # Menampilkan fungsi logaritma natural awal
        print ("fungsi awal = ln["+ Print_Polinomial(F)+ "]")

        # Menampilkan turunan pertama dari ln(f[x])
        Turunan_Logaritma_Natural(F)
        
        
    
    
