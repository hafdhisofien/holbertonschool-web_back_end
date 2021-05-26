const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', function (){
    let log;

    beforeEach(function() {
        log = sinon.spy(console, 'log');
    });
    afterEach(function(){
        log.restore();
    })

    it('sendPaymentRequestToAPI with 100, 20',function(){
      sendPaymentRequestToApi(100, 20);
      chai.expect(log.calledOnce).to.be.true;
      chai.expect(log.calledWith('The total is: 120')).to.be.true;
    });
    it('sendPaymentRequestToAPI with 10, 10',function(){
        sendPaymentRequestToApi(10, 10);
        chai.expect(log.calledOnce).to.be.true;
        chai.expect(log.calledWith('The total is: 20')).to.be.true;
      });
  });