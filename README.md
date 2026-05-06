# 🚀 Shopee Flash Sale Sniper (Hybrid Version)

Bot otomasi berbasis **Python** & **Playwright** yang dirancang khusus untuk memenangkan *war* Flash Sale Shopee (seperti iPhone Rp1.000). Menggunakan metode **Hybrid**: Kecepatan bot untuk eksekusi klik awal, dan jari user untuk eksekusi final/verifikasi.

---

## 🛠️ Persiapan Awal

Pastikan perangkat Anda sudah terpasang komponen berikut:

| Komponen | Deskripsi |
| :--- | :--- |
| **Python 3.10+** | Bahasa pemrograman utama. [Download di sini](https://www.python.org/downloads/) |
| **Google Chrome** | Browser target (Gunakan lokasi instalasi default). |
| **VS Code** | Editor untuk konfigurasi script. |

### 📦 Instalasi Library
Buka Terminal atau CMD, lalu jalankan perintah berikut:
```bash
pip install playwright playwright-stealth python-dotenv
playwright install chromium

---

# 🚀 Cara Menjalankan Bot
Langkah 1: Membuka Chrome via Debug Mode
Bot ini menempel pada sesi Chrome yang sudah login agar lebih aman dari deteksi sistem.

Tutup semua jendela Chrome yang sedang terbuka.

Buka CMD, masuk ke direktori project (Contoh: D:\shopee_bot).

Jalankan perintah ini untuk membuka Chrome khusus debug:
