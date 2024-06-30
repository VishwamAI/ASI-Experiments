import unittest
import numpy as np
from decision_making.decision_making import DecisionMaking

class TestDecisionMaking(unittest.TestCase):
    def setUp(self):
        self.decision_making = DecisionMaking()
        self.data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.labels = np.array([0, 1, 1])

    def test_evaluate_strategies(self):
        results = self.decision_making.evaluate_strategies(self.data, self.labels)
        self.assertIsInstance(results, dict)
        self.assertEqual(len(results), 3)
        for strategy, metrics in results.items():
            self.assertIn(strategy, ['strategy_1', 'strategy_2', 'strategy_3'])
            self.assertIsInstance(metrics, dict)
            self.assertIn('accuracy', metrics)
            self.assertIn('precision', metrics)
            self.assertIn('recall', metrics)
            self.assertIn('f1_score', metrics)
            self.assertIsInstance(metrics['accuracy'], float)
            self.assertIsInstance(metrics['precision'], float)
            self.assertIsInstance(metrics['recall'], float)
            self.assertIsInstance(metrics['f1_score'], float)

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
