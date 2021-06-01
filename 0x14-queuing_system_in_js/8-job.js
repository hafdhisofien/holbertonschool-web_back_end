export default function createPushNotificationsJobs(jobs, queue) {
    if (Object.getPrototypeOf(jobs) !== Array.prototype) throw Error('Jobs is not an array');

    jobs.forEach((job) => {
        const onejob = queue.create('push_notification_code_3', job).save(
            function(error) {
                if (!error) console.log(`Notification job created: ${onejob.id}`);
            });
    
        onejob.on('complete', () => console.log(`Notification job ${onejob.id} completed`));
        onejob.on('failed', (error) => console.log(`Notification job ${onejob.id} failed: ${error}`));
        onejob.on('progress', (progress) => console.log(`Notification job ${onejob.id} ${progress}% complete`));
    });
}