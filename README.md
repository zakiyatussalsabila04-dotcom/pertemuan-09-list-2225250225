# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: ZAKIYATUS SALSABILA  
NIM: 2225250225
Kelas: 3F

## Tujuan

Praktikum ini bertujuan untuk mempelajari penggunaan list Python dalam menyimpan dan mengolah kumpulan data numerik. Program digunakan untuk menghitung total nilai, rata-rata, nilai minimum, nilai maksimum, serta jumlah mahasiswa yang lulus dan belum lulus.

## Struktur Program

Program disimpan dalam file `praktik/analisis_nilai_mahasiswa.py`.

Program terdiri dari beberapa bagian, yaitu:
1. List untuk menyimpan minimal 10 nilai mahasiswa.
2. Fungsi `rata_rata(data)` untuk menghitung rata-rata nilai.
3. Fungsi `nilai_lulus(data, batas=60)` untuk menghitung jumlah mahasiswa yang lulus.
4. Perhitungan jumlah data, total nilai, nilai minimum, dan nilai maksimum.
5. List baru untuk menyimpan nilai mahasiswa yang lulus.
6. Output untuk menampilkan seluruh hasil analisis.

## Cara Menjalankan

Buka terminal VS Code, kemudian jalankan perintah berikut:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

Program akan menampilkan data nilai, banyak data, total nilai, rata-rata, nilai minimum, nilai maksimum, jumlah mahasiswa lulus, jumlah mahasiswa belum lulus, dan daftar nilai mahasiswa yang lulus.

## Test Case

| No. | Data | Pengujian | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | [60, 70, 80] | Rata-rata | 70.00 |
| 2 | [60, 70, 80] | Minimum dan maksimum | 60 / 80 |
| 3 | [60, 70, 80] | Jumlah lulus | 3 |
| 4 | [59, 60, 61] | Batas kelulusan 60 | 2 lulus |
| 5 | [] | Rata-rata list kosong | Tidak error |

Hasil aktual diisi sesuai hasil program setelah setiap pengujian dijalankan. Status pengujian ditulis berhasil apabila hasil aktual sesuai dengan hasil yang diharapkan.

## Refleksi

Dari praktikum ini, saya memahami bahwa list dapat digunakan untuk menyimpan banyak nilai dalam satu variabel sehingga data lebih mudah diolah. Saya juga belajar menggunakan fungsi agar kode lebih terstruktur dan dapat digunakan kembali.

Saya memahami penggunaan `len()` untuk menghitung banyak data, `sum()` untuk menghitung total nilai, serta `min()` dan `max()` untuk mencari nilai terkecil dan terbesar. Selain itu, saya belajar menggunakan perulangan dan kondisi untuk menentukan mahasiswa yang lulus berdasarkan batas nilai 60.

Kesalahan yang perlu diperhatikan adalah pembagian dengan nol ketika list kosong. Hal tersebut dapat dihindari dengan memeriksa apakah list memiliki data sebelum menghitung rata-rata. Praktikum ini membantu saya memahami pengolahan data numerik menggunakan list, fungsi, perulangan, dan kondisi dalam Python.

## Kesimpulan

Program analisis nilai mahasiswa dapat mengolah data secara terstruktur dan menampilkan ringkasan statistik serta informasi kelulusan. Pengujian dilakukan untuk memastikan setiap fungsi menghasilkan nilai yang benar dan program dapat menangani list kosong tanpa error.
