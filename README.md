# H3R4-Guardian
auto moderation on discord with python

[H̶3̶R̶4̶ E̶x̶e̶c̶u̶t̶i̶v̶e̶.][DOCUMENTATION UPGRADE: H3R4 OMNIPOTENT V20.0]Status: README OPTIMIZED | PROFESSIONAL GRADE | USER-CENTRIC.Operator, gue udah buatkan file README.md yang sangat detail. Penjelasan fiturnya gue buat scannable (mudah dibaca cepat) dan panduan setup-nya gue pecah jadi langkah-langkah teknis yang gak bakal bikin bingung, bahkan buat pemula sekalipun.FILE: README.mdCopy seluruh blok teks di bawah ini dan simpan sebagai README.md di folder repository lu.Markdown# 🛡️ H3R4 OMNIPOTENT V19.0 (PRO)
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
