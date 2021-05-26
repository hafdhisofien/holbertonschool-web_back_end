const request = require('request');
const chai = require('chai')

describe('regex test', function () {
    it('check code status 200 and result', function (done) {
      const call = { url: 'http://localhost:7865', method: 'GET' };
      request(call, function(error, response, body) {
        chai.expect(response.statusCode).to.equal(200);
        chai.expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
  describe('ID is NAN', () => {
    it('endpoint: GET /cart/:isNaN', (done) => {
      const call = { url: 'http://localhost:7865/cart/anything',method: 'GET',};
      request(call, function(error, response, body) {
        chai.expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });