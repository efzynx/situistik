# checker.py

import requests
import dns.resolver
import whois
from datetime import datetime

def check_http_status(domain: str) -> dict:
    """Memeriksa status HTTP/HTTPS dan ketersediaan domain."""
    results = {
        'up': False,
        'status_code': None,
        'reason': '',
        'url': ''
    }
    # Coba dengan HTTPS terlebih dahulu (standar modern)
    try:
        url = f"https://{domain}"
        response = requests.get(url, timeout=10, allow_redirects=True, headers={'User-Agent': 'MyCheckerApp/1.0'})
        results.update({
            'up': 200 <= response.status_code < 400,
            'status_code': response.status_code,
            'reason': response.reason,
            'url': response.url
        })
        return results
    except requests.exceptions.RequestException as e:
        # Jika HTTPS gagal, coba dengan HTTP sebagai fallback
        try:
            url = f"http://{domain}"
            response = requests.get(url, timeout=10, allow_redirects=True, headers={'User-Agent': 'MyCheckerApp/1.0'})
            results.update({
                'up': 200 <= response.status_code < 400,
                'status_code': response.status_code,
                'reason': response.reason,
                'url': response.url
            })
            return results
        except requests.exceptions.RequestException as e_http:
            results['reason'] = str(e_http)
            return results

def check_dns(domain: str) -> dict:
    """Mendapatkan record DNS umum untuk sebuah domain."""
    dns_records = {}
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            dns_records[record_type] = [str(rdata) for rdata in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            dns_records[record_type] = [] # Tidak ada record atau domain tidak ada
        except Exception:
            dns_records[record_type] = ["Error querying record."]

    return dns_records

def check_whois(domain: str) -> dict:
    """Mendapatkan informasi WHOIS untuk sebuah domain."""
    try:
        w = whois.whois(domain)
        # Ubah objek datetime menjadi string agar mudah diproses (JSON serializable)
        whois_info = {
            'registrar': w.registrar,
            'creation_date': w.creation_date.isoformat() if isinstance(w.creation_date, datetime) else w.creation_date,
            'expiration_date': w.expiration_date.isoformat() if isinstance(w.expiration_date, datetime) else w.expiration_date,
            'name_servers': w.name_servers,
        }
        return whois_info
    except Exception as e:
        return {'error': str(e)}

def run_all_checks(domain: str) -> dict:
    """Fungsi utama untuk menjalankan semua pengecekan."""
    print(f"Memulai analisis untuk domain: {domain}...")
    
    http_results = check_http_status(domain)
    dns_results = check_dns(domain)
    whois_results = check_whois(domain)
    
    print("Analisis selesai.")
    
    # Gabungkan semua hasil ke dalam satu dictionary besar
    final_results = {
        'domain': domain,
        'checked_at': datetime.now().isoformat(),
        'status_check': http_results,
        'dns_records': dns_results,
        'whois_info': whois_results
    }
    
    return final_results

# Bagian ini hanya akan berjalan jika file ini dieksekusi secara langsung
# Sangat berguna untuk melakukan tes cepat
if __name__ == "__main__":
    from pprint import pprint
    
    test_domain = "google.com"
    results = run_all_checks(test_domain)
    
    print("\n--- HASIL ANALISIS LENGKAP ---")
    pprint(results)