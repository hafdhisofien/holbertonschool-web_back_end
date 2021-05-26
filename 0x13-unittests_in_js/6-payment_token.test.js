const chai = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', () => {
    it('promise response from API should resolve', (done) => {
        getPaymentTokenFromAPI(true).then((response) => {
            chai.expect(response).to.include({ data: 'Successful response from the API' });
            done();
        })
        .catch((err) => {
            done(err);
        });
    });
});