import unittest
from core.core import ASIMainControlLoop

class TestASIMainControlLoop(unittest.TestCase):
    def setUp(self):
        self.asi = ASIMainControlLoop()

    def test_initialization(self):
        self.assertIsInstance(self.asi, ASIMainControlLoop)
        self.assertIsInstance(self.asi.state, dict)

    def test_process_input(self):
        input_data = {"key": "value"}
        self.asi.process_input(input_data)
        self.assertEqual(self.asi.state["input_data"], input_data)

        input_data = '{"key": "value"}'
        self.asi.process_input(input_data)
        self.assertEqual(self.asi.state["input_data"], {"key": "value"})

        input_data = "invalid_json"
        self.asi.process_input(input_data)
        self.assertIsNone(self.asi.state["input_data"])

    def test_make_decision(self):
        input_data = {"key": "value"}
        self.asi.process_input(input_data)
        decision = self.asi.make_decision()
        self.assertEqual(decision, "decision_based_on_key_value")
        self.assertEqual(self.asi.state["decision"], "decision_based_on_key_value")

        input_data = {"key": "other_value"}
        self.asi.process_input(input_data)
        decision = self.asi.make_decision()
        self.assertEqual(decision, "default_decision")
        self.assertEqual(self.asi.state["decision"], "default_decision")

    def test_execute_action(self):
        action = {"action": "test"}
        self.asi.execute_action(action)
        self.assertEqual(self.asi.state["action"], action)

    def test_run(self):
        # This test will need to be adapted once the run method is fully implemented
        pass

if __name__ == "__main__":
    unittest.main()
