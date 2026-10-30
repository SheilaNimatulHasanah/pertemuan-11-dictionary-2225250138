def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM dengan aman."""
    return data.get(nim)

def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa."""
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# Inisialisasi dictionary data mahasiswa dengan NIM sebagai key utama
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== PENGUJIAN PENCARIAN (TEST CASE) ===")
# Test Case 1: Pencarian tersedia (A003)
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)
if hasil is not None:
    print(f"Pencarian '{nim_cari}': Data {hasil['nama']} ditampilkan -> {hasil}")
else:
    print(f"Pencarian '{nim_cari}': Data tidak ditemukan")

# Test Case 2: Pencarian tidak tersedia (A999)
nim_tidak_ada = "A999"
hasil_tdk = cari_mahasiswa(data_mahasiswa, nim_tidak_ada)
if hasil_tdk is not None:
    print(f"Pencarian '{nim_tidak_ada}': {hasil_tdk}")
else:
    print(f"Pencarian '{nim_tidak_ada}': Pesan 'Data tidak ditemukan'")

print("\n=== PEMBARUAN & PENAMBAHAN DATA ===")
# Test Case 3: Penambahan data mahasiswa baru (A006)
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}
print("Key A006 berhasil ditambahkan:", "A006" in data_mahasiswa)

# Test Case 4: Pembaruan nilai mahasiswa tertentu (A002 menjadi 82)
if "A002" in data_mahasiswa:
    data_mahasiswa["A002"]["nilai"] = 82
    print(f"Nilai A002 ({data_mahasiswa['A002']['nama']}) diperbarui menjadi: {data_mahasiswa['A002']['nilai']}")

print("\n=== REKAP SELURUH DATA & RATA-RATA (ITEMS) ===")
# Test Case 5: Menampilkan seluruh data menggunakan items()
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")

# Menghitung rata-rata kelas
rata_kelas = rata_rata_nilai(data_mahasiswa)
print(f"\nRata-rata nilai kelas = {rata_kelas:.2f}")