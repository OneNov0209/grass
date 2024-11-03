# Grass Bot

Grass Bot adalah aplikasi yang dirancang untuk terhubung ke layanan Grass melalui WebSocket. Aplikasi ini menggunakan Python dan beberapa pustaka untuk mengelola koneksi dan logika bot.

## Daftar Isi

- [Fitur](#fitur)
- [Persyaratan](#persyaratan)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## Fitur

- Koneksi ke WebSocket menggunakan IP VPS.
- Pengiriman dan penerimaan pesan secara real-time.
- Logika dasar untuk mengelola otentikasi dan komunikasi dengan layanan.

## Persyaratan

Pastikan Anda memiliki hal berikut sebelum memulai:

- Python 3.7 atau lebih baru.
- Akses internet.
- VPS dengan IP publik.

## Instalasi

Ikuti langkah-langkah di bawah ini untuk menginstal Grass Bot:

1. **Kloning repositori:**
   ```bash
   git clone https://github.com/OneNov0209/grass.git
   cd grass
   ```

 2. ***install requirements***
  ```bash
pip install -r requirements.txt
```
```
pip install python-dotenv
```

3. **Buat file .env:**
```bash
sudo nano .env
```
isi dengan Id grass, url aplikasi dasboard dan Ip Vps anda, Dengan format seperti dibawah:

USER_ID=

ORIGIN_URL=https://app.getgrass.io/

DEVICE_IP=

4. **Buat layanan systemd**
```bash
sudo nano /etc/systemd/system/grassbot.service
```
5. ***Tambahahkan script ini***:
```
[Unit]
Description=Grass Bot Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /root/grass/localgrassnode.py
WorkingDirectory=/root/grass
User=root
Restart=always

[Install]
WantedBy=multi-user.target
````
ctrl x y etener

6. ***Aktifkan layanan**
```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl enable grassbot.service
```
```bash
sudo systemctl start grassbot.service
```
7. ***Cek statsus***
```bash
sudo systemctl status grassbot.service
```
8. ***cek logs**
```bash
sudo journalctl -u grassbot.service -f -o cat
```

### Register ###
Link: https://app.getgrass.io/register/?referralCode=MLsBtbbiLMvTPWA

download Ekstensi aplikasi: https://chrome.google.com/webstore/detail/grass-extension/ilehaonighjijnmpnagapkhpcdbhclfg?hl=en&authuser=0
