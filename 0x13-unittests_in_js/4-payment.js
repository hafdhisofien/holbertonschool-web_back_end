const Utils = require('./utils.js');

module.exports = function(totalAmount, totalShipping){
    const res = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${res}`);
}