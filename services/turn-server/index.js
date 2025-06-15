const Turn = require('node-turn');
require('dotenv').config(); // To load environment variables from .env file

const turnUsername = process.env.TURN_USERNAME || 'defaultuser';
const turnPassword = process.env.TURN_PASSWORD || 'defaultpassword';
const turnRealm = process.env.TURN_REALM || 'tigasdev.com';
const turnListeningIp = process.env.TURN_LISTEN_IP || '0.0.0.0'; // Listen on all interfaces
const turnRelayIp = process.env.TURN_RELAY_IP; // Public IP of the server, if behind NAT
const turnMinPort = parseInt(process.env.TURN_MIN_PORT, 10) || 49152;
const turnMaxPort = parseInt(process.env.TURN_MAX_PORT, 10) || 65535;
const turnListeningPort = parseInt(process.env.TURN_PORT, 10) || 3478;
const turnVerbose = process.env.TURN_VERBOSE === 'true';

if (!turnRelayIp) {
    console.warn(`
        **************************************************************************************
        WARNING: TURN_RELAY_IP environment variable is not set.
        If this server is behind a NAT, you MUST set this to the public IP address
        of the server for the TURN server to function correctly with external clients.
        If running locally or with a direct public IP, it might work but it's less reliable.
        **************************************************************************************
    `);
}

const server = new Turn({
    // Set basic listening options
    listeningIps: [turnListeningIp],
    listeningPort: turnListeningPort,

    // Set authentication options
    authMech: 'long-term',
    credentials: {
        [turnUsername]: turnPassword
    },
    realm: turnRealm,

    // Specify the public IP of the server if it's behind a NAT
    // This is crucial for the server to correctly advertise its relay address
    relayIp: turnRelayIp, // If your server has a public IP directly, you might not need this or can use the listening IP

    // Define the port range for relaying media
    minPort: turnMinPort,
    maxPort: turnMaxPort,

    // Other options
    debugLevel: turnVerbose ? 'DEBUG' : 'INFO', // 'TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'
    log: (level, message) => {
        console.log(`[${level}] ${message}`);
    },
    // software: 'TigasDev TURN Server' // Optional: Custom software name
});

// Handle server errors
server.on('error', (err) => {
    console.error('TURN Server Error:', err);
});

// Log connected users
server.on('allocation', (allocation) => {
    console.log(`[INFO] Client connected and allocation created:`);
    console.log(`  Username: ${allocation.username}`);
    console.log(`  Client Address: ${allocation.clientAddress}:${allocation.clientPort}`);
    console.log(`  Relay Address: ${allocation.relayAddress}:${allocation.relayPort}`);
    console.log(`  Protocol: ${allocation.protocol}`);
});

// Start the server
server.start();
console.log(`TURN server started on ${turnListeningIp}:${turnListeningPort}`);
console.log(`Realm: ${turnRealm}`);
console.log(`Relay port range: ${turnMinPort}-${turnMaxPort}`);
if (turnRelayIp) {
    console.log(`Relay IP (public IP): ${turnRelayIp}`);
}
console.log(`Credentials: ${turnUsername} / (password is hidden)`);
