const calculateNumber = require('./1-calcul.js');
const assert = require('assert');

describe("smoke test for type of SUM", function() {
    it("checks if rounded", function() {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 1, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 1.1, 3.5), 5);
        assert.strictEqual(calculateNumber('SUM', 1, 1), 2);
        assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
        assert.strictEqual(calculateNumber('SUM', -1, -4), -5);
        assert.strictEqual(calculateNumber('SUM', 1, -1), 0);
    });
  });

  describe("smoke test for type of SUBTRACT", function() {
    it("checks if rounded", function() {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        assert.strictEqual(calculateNumber('SUBTRACT', 5, 3), 2);
        assert.strictEqual(calculateNumber('SUBTRACT', 1, 1), 0);
        assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
        assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5), 3);
    });
  });

  describe("smoke test for type of DIVIDE", function() {
    it("checks if rounded", function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.strictEqual(calculateNumber('DIVIDE', 1.1, 3.5), 0.25);
        assert.strictEqual(calculateNumber('DIVIDE', 1, 1), 1);
        assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
        assert.strictEqual(calculateNumber('DIVIDE', -1.4, -4.5), 0.25);
    });
  });