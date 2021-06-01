import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';
const queue = kue.createQueue();


describe('createPushNotificationsJobs', function(){
    before(function () {
      queue.testMode.enter();
    });
  
    afterEach(function () {
      queue.testMode.clear();
    });
  
    after(function () {
      queue.testMode.exit();
    });
    it('Error if jobs is not an array', function(){
    expect(function(){createPushNotificationsJobs(2, queue);}).to.throw('Jobs is not an array');})
    it('Error if jobs is a string', function(){
    expect(function(){createPushNotificationsJobs("jobs", queue);}).to.throw('Jobs is not an array');})
    it('Error if jobs is an object', function(){
    expect(function(){createPushNotificationsJobs({}, queue);}).to.throw('Jobs is not an array');})
});
