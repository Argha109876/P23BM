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

#Fungsi untk turunan pembagian 2 fungsi
if kalkulator == 3:
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