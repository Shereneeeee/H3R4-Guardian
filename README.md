
🛡️ H3R4 OMNIPOTENT KERNEL V25.0
Supreme Titan Edition - Sebuah sistem manajemen dan perlindungan Discord tingkat lanjut dengan integrasi Terminal GUI (TUI) real-time.

🚀 Ikhtisar (Overview)
H3R4 OMNIPOTENT KERNEL adalah bot Discord berbasis Python yang dirancang untuk stabilitas tinggi dan kontrol penuh melalui terminal. Menggunakan library Rich, bot ini menampilkan dashboard interaktif langsung di console Anda, memantau log aktivitas, latensi, dan status sistem secara real-time.


✨ Fitur Utama
🛡️ Advanced Protection: Sistem Global Lockdown (Emergency mode) untuk mengunci seluruh channel secara instan.

⚖️ Smart Moderation: Sistem Strike otomatis (3 kali pelanggaran = Auto Mute), Purge pesan, Kick, dan Ban.

📊 Real-Time GUI: Dashboard terminal yang indah dengan Live Logs, indikator Uptime, dan Latency Guard.

⚙️ Dynamic Database: Konfigurasi tersimpan secara lokal dalam h3r4_guardian_config.json.

🤖 Auto-Response: Sistem respon otomatis berbasis kata kunci yang dapat dikonfigurasi langsung dari Discord.
---

🛡️ PROTECTION PROTOCOLS

?emergency — Lockdown Global! Mengunci semua channel di server sekaligus. (Admin Only)

?unemergency — Memulihkan seluruh channel server ke keadaan semula. (Admin Only)

?lock — Mengunci channel yang sedang digunakan saja. (Staff Only)

?unlock — Membuka kembali channel yang sedang dikunci. (Staff Only)

⚖️ MODERATION SYSTEM
?kick @user [alasan] — Mengeluarkan member dari server dengan catatan.

?ban @user [alasan] — Memblokir member secara permanen dari server.

?purge [jumlah] — Menghapus pesan dalam jumlah banyak secara instan.

🤖 AUTOMATION & DATABASE

?addword [kata] — Menambahkan kata baru ke dalam daftar sensor otomatis.

?listword — Menampilkan semua kata yang saat ini disensor oleh bot.

?addresp [pemicu] | [jawaban] — Membuat respon otomatis (Gunakan tanda | sebagai pemisah).

?delresp [pemicu] — Menghapus respon otomatis yang sudah ada.

🔍 INFORMATION & INTEL

?help — Membuka menu pusat bantuan H3R4 OMNIPOTENT.

?userinfo @user — Menampilkan detail intelijen akun (ID, Tanggal Join, dll).

?ping — Mengecek kecepatan koneksi bot ke server Discord.

?uptime — Melihat durasi sistem telah berjalan tanpa restart.

💡 CARA PENGGUNAAN CEPAT:

Sensor Kata: Ketik ?addword anjing -> Maka setiap member (non-mod) yang ketik kata itu pesannya akan dihapus.

Balas Otomatis: Ketik ?addresp halo | halo juga user! -> Bot akan otomatis membalas setiap ada yang ketik 'halo'.

Bersih Chat: Ketik ?purge 20 -> 20 pesan terakhir akan langsung hilang.


## 🛠️ Panduan Setup (Setup Guide)

Ikuti langkah-langkah di bawah ini untuk mengaktifkan bot di PC, VPS, atau Termux.

### **Langkah 1: Persiapan (Prerequisites)**
Pastikan lu udah install Python 3.8 ke atas.
```bash

##Langkah 2: Clone & Install Library
Copy repository ini dan install library pendukung yang dibutuhkan (discord.py & rich).

Bash

git clone https://github.com/Shereneeeee/H3R4-Guardian
cd H3R4-Guardian
pip install -r requirements.txt

langkah 3:


python main.py

2. Input Token Bot (Opsi 1)
Bot akan memunculkan Management Panel.

Ketik 1 lalu tekan Enter.

Paste Token Bot lu (Token ini didapat dari Discord Developer Portal).

Note: Token akan tersimpan otomatis di config_h3r4.json.

3. Input Mod Role ID (Opsi 2)
Ketik 2 lalu tekan Enter.

Paste ID Role Moderator server lu. Ini supaya lu dan staff lu TIDAK kena sensor otomatis pas ngetik kata kasar.

Cara ambil ID: Aktifkan 'Developer Mode' di Discord -> Klik kanan Role-nya -> Copy ID.

4. Launching (Opsi 4)
Ketik 4 lalu tekan Enter.

Tunggu sampai layar terminal berubah menjadi Live Activity Log dengan banner merah H3R4.

Jika muncul log [SYSTEM] Authorized as NameBot#1234, artinya bot sudah Online.

5. Verifikasi di Discord
Masuk ke server Discord lu.

Ketik ?help.

Jika bot mengirimkan Embed Red Menu, maka kalibrasi berhasil 100%.

