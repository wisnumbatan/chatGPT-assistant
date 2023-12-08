# chatgpt-voice-assistant

Pastikan Anda menggunakan Python versi 3.6 atau yang lebih baru. Untuk memeriksanya, jalankan perintah berikut di terminal Anda: python --version

Instal dependensi berikut:
pip install openai python-dotenv speechrecognition pyttsx3 numpy pyaudio

Masukan dan keluaran dari skrip ini didasarkan pada perangkat audio default Anda. (Periksa / ubah ini dalam pengaturan Anda jika menggunakan Windows)
Periksa / Ubah perangkat audio default di Raspberry Pi:
Jalankan sudo raspi-config
Gunakan tombol panah untuk navigasi melalui opsi. Pergi ke -> sistem -> audio -> pilih output audio yang Anda inginkan (jika tidak yakin, gunakan output audio 0)

Untuk masukan audio:
Untuk membuat Raspberry Pi mendengarkan mikrofon Anda sebagai masukan, Anda dapat mengikuti langkah-langkah ini:

Pertama, hubungkan perangkat mikrofon Anda ke Raspberry Pi dan pastikan bahwa perangkat tersebut dikenali oleh sistem. Anda dapat melakukannya dengan menjalankan perintah berikut di terminal:
lsusb
Perintah ini akan menampilkan semua perangkat USB yang terhubung ke Raspberry Pi Anda. Cari mikrofon Anda dalam daftar tersebut.
Selanjutnya, Anda perlu menginstal paket-paket yang diperlukan untuk bekerja dengan audio. Anda dapat melakukannya dengan menjalankan perintah berikut di terminal:
sudo apt-get install alsa-utils
Perintah ini akan menginstal utilitas ALSA (Advanced Linux Sound Architecture), yang digunakan untuk mengonfigurasi audio pada sistem Linux.
Setelah paket terinstal, Anda dapat memeriksa apakah mikrofon Anda dikenali oleh sistem dengan menjalankan perintah berikut:
arecord -l
Ingatlah nomor untuk perangkat audio yang Anda pilih. (dimulai dengan "card")
Perintah ini akan menampilkan semua perangkat audio yang terhubung ke Raspberry Pi Anda. Cari mikrofon webcam Anda dalam daftar tersebut.
Jika mikrofon Anda dikenali oleh sistem, Anda dapat mengaturnya sebagai perangkat audio masukan default dengan mengedit file konfigurasi ALSA. Untuk melakukannya, jalankan perintah berikut:
sudo nano /usr/share/alsa/alsa.conf
Perintah ini akan membuka file konfigurasi ALSA di editor teks Nano.
Di dalam file konfigurasi, cari baris-baris berikut:
; defaults.ctl.card 0
; defaults.pcm.card 0
Hapus tanda semikolon pada awal setiap baris, dan ubah nilai dari 0 menjadi nomor webcam mikrofon Anda. Misalnya, jika mikrofon webcam Anda terdaftar sebagai "card 1" dalam keluaran perintah arecord -l, Anda harus mengubah baris-baris tersebut menjadi:
defaults.ctl.card 1
defaults.pcm.card 1
Simpan perubahan pada file konfigurasi dengan menekan Ctrl+O, kemudian keluar dari editor teks dengan menekan Ctrl+X.
Terakhir, Anda dapat menguji mikrofon Anda dengan menjalankan perintah berikut:
arecord -f cd -D hw:1 | aplay
Perintah ini akan merekam audio dari mikrofon Anda dan memutarnya melalui perangkat audio output default. Jika Anda mendengar suara, itu berarti bahwa mikrofon Anda berfungsi dengan baik.

Pada suatu titik dalam proses ini, Anda mungkin mengalami kesalahan libespeak di Raspberry Pi. Menjalankan perintah berikut di terminal seharusnya memperbaikinya sudo apt-get install libespeak1.

Selamat! Cobalah menjalankan skripnya dengan menavigasi ke folder proyek melalui cd nama_folder lalu jalankan python main.py