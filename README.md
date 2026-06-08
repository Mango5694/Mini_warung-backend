# Mini-Warung Inventory System (CLI Based)

Aplikasi manajemen inventaris sederhana berbasis **Command Line Interface (CLI)** yang dirancang untuk membantu pemilik toko kecil mengelola stok barang secara digital. Proyek ini memfokuskan pada efisiensi logika backend dan integritas data.

## 🚀 Fitur Utama
- **Sistem Menu Interaktif**: Navigasi menggunakan sistem "Gateway" (if-elif-else) yang memungkinkan pengguna memilih fitur tanpa harus mengulang program dari awal.
- **Operasi CRUD Lengkap**: 
  - **Create**: Menambah barang baru ke stok.
  - **Read**: Menampilkan daftar seluruh stok barang dengan format yang rapi.
  - **Delete**: Menghapus barang yang sudah habis terjual.
- **Data Persistence**: Menggunakan sistem *File Handling* (.txt) agar data tetap tersimpan secara permanen meskipun aplikasi ditutup.
- **User-Friendly Error Handling**: Implementasi `try-except` untuk mencegah aplikasi crash jika pengguna salah memasukkan input.
- **Data Sanitization**: Dilengkapi fungsi `.strip()` dan `.lower()` untuk memastikan data yang masuk bersih dari spasi liar dan tidak ada duplikasi akibat perbedaan huruf kapital.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Storage**: Flat File Database (.txt)
- **Logic Concepts**: 
  - Modular Programming (Functions/def)
  - Global Variable Scope
  - Infinite Loops with Sub-menu breaks
  - List Comprehension (for data validation)

## 📖 Cara Menjalankan
1. Pastikan Anda memiliki Python 3 terinstal di perangkat Anda.
2. Clone repository ini atau unduh file `main.py`.
3. Jalankan melalui terminal/console:
   ```bash
   python main.py
