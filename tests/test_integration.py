import unittest
import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.core import ASIMainControlLoop

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.asi = ASIMainControlLoop()

    def test_integration_decision_making(self):
        input_data = {
            "data": [
                [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15],
                [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30],
                [31, 32, 33], [34, 35, 36], [37, 38, 39], [40, 41, 42], [43, 44, 45],
                [46, 47, 48], [49, 50, 51], [52, 53, 54], [55, 56, 57], [58, 59, 60]
            ],
            "labels": [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
        }
        self.asi.process_input(input_data)
        decision = self.asi.make_decision()

        self.assertIsInstance(decision, dict)
        self.assertIn("strategies_results", decision)
        self.assertIn("risks", decision)
        self.assertIn("outcomes", decision)

        strategies_results = decision["strategies_results"]
        risks = decision["risks"]
        outcomes = decision["outcomes"]

        self.assertIsInstance(strategies_results, dict)
        self.assertIsInstance(risks, dict)
        self.assertIsInstance(outcomes, dict)

        for strategy, metrics in strategies_results.items():
            self.assertIn(strategy, ['logistic_regression', 'decision_tree', 'svm'])
            self.assertIsInstance(metrics, dict)
            self.assertIn('accuracy', metrics)
            self.assertIn('precision', metrics)
            self.assertIn('recall', metrics)
            self.assertIn('f1_score', metrics)
            self.assertIsInstance(metrics['accuracy'], float)
            self.assertIsInstance(metrics['precision'], float)
            self.assertIsInstance(metrics['recall'], float)
            self.assertIsInstance(metrics['f1_score'], float)

        for decision, value in risks.items():
            self.assertIn(decision, ['decision_1', 'decision_2', 'decision_3'])
            self.assertIsInstance(value, float)

        for decision, value in outcomes.items():
            self.assertIn(decision, ['decision_1', 'decision_2', 'decision_3'])
            self.assertIsInstance(value, float)

if __name__ == "__main__":
    unittest.main()
