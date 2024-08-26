import { expect } from 'chai';
import kue from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
    let queue;

    beforeEach(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    });

    it('should create jobs and handle job events', (done) => {
        const jobs = [
            { phoneNumber: '4153518780', message: 'Test message' }
        ];

        createPushNotificationsJobs(jobs, queue);

        queue.testMode.jobs((err, jobs) => {
            if (err) return done(err);
            expect(jobs).to.have.lengthOf(1);
            expect(jobs[0].type).to.equal('push_notification_code_3');
            done();
        });
    });
});
