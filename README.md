🚀 Shopee Flash Sale Sniper (Hybrid Version)
Bot ini dirancang untuk membantu memenangkan war flash sale Shopee dengan kecepatan tinggi menggunakan Playwright. Menggunakan metode Hybrid, bot menangani kecepatan klik di awal, sementara user bisa bersiap melakukan verifikasi manual di HP/Browser jika terdeteksi sistem keamanan.

🛠️ Persiapan Awal (Prasyarat)
Sebelum menjalankan bot, pastikan perangkat Anda sudah terpasang:

Python 3.10+: Download di sini

Google Chrome: Pastikan Chrome sudah terinstall di lokasi default.

VS Code: Untuk mengedit script dengan mudah.

Instalasi Library
Buka Terminal/CMD, masuk ke folder project, lalu jalankan:

Bash
pip install playwright playwright-stealth python-dotenv
playwright install chromium
⚙️ Konfigurasi File
1. File .env
Edit file .env untuk menentukan target. Pastikan format URL benar:

Cuplikan kode
TARGET_URL=https://shopee.co.id/product/255563049/23157471408
SALE_TIME=20:00:00
CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe
2. File requirements.txt
Pastikan isinya sudah sesuai:

Plaintext
playwright
playwright-stealth
python-dotenv
🚀 Cara Menjalankan Bot
Langkah 1: Membuka Chrome via Debug Mode
Bot ini tidak login otomatis (untuk menghindari blokir), melainkan menempel pada sesi Chrome yang sudah ada.

Tutup semua jendela Chrome yang sedang berjalan.

Buka CMD, masuk ke direktori project (Misal: D:\shopee_bot).

Jalankan perintah ini untuk membuka Chrome khusus:

Bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="D:\shopee_bot\user_data"

   *Note: Perintah ini akan membuat folder `user_data` di folder project. Folder ini menyimpan data login Anda.*

### Langkah 2: Login & Standby Produk
1. Di jendela Chrome yang baru terbuka, buka [Shopee](https://shopee.co.id) dan **Login** secara manual.
2. Buka link produk target (yang ada di `.env`).
3. **PENTING:** Klik manual varian produk (Warna/Ukuran) dan pastikan varian sudah terpilih (kotak menjadi orange). **Standby saja di laman tersebut.**

### Langkah 3: Menjalankan Script Sniper
1. Kembali ke VS Code atau CMD baru (pastikan tetap di folder project).
2. Jalankan bot dengan perintah:
   ```bash
   python main.py
Bot akan memantau waktu secara real-time (cek setiap 0.01 detik). Begitu waktu menyentuh SALE_TIME, bot akan otomatis mengklik tombol "Beli Dengan Voucher" atau "Beli Sekarang".

💡 Tips & Trik Penting
Taktik Hybrid: Jika bot berhasil klik Checkout namun muncul perintah "Lanjutkan di Aplikasi", segera buka aplikasi Shopee di HP Anda, masuk ke menu Keranjang atau Pesanan Saya, dan selesaikan pembayaran di sana.

Verifikasi Manual: Jika di tengah proses muncul Captcha/Verifikasi, jangan panik. Segera selesaikan verifikasi secara manual di browser tersebut agar sistem menganggap aktivitas dilakukan oleh manusia, lalu jalankan ulang bot jika perlu.

Ganti Akun: Jika ingin menggunakan akun lain, hapus folder user_data di dalam direktori project, lalu ulangi proses Login dari awal.

Folder Lokasi: Cara cepat buka CMD di folder: Masuk ke folder D:\shopee_bot, klik pada address bar di atas, hapus isinya, ketik cmd, lalu tekan Enter.

⚠️ Disclaimer
Script ini dibuat untuk tujuan pembelajaran (educational purposes). Penggunaan bot untuk memanipulasi sistem transaksi dapat melanggar Syarat & Ketentuan pihak ketiga. Risiko akun dibatasi atau pesanan dibatalkan ditanggung sepenuhnya oleh pengguna.
