// src/components/WhoisResult.jsx

import React from 'react';

// Fungsi helper untuk memformat tanggal
const formatDate = (dateString) => {
  if (!dateString) return 'N/A';
  // Jika datenya berupa list, ambil yang pertama
  const dateToFormat = Array.isArray(dateString) ? dateString[0] : dateString;
  return new Date(dateToFormat).toLocaleDateString('id-ID', {
    year: 'numeric', month: 'long', day: 'numeric',
  });
};


const WhoisResult = ({ whoisData }) => {
  if (!whoisData) return null;

  if (whoisData.error) {
    return <div className="details-container"><p>Error fetching Whois data: {whoisData.error}</p></div>
  }

  return (
    <div className="details-container">
      <h3>Whois Information</h3>
      <ul className="details-list">
        <li>
          <strong>Registrar:</strong> {whoisData.registrar || 'N/A'}
        </li>
        <li>
          <strong>Tanggal Dibuat:</strong> {formatDate(whoisData.creation_date)}
        </li>
        <li>
          <strong>Tanggal Kadaluarsa:</strong> {formatDate(whoisData.expiration_date)}
        </li>
        <li>
          <strong>Name Servers:</strong>
          <ul>
            {(whoisData.name_servers || []).map((ns, index) => <li key={index}>{ns}</li>)}
          </ul>
        </li>
      </ul>
    </div>
  );
};

export default WhoisResult;