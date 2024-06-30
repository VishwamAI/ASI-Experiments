import unittest
import numpy as np
from decision_making.decision_making import DecisionMaking

class TestDecisionMaking(unittest.TestCase):
    def setUp(self):
        self.decision_making = DecisionMaking()
        self.data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_evaluate_strategies(self):
        results = self.decision_making.evaluate_strategies(self.data)
        self.assertIsInstance(results, dict)
        self.assertEqual(len(results), 3)
        for strategy, value in results.items():
            self.assertIn(strategy, ['strategy_1', 'strategy_2', 'strategy_3'])
            self.assertIsInstance(value, float)

    def test_assess_risks(self):
        risks = self.decision_making.assess_risks(self.data)
        self.assertIsInstance(risks, dict)
        self.assertEqual(len(risks), 3)
        for decision, value in risks.items():
            self.assertIn(decision, ['decision_1', 'decision_2', 'decision_3'])
            self.assertIsInstance(value, float)

    def test_predict_outcomes(self):
        outcomes = self.decision_making.predict_outcomes(self.data)
        self.assertIsInstance(outcomes, dict)
        self.assertEqual(len(outcomes), 3)
        for decision, value in outcomes.items():
            self.assertIn(decision, ['decision_1', 'decision_2', 'decision_3'])
            self.assertIsInstance(value, float)

if __name__ == '__main__':
    unittest.main()
