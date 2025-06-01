const express = require('express');
const cors = require('cors');
const helmet = require('helmet');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({
    service: 'peer-server',
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    service: 'peer-server',
    version: '1.0.0',
    message: 'Peer Server is running'
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Peer Server running on port ${PORT}`);
  console.log(`📊 Health check: http://localhost:${PORT}/health`);
}); 