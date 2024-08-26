import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle error event
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
