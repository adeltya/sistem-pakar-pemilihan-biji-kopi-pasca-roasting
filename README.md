# Siko: Sistem Pakar Pemilihan Biji Kopi Pasca Roasting

Aplikasi web Sistem Pakar ini dirancang untuk melakukan klasifikasi kelayakan biji kopi pasca roasting menggunakan metode **Forward Chaining**. Proyek ini dibuat berdasarkan penelitian yang berjudul *"Sistem Pakar Pemilihan Biji Kopi Pasca Roasting untuk Menghasilkan Kopi Berkualitas Menggunakan Metode Forward Chaining"*.

Aplikasi ini mendeteksi 3 jenis kopi utama (Arabika, Robusta, Liberika) dan mengategorikannya menjadi **Berkualitas** atau **Memiliki Cacat (Defect)** berdasarkan 17 ciri fisik, aroma, dan kadar kafein yang teramati.

---

## Fitur Utama

1. **🔍 Konsultasi Pakar (Wizard Interaktif)**: Mengarahkan pengguna langkah demi langkah dalam menjawab pertanyaan ciri fisik kopi berdasarkan pohon keputusan (*decision tree*).
2. **📋 Simulator Forward Chaining & Aturan**: Memungkinkan pengguna memilih ciri secara bebas (checklist) dan menampilkan proses inferensi rules satu per satu secara visual (*trace log*).
3. **📖 Ensiklopedia Kopi**: Informasi edukasi mengenai karakteristik mendalam tentang kopi Arabika, Robusta, dan Liberika.
4. **🕒 Riwayat Tes Sesi**: Menyimpan riwayat klasifikasi kopi yang telah dilakukan dalam satu sesi penggunaan aplikasi.
5. **🎨 Desain Premium Bertema Kopi**: Antarmuka responsif bernuansa kopi hangat dengan efek transisi halus.

---

## Struktur Folder Proyek

```text
C:\Users\Adeltya\sistem_pakar_kopi\
├── app.py              # Kode logika utama Streamlit & Forward Chaining
├── style.css           # Desain tema kustom (Coffee Espresso Dark Mode)
├── requirements.txt    # Daftar dependensi modul Python
└── README.md           # Dokumen panduan penggunaan ini
```

---

## Persyaratan Awal (Prerequisites)

Pastikan komputer Anda sudah terinstal **Python 3.8** atau versi di atasnya.

---

## Cara Menjalankan Aplikasi

Ikuti langkah-langkah mudah berikut di Command Prompt (cmd) atau PowerShell Anda:

### 1. Buka Terminal di Direktori Proyek
Buka Command Prompt atau PowerShell, lalu arahkan ke folder proyek ini:
```bash
cd C:\Users\Adeltya\sistem_pakar_kopi
```

### 2. Pasang Dependensi (Streamlit)
Jalankan perintah berikut untuk menginstal package Streamlit yang dibutuhkan:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Server Streamlit
Jalankan aplikasi dengan perintah:
```bash
streamlit run app.py
```

### 4. Buka Aplikasi di Browser
Setelah menjalankan perintah di atas, server lokal akan aktif dan otomatis membuka peramban web Anda ke alamat:
* **Local URL**: `http://localhost:8501`

Jika tidak terbuka secara otomatis, silakan salin alamat di atas ke browser Anda.

---

## Aturan Sistem Pakar (6 Kaidah Produksi)

Berikut adalah ringkasan basis pengetahuan aturan keputusan yang tertanam dalam program:
* **Rule 1 (Arabika Berkualitas)**: C01 $\land$ C02 $\land$ C03 $\land$ C04 $\land$ C05 $\rightarrow$ J01
* **Rule 2 (Robusta Berkualitas)**: C06 $\land$ C07 $\land$ C08 $\land$ C09 $\land$ C10 $\rightarrow$ J02
* **Rule 3 (Liberika Berkualitas)**: C11 $\land$ C12 $\land$ C13 $\land$ C14 $\rightarrow$ J03
* **Rule 4 (Arabika Cacat)**: C01 $\land$ C02 $\land$ C03 $\land$ C04 $\land$ (C15 $\lor$ C16 $\lor$ C17) $\rightarrow$ J04
* **Rule 5 (Robusta Cacat)**: C06 $\land$ C07 $\land$ C08 $\land$ C09 $\land$ (C15 $\lor$ C16 $\lor$ C17) $\rightarrow$ J05
* **Rule 6 (Liberika Cacat)**: C11 $\land$ C12 $\land$ C13 $\land$ (C15 $\lor$ C16 $\lor$ C17) $\rightarrow$ J06
