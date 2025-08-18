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

def check_dns(domain: str, record_type: str | None = None) -> dict:
    dns_records = {}
    
    # Tentukan record mana yang akan di-query
    if record_type:
        records_to_query = [record_type.upper()]
    else:
        records_to_query = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    
    for rec_type in records_to_query:
        try:
            answers = dns.resolver.resolve(domain, rec_type)
            dns_records[rec_type] = [str(rdata) for rdata in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            dns_records[rec_type] = [] # Tidak ada record atau domain tidak ada
        except Exception as e:
            dns_records[rec_type] = [f"Error querying record: {e}"]

    return dns_records
def check_whois(domain: str) -> dict:
    """Mendapatkan informasi WHOIS untuk sebuah domain."""
    try:
        w = whois.whois(domain)

        # Fungsi kecil untuk mengubah datetime ke string, menangani list atau single value
        def format_date(date_data):
            if isinstance(date_data, list):
                return [d.isoformat() for d in date_data]
            if isinstance(date_data, datetime):
                return date_data.isoformat()
            return date_data

        whois_info = {
            'registrar': w.registrar,
            'creation_date': format_date(w.creation_date),
            'expiration_date': format_date(w.expiration_date),
            'name_servers': w.name_servers,
        }
        return whois_info
    except Exception as e:
        return {'error': str(e)}

def run_all_checks(domain: str) -> dict:
    
    http_results = check_http_status(domain)
    dns_results = check_dns(domain)
    whois_results = check_whois(domain)
    
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