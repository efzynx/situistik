# api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Impor setiap fungsi checker secara individual
from checker import check_http_status, check_dns, check_whois

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title="Situistik API",
    description="API RESTful untuk analisis status, DNS, dan Whois sebuah domain.",
    version="2.0.0" # Naikkan versi karena ada perubahan besar
)

# Middleware CORS (tetap sama)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Selamat datang di Situistik API v2. Lihat dokumentasi di /docs"}


# --- Endpoint Baru yang Terpisah ---

@app.get("/status/{domain}", tags=["Status"])
def get_website_status(domain: str):
    """Memeriksa apakah sebuah website UP atau DOWN."""
    return check_http_status(domain)


@app.get("/whois/{domain}", tags=["Whois"])
def get_whois_info(domain: str):
    """Mendapatkan informasi Whois dari sebuah domain."""
    return check_whois(domain)


@app.get("/dns/{domain}", tags=["DNS"])
def get_all_dns_records(domain: str):
    """Mendapatkan semua record DNS umum (A, AAAA, MX, NS, TXT)."""
    return check_dns(domain) # Memanggil tanpa record_type spesifik


@app.get("/dns/{domain}/{record_type}", tags=["DNS"])
def get_specific_dns_record(domain: str, record_type: str):
    """
    Mendapatkan record DNS untuk tipe spesifik.
    Contoh tipe: A, AAAA, MX, NS, TXT, CNAME, SOA.
    """
    return check_dns(domain, record_type=record_type)