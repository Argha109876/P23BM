# Sub Program Penting:
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
    
  
# Algoritma Utama:
# Input Banyak konstanta 
R = int(input("Masukkan total variabel x (Termasuk konstanta tanpa X) = "))
F = [[0 for j in range(3)] for i in range(R)]
F[0][2] = R

# Print Aturan Penting
print()
print("Aturan Penting!!")
print("1. Masukkan dari pangkat tertinggi agar tidak error!")
print("2. Masukkan persamaan paling sederhana (Tidak ada pangkat yang sama)!")
print("3. Untuk Konstanta tanpa x, beri pangkat 0")
print("4. Jangan memasukkan pangkat di bawah 0")
print()

# Input Fungsi:
for i in range(R):
    F[i][0]= float(input("Masukkan konstanta variabel x-"+str(i+1)+" = "))
    F[i][1]= int(input("Masukkan pangkat variabel x-"+str(i+1)+" = "))

print()
print("fungsi awal = ", Print_Polinomial(F))

# Jika fungsi orde 2
if F[0][1] == 2 :
    # Menyalin fungsi pertama untuk dipakai mencari titik kritis:
    F1 = [[x for x in row] for row in F]
    print()

    # Mencari turunan pertama fungsi:
    F = Turunan_Polinomial(F)
    print("Turunan Pertama = ", Print_Polinomial(F))

    # Mencari Pembuat nol, titik kritis, dan kemonotonan
    x = Pembuatnol_orde1(F)
    print("Pembuat nol =", x)
    y =  F_dari_X (F1,x)
    print("Titik Kritis adalah y = ", y)
    if F1[0][0] >= 0:
        print("Fungsi monoton naik pada [", x, ",Tak hingga]")
        print("Fungsi monoton turun pada [- Tak hingga, ", x, "]")
    if F1[0][0] < 0:
        print("Fungsi monoton naik pada [- Tak hingga, ", x, "]")
        print("Fungsi monoton turun pada [", x, ",Tak hingga]")

    print()
    # Mencari turunan kedua
    F = Turunan_Polinomial(F)
    print("Turunan Kedua = ", Print_Polinomial(F))

    # Mencari pembuat nol dan kecekungan
    x = Pembuatnol_orde0(F)
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
    print()

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

    