// src/components/DnsResult.jsx

import React from 'react';

const DnsResult = ({ dnsData }) => {
  if (!dnsData) return null;

  return (
    <div className="details-container">
      <h3>DNS Records</h3>
      <table className="details-table">
        <thead>
          <tr>
            <th>Tipe Record</th>
            <th>Nilai</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(dnsData).map(([type, values]) => (
            values.length > 0 && (
              <tr key={type}>
                <td>{type}</td>
                <td>
                  {values.map((value, index) => (
                    <div key={index}>{value}</div>
                  ))}
                </td>
              </tr>
            )
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DnsResult;