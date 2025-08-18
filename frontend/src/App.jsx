// src/App.jsx

import { useState } from 'react';
import axios from 'axios';
// Hapus import App.css karena sudah tidak kita gunakan
// import './App.css'

// URL base dari API FastAPI kita. Pastikan backend sedang berjalan!
const API_BASE_URL = 'http://127.0.0.1:8000';

function App() {
  // State untuk menyimpan input domain dari pengguna
  const [domain, setDomain] = useState('');
  
  // State untuk menyimpan hasil gabungan dari API
  const [results, setResults] = useState(null);
  
  // State untuk menandakan proses loading (saat fetching data)
  const [loading, setLoading] = useState(false);
  
  // State untuk menyimpan pesan error jika terjadi
  const [error, setError] = useState('');

  // Fungsi yang akan dijalankan saat form disubmit
  const handleAnalyze = async (e) => {
    e.preventDefault(); // Mencegah form dari refresh halaman
    if (!domain) {
      setError('Nama domain tidak boleh kosong.');
      return;
    }

    // Reset state sebelum memulai analisis baru
    setLoading(true);
    setResults(null);
    setError('');

    try {
      // Kita panggil semua endpoint secara paralel untuk efisiensi!
      const [statusRes, whoisRes, dnsRes] = await Promise.all([
        axios.get(`${API_BASE_URL}/status/${domain}`),
        axios.get(`${API_BASE_URL}/whois/${domain}`),
        axios.get(`${API_BASE_URL}/dns/${domain}`)
      ]);
      
      // Gabungkan semua hasil menjadi satu objek
      setResults({
        status: statusRes.data,
        whois: whoisRes.data,
        dns: dnsRes.data
      });

    } catch (err) {
      console.error("API Fetch Error:", err);
      setError('Gagal mengambil data. Pastikan domain valid dan API server backend berjalan.');
    } finally {
      // Apapun hasilnya (sukses/gagal), hentikan loading
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Situistik 🕵️</h1>
      <p>Analisis Status, Whois, dan DNS untuk Domain Anda</p>
      
      <form onSubmit={handleAnalyze}>
        <input
          type="text"
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
          placeholder="Contoh: google.com"
          disabled={loading}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Menganalisis...' : 'Analisis'}
        </button>
      </form>

      {/* Tampilkan pesan error jika ada */}
      {error && <p className="error">{error}</p>}

      {/* Tampilkan hasil jika sudah ada */}
      {results && (
        <div className="results">
          <h2>Hasil untuk: {domain}</h2>
          
          <h3>Status Website</h3>
          <pre>{JSON.stringify(results.status, null, 2)}</pre>

          <h3>Informasi Whois</h3>
          <pre>{JSON.stringify(results.whois, null, 2)}</pre>
          
          <h3>Record DNS</h3>
          <pre>{JSON.stringify(results.dns, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;