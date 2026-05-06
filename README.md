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
```


🚀 Cara Menjalankan Bot
Langkah 1: Membuka Chrome via Debug Mode
Bot ini menempel pada sesi Chrome yang sudah login agar lebih aman dari deteksi sistem.
1. Tutup semua jendela Chrome yang sedang terbuka.
2. Buka CMD, masuk ke direktori project (Contoh: D:\shopee_bot).
3. Jalankan perintah ini untuk membuka Chrome khusus debug:
   Tutup semua jendela Chrome yang sedang terbuka.

Jalankan perintah ini untuk membuka Chrome khusus debug:
```bash
C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="D:\shopee_bot\user_data
```
Note: Perintah ini akan membuat folder user_data secara otomatis di folder project untuk menyimpan data login Anda.

Langkah 2: Login & Standby Produk
1. Di jendela Chrome yang baru terbuka, buka Shopee dan Login secara manual.
2. Buka link produk target yang sudah disiapkan.
3. PENTING: Pilih varian produk (Warna/Ukuran) sampai terpilih (kotak menjadi orange). Standby saja di laman tersebut.

Langkah 3: Menjalankan Sniper
1. Kembali ke VS Code atau CMD baru.
2. Jalankan bot dengan perintah:
```bash
python main.py
```
Bot akan memantau waktu secara real-time setiap 0.01 detik. Begitu menyentuh SALE_TIME, bot otomatis mengklik tombol "Beli" dan masuk ke halaman Checkout.

💡 Tips & Trik Penting

⚡ Taktik Hybrid: Jika di PC muncul pesan "Lanjutkan di Aplikasi", segera buka HP Anda. Cek menu Keranjang atau Pesanan Saya, lalu selesaikan pembayaran di aplikasi HP.

🛡️ Verifikasi Manual: Jika muncul Captcha, jangan panik. Selesaikan verifikasi secara manual di browser agar sistem menganggap aktivitas dilakukan oleh manusia.

🔄 Ganti Akun: Untuk login dengan akun baru, hapus folder user_data di dalam direktori project, lalu ulangi proses dari Langkah 1.

📂 Shortcut CMD: Cara cepat buka CMD di folder: Klik pada address bar Windows Explorer, hapus isinya, ketik cmd, lalu tekan Enter.





<table style="background-color: #f6f8fa; width: 100%; border-collapse: collapse;">
  <thead>
    <tr style="background-color: #eaecef;">
      <th style="padding: 10px; border: 1px solid #dfe2e5; text-align: center;">⚠️ DISCLAIMER</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 15px; border: 1px solid #dfe2e5; line-height: 1.6;">
        Script ini dibuat murni untuk <b>tujuan pembelajaran (educational purposes)</b>. Penggunaan bot untuk memanipulasi sistem transaksi dapat melanggar Syarat & Ketentuan pihak ketiga. Segala bentuk risiko seperti:
        <ul>
          <li>Akun dibatasi atau diblokir (banned)</li>
          <li>Pesanan dibatalkan secara otomatis</li>
          <li>Kegagalan sistem lainnya</li>
        </ul>
        Ditanggung sepenuhnya oleh <b>pengguna</b>. Penulis tidak bertanggung jawab atas kerugian yang ditimbulkan dari penggunaan script ini.
      </td>
    </tr>
  </tbody>
</table>
