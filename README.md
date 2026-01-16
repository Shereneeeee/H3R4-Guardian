# H3R4-Guardian
auto moderation on discord with python

[H̶3̶R̶4̶ E̶x̶e̶c̶u̶t̶i̶v̶e̶.][DOCUMENTATION UPGRADE: H3R4 OMNIPOTENT V19.0]Status: README OPTIMIZED | PROFESSIONAL GRADE | USER-CENTRIC.Operator, # 🛡️ H3R4 OMNIPOTENT V19.0 (PRO)
> **Advanced Discord Moderation Kernel with Real-Time Interactive Terminal GUI.**

[![Version](https://img.shields.io/badge/Version-20.0-red.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

---

## 🌟 Fitur Utama (Features)

H3R4 OMNIPOTENT bukan sekadar bot biasa. Ini adalah sistem kernel yang berjalan dengan efisiensi tinggi dan antarmuka interaktif.

### 1. **Interactive Management Panel**
Tidak perlu mengedit file kode (`.py`) untuk memasukkan Token atau ID Role. Bot dilengkapi dengan panel menu saat pertama kali dijalankan (Opsi 1-5).

### 2. **Real-Time Live Logger**
Setiap aktivitas di server Discord lu (Kick, Ban, Sensor, Command) akan tercatat secara instan di terminal dengan tampilan visual yang estetik menggunakan library `Rich`.

### 3. **Smart Security Sensor**
Sistem filter kata kasar (Blacklist) yang cerdas. Bot akan otomatis menghapus pesan toxic dan melewati (bypass) pemeriksaan jika pengirim pesan adalah Admin atau Moderator.

### 4. **Dynamic Auto-Response**
Lu bisa nambahin jawaban otomatis bot langsung dari dalam Discord menggunakan command `?addresp`. Sangat berguna untuk FAQ atau sambutan otomatis.

### 5. **Emergency Lockdown**
Perintah `?emergency` akan mengunci seluruh channel di server dalam hitungan detik untuk mencegah serangan raid atau spam massal.

---


?help,-,Membuka pusat bantuan visual H3R4,                                    Semua Member
?ping,-,Cek kecepatan respon (latensi) bot,                                   Semua Member
?uptime,-,Melihat berapa lama bot sudah aktif,                                Semua Member
?userinfo,@user,Mengambil intel detail akun member,                           Semua Member
?kick,@user [alasan],Mengeluarkan member dari server,                           Moderator
?ban,@user [alasan],Blokir member permanen dari server,                         Moderator
?purge,[jumlah],Menghapus pesan secara massal (max 100),                        Moderator
?lock,-,Mengunci channel agar member tidak bisa chat,                           Moderator
?unlock,-,Membuka kembali channel yang terkunci,                                Moderator
?addword,[kata],Menambah kata kasar ke daftar sensor,                         Administrator
?addresp,[pemicu]|[respon],Set jawaban otomatis (pake pemisah |),             Administrator
?emergency,-,Lockdown Global: Kunci seluruh channel,                          Administrator
?unemergency,-,Membuka kembali seluruh server,                                Administrator

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

