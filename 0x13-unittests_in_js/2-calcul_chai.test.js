const calculateNumber = require('./1-calcul.js');
const chai = require('chai');

describe("smoke test for type of SUM", function() {
    it("checks if rounded", function() {
        chai.expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        chai.expect(calculateNumber('SUM', 1, 4.5)).to.equal(6);
        chai.expect(calculateNumber('SUM', 1.1, 3.5)).to.equal(5);
        chai.expect(calculateNumber('SUM', 1, 1)).to.equal(2);
        chai.expect(calculateNumber('SUM', 0, 0)).to.equal(0);
        chai.expect(calculateNumber('SUM', -1, -4)).to.equal(-5);
        chai.expect(calculateNumber('SUM', 1, -1)).to.equal(0);
    });
  });

  describe("smoke test for type of SUBTRACT", function() {
    it("checks if rounded", function() {
        chai.expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        chai.expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
        chai.expect(calculateNumber('SUBTRACT', 1, 1)).to.equal(0);
        chai.expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
        chai.expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3);
    });
  });

  describe("smoke test for type of DIVIDE", function() {
    it("checks if rounded", function() {
        chai.expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        chai.expect(calculateNumber('DIVIDE', 1.1, 3.5)).to.equal(0.25);
        chai.expect(calculateNumber('DIVIDE', 1, 1)).to.equal(1);
        chai.expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
        chai.expect(calculateNumber('DIVIDE', -1.4, -4.5)).to.equal(0.25);
    });
  });