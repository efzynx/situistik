// src/components/Footer.jsx

import React from 'react';

// Komponen sederhana untuk menampilkan informasi di bagian bawah halaman.
const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-section">
        <h3>Tentang Situistik</h3>
        <p>
          Situistik adalah alat diagnostik web sederhana yang membantu Anda memeriksa apakah sebuah situs web sedang down atau tidak dari berbagai perspektif. Cukup masukkan nama domain, dan kami akan melakukan pengecekan status HTTP, mengambil catatan DNS penting, dan menampilkan data registrasi Whois untuk analisis yang lebih mendalam.
        </p>
      </div>
      <div className="footer-section">
        <h3>Teknologi yang Digunakan</h3>
        <p>
          Aplikasi ini dibangun dengan antarmuka yang responsif menggunakan <strong>React.js (Vite)</strong> dan didukung oleh backend yang andal yang dibuat dengan <strong>Python (FastAPI)</strong>. Arsitektur ini menggabungkan kecepatan rendering di sisi klien dengan kekuatan pemrosesan jaringan di sisi server.
        </p>
      </div>
      <div className="footer-section footer-meta">
        <p>
          Dikelola oleh <a href="https://github.com/efzynx" target="_blank" rel="noopener noreferrer">Efzyn</a>
        </p>
        <p>
          {/* Ganti dengan URL repositori Anda yang sebenarnya */}
          <a href="https://github.com/efzynx/situistik.git" target="_blank" rel="noopener noreferrer">
            Lihat Kode Sumber di GitHub
          </a>
        </p>
      </div>
    </footer>
  );
};

export default Footer;
