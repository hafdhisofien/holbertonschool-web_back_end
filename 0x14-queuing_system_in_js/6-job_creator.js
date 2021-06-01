import kue from 'kue';
const queue = kue.createQueue();

const data = {
    phoneNumber: "",
    message: "",
};

const job = queue.create('push_notification_code', data).save(
    function(error) {
        if (!error) console.log(`Notification job created: ${job.id}`);
    });

job.on('complete', function() {
    console.log('Notification job completed')});

job.on('failed', function() {
    console.log('Notification job failed')});
