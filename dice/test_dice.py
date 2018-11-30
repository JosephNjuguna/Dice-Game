import unittest
import dice

class testDice(unittest.TestCase):
    def test_class(self):
        dicerange = 1,6
        result = dice(dicerange)
        self.assertEqual(result, range(dicerange))

        
