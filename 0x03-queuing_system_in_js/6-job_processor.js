import kue from 'kue';
import redis from 'redis';

const queue = kue.createQueue();
const client = redis.createClient();

// Function to send notification
const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Queue process to handle push_notification_code jobs
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});
