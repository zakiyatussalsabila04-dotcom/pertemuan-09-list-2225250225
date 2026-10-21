
def rata_rata(data):
    # Menghitung nilai rata-rata
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=66):
    # Menghitung jumlah siswa yang lulus
    return sum(1 for nilai in data if nilai >= batas)


# Data nilai siswa
nilai = [78, 55, 99, 67, 60, 82, 45, 71, 88, 59]

# Menghitung hasil
rata = rata_rata(nilai)
lulus = nilai_lulus(nilai)
belum_lulus = len(nilai) - lulus

# Menampilkan ringkasan
print("Data nilai:", nilai)
print(f"Rata-rata: {rata:.2f}")
print(f"Nilai minimum: {min(nilai)}")
print(f"Nilai maksimum: {max(nilai)}")
print(f"Jumlah siswa lulus: {lulus}")
print(f"Jumlah siswa belum lulus: {belum_lulus}")
