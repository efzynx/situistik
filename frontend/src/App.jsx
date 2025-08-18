// src/App.jsx

import { useState } from 'react';
import axios from 'axios';
import './index.css';

// Impor komponen-komponen baru kita
import StatusResult from './components/StatusResult';
import DnsResult from './components/DnsResult';
import WhoisResult from './components/WhoisResult';
import Footer from './components/Footer';

const API_BASE_URL = 'http://127.0.0.1:8000';

function App() {
  const [domain, setDomain] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  // State baru untuk melacak tab yang sedang aktif
  const [activeTab, setActiveTab] = useState('status');

  const handleAnalyze = async (e) => {
    e.preventDefault();
    if (!domain) {
      setError('Nama domain tidak boleh kosong.');
      return;
    }

    setLoading(true);
    setResults(null);
    setError('');
    setActiveTab('status'); // Selalu reset ke tab status saat analisis baru

    try {
      const [statusRes, whoisRes, dnsRes] = await Promise.all([
        axios.get(`${API_BASE_URL}/status/${domain}`),
        axios.get(`${API_BASE_URL}/whois/${domain}`),
        axios.get(`${API_BASE_URL}/dns/${domain}`)
      ]);
      
      setResults({
        status: statusRes.data,
        whois: whoisRes.data,
        dns: dnsRes.data
      });
    } catch (err) {
      console.error("API Fetch Error:", err);
      setError('Gagal mengambil data. Pastikan domain valid dan API server backend berjalan.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Situistik 🕵️</h1>
      <p>Cek apakah sebuah situs, aplikasi, atau layanan sedang down untuk semua orang atau hanya Anda.</p>
      
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

      {error && <p className="error">{error}</p>}

      {loading && <p>Loading...</p>}

      {results && (
        <div className="results">
          {/* Navigasi Tab */}
          <div className="tabs">
            <button 
              className={`tab-button ${activeTab === 'status' ? 'active' : ''}`}
              onClick={() => setActiveTab('status')}
            >
              Status
            </button>
            <button 
              className={`tab-button ${activeTab === 'dns' ? 'active' : ''}`}
              onClick={() => setActiveTab('dns')}
            >
              DNS Records
            </button>
            <button 
              className={`tab-button ${activeTab === 'whois' ? 'active' : ''}`}
              onClick={() => setActiveTab('whois')}
            >
              Whois Info
            </button>
          </div>

          {/* Konten Tab */}
          <div className="tab-content">
            {activeTab === 'status' && <StatusResult statusData={results.status} />}
            {activeTab === 'dns' && <DnsResult dnsData={results.dns} />}
            {activeTab === 'whois' && <WhoisResult whoisData={results.whois} />}
          </div>
        </div>
      )}
      <Footer />
    </div>
  );
}

export default App;