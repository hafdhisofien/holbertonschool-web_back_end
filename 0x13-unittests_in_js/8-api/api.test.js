const request = require('request');
const chai = require('chai')

describe('ntegration test', function () {
    it('check code status 200 and result', function (done) {
      const call = { url: 'http://localhost:7865', method: 'GET' };
      request(call, function(error, response, body) {
        chai.expect(response.statusCode).to.equal(200);
        chai.expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });