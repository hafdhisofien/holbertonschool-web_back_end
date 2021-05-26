const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', function (){
    const spy = sinon.spy(Utils, 'calculateNumber');
  
    it('validate the usage of the Utils',function(){
      sendPaymentRequestToApi(100, 20);
      chai.expect(spy.calledOnce).to.be.true;
      chai.expect(spy.calledWith('SUM', 100, 20)).to.be.true;
      spy.restore()
    });
  });