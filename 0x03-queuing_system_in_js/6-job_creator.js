import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Create a job object
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the notification message',
};

// Create a job
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (err) {
    console.error(`Notification job failed: ${err}`);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Process job events
job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
