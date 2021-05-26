const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe("smoke test", function() {
    it("checks if rounded", function() {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(-1, 1), 0);
        assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
    });
    it('checks if argument is NaN', () => {
        assert.strictEqual(isNaN(calculateNumber(1)), true);
        assert.strictEqual(isNaN(calculateNumber()), true);
      });
  });