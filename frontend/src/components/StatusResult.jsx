// src/components/StatusResult.jsx

import React from 'react';

// Terima 'statusData' sebagai properti (prop) dari App.jsx
const StatusResult = ({ statusData }) => {
  if (!statusData) return null;

  const isUp = statusData.up;

  return (
    <div className={`status-card ${isUp ? 'is-up' : 'is-down'}`}>
      <div className="status-icon">
        {isUp ? '✅' : '❌'}
      </div>
      <div className="status-text">
        <h2>{isUp ? "It's UP!" : "It's DOWN."}</h2>
        <p>
          {isUp 
            ? `We reached ${statusData.url} successfully.`
            : `We could not reach the server. Reason: ${statusData.reason}`
          }
        </p>
        {isUp && <p>Status Code: {statusData.status_code} {statusData.reason}</p>}
      </div>
    </div>
  );
};

export default StatusResult;