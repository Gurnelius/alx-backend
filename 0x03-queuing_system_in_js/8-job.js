import kue from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach(job => {
        const newJob = queue.create('push_notification_code_3', job)
            .save(err => {
                if (err) {
                    console.error(`Error creating job: ${err}`);
                } else {
                    console.log(`Notification job created: ${newJob.id}`);
                }
            });

        newJob.on('complete', () => {
            console.log(`Notification job ${newJob.id} completed`);
        }).on('failed', (errorMessage) => {
            console.log(`Notification job ${newJob.id} failed: ${errorMessage}`);
        }).on('progress', (progress) => {
            console.log(`Notification job ${newJob.id} ${progress}% complete`);
        });
    });
};

export default createPushNotificationsJobs;
