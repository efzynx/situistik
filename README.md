Situistik 🕵️Alat diagnostik web sederhana untuk memeriksa status, catatan DNS, dan informasi Whois dari sebuah domain. Proyek ini dibangun dengan arsitektur modern yang memisahkan backend (Python/FastAPI) dan frontend (React/Vite).✨ Fitur UtamaPengecekan Status Website: Memverifikasi apakah sebuah domain dapat diakses (UP) atau tidak (DOWN) melalui permintaan HTTP/HTTPS.Pencarian DNS: Mengambil catatan DNS umum seperti A, AAAA, MX, NS, dan TXT.Informasi Whois: Menampilkan data registrasi domain, termasuk registrar, tanggal pembuatan, dan tanggal kedaluwarsa.Antarmuka CLI: Selain antarmuka web, tersedia juga versi Command-Line Interface (CLI) untuk analisis cepat dari terminal.API RESTful: Backend menyediakan API yang terstruktur dan RESTful untuk setiap fitur pengecekan.🛠️ Tumpukan TeknologiProyek ini dibagi menjadi dua komponen utama:Backend (/backend)Bahasa: Python 3Framework API: FastAPIServer: UvicornPustaka Kunci:requests untuk pengecekan HTTP.dnspython untuk query DNS.python-whois untuk mengambil data Whois.typer dan rich untuk antarmuka CLI.Frontend (/frontend)Framework: React.jsBuild Tool: VitePustaka Kunci:axios untuk berkomunikasi dengan backend API.Styling menggunakan CSS murni.🚀 Menjalankan Secara LokalUntuk menjalankan proyek ini di mesin lokal Anda, ikuti langkah-langkah berikut.PrasyaratPython 3.8+Node.js v18+ dan npm1. Kloning Repositorigit clone [https://github.com/efzynx/situistik.git](https://github.com/efzynx/situistik.git)
cd situistik
2. Menjalankan BackendBuka terminal pertama Anda dan jalankan perintah berikut:# Pindah ke direktori backend
cd backend

# Buat dan aktifkan virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Instal semua dependensi Python
pip install -r requirements.txt

# Jalankan server API
uvicorn api:app --reload
Server backend sekarang akan berjalan di http://127.0.0.1:8000.3. Menjalankan FrontendBuka terminal kedua (biarkan terminal backend tetap berjalan) dan jalankan perintah berikut:# Pindah ke direktori frontend dari root proyek
cd frontend

# Instal semua dependensi JavaScript
npm install

# Jalankan server pengembangan
npm run dev
Aplikasi web sekarang dapat diakses di http://localhost:5173.4. (Opsional) Menjalankan CLIJika Anda ingin menggunakan versi CLI, pastikan Anda berada di direktori backend dengan virtual environment yang aktif, lalu jalankan:python cli.py analyze google.com
📂 Struktur Proyeksituistik/
├── backend/        # Semua kode Python (FastAPI, CLI, Logika Inti)
│   ├── .venv/
│   ├── api.py
│   ├── checker.py
│   ├── cli.py
│   └── requirements.txt
└── frontend/       # Semua kode React.js (Vite)
    ├── src/
    ├── package.json
    └── ...
🤝 KontribusiKontribusi, isu, dan permintaan fitur sangat diterima! Jangan ragu untuk membuat pull request atau membuka isu baru.📜 LisensiProyek ini dilisensikan di bawah