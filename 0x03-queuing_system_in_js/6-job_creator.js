import { createQueue } from 'kue';

const queue = createQueue();

const notification = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', notification).save((err) => {
  if (!err) {	
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.on('completed', () => {
  console.log('Notification job completed');
});
