Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input 
NIM, nilai.

## Cara Menjalankan
```bash
python3 tugas/rekap_nilai_file.py
```

## Error yang Ditangani
* `FileNotFoundError`: Ditangani ketika file `data/nilai.txt` tidak ditemukan agar program tidak *crash*.
* `ValueError`: Ditangani ketika data nilai pada baris tertentu berupa teks atau tidak valid sehingga baris tersebut dilewati tanpa menghentikan proses keseluruhan.

## Test Case
| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| Normal (Semua baris valid) | Semua record diproses dan rekap benar | Semua record diproses dan rekap benar | Lulus |
| File hilang (`nilai.txt` tidak ada) | Pesan file tidak ditemukan; program tidak *crash* | Pesan file tidak ditemukan; program tidak *crash* | Lulus |
| Nilai invalid (`A004,abc`) | Baris invalid dilewati/dilaporkan; record lain tetap diproses | Baris invalid dilewati/dilaporkan; record lain tetap diproses | Lulus |
| Baris kosong | Baris kosong dilewati | Baris kosong dilewati | Lulus |
| Batas lulus (Nilai 60) | Dihitung sebagai lulus | Dihitung sebagai lulus | Lulus | 

## Refleksi
Kesalahan penanganan error yang sempat diantisipasi adalah mencegah program berhenti secara total ketika mendapati format baris atau nilai teks yang salah (`ValueError`), sehingga baris data yang valid tetap dapat dihitung dengan akurat.
