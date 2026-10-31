# Pertemuan 11 - Dictionary/Map

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Program ini menggunakan *nested dictionary* (dictionary bersarang). Key utama yang digunakan adalah **NIM** mahasiswa (contoh: `"A001"`, `"A002"`, dst.), sedangkan value-nya berupa dictionary yang memuat atribut `"nama"`, `"kelas"`, dan `"nilai"`.

## Cara Menjalankan
```bash
python3 praktik/data_mahasiswa.py
```

## Test Case
| Kasus / Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| Pencarian tersedia (`A003`) | Data Citra ditampilkan | Data Citra ditampilkan | Lulus |
| Pencarian tidak tersedia (`A999`) | Pesan 'Data tidak ditemukan' | Pesan 'Data tidak ditemukan' | Lulus |
| Pembaruan nilai (`A002`) | Nilai A002 berubah menjadi 82 | Nilai A002 berubah menjadi 82 | Lulus |
| Penambahan data (`A006`) | Key A006 tersedia setelah ditambahkan | Key A006 tersedia setelah ditambahkan | Lulus |
| Rekap seluruh data (`items()`) | Semua NIM dan data tampil | Semua NIM dan data tampil | Lulus |

## Refleksi
Kesalahan akses key yang sempat ditemukan adalah terjadinya `KeyError` saat mencoba mengakses key secara langsung menggunakan tanda kurung siku (`[]`) tanpa memastikan apakah key tersebut tersedia di dalam dictionary. Hal ini diperbaiki dengan menggunakan method `.get()` serta melakukan pengecekan menggunakan operator `in` agar program dapat berjalan dengan aman.
