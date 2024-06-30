import unittest
import subprocess
import os
import json
from unittest.mock import patch, MagicMock

class TestMainScript(unittest.TestCase):

    def setUp(self):
        self.config_path = 'test_config.json'
        self.log_path = 'test_asi.log'
        self.create_test_config()

    def tearDown(self):
        if os.path.exists(self.config_path):
            os.remove(self.config_path)
        if os.path.exists(self.log_path):
            os.remove(self.log_path)

    def create_test_config(self):
        config = {
            "parameter1": "test_value1",
            "parameter2": "test_value2"
        }
        with open(self.config_path, 'w') as config_file:
            json.dump(config, config_file)

    @patch('main.ASIMainControlLoop')
    def test_main_script_with_default_config(self, MockASIMainControlLoop):
        mock_asi_system = MagicMock()
        MockASIMainControlLoop.return_value = mock_asi_system
        mock_asi_system.get_input.side_effect = ['test_input', KeyboardInterrupt]

        result = subprocess.run(['python3', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Configuration loaded", result.stdout)

    @patch('main.ASIMainControlLoop')
    def test_main_script_with_custom_config(self, MockASIMainControlLoop):
        mock_asi_system = MagicMock()
        MockASIMainControlLoop.return_value = mock_asi_system
        mock_asi_system.get_input.side_effect = ['test_input', KeyboardInterrupt]

        result = subprocess.run(['python3', 'main.py', '--config', self.config_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Configuration loaded", result.stdout)

    @patch('main.ASIMainControlLoop')
    def test_main_script_with_custom_log(self, MockASIMainControlLoop):
        mock_asi_system = MagicMock()
        MockASIMainControlLoop.return_value = mock_asi_system
        mock_asi_system.get_input.side_effect = ['test_input', KeyboardInterrupt]

        result = subprocess.run(['python3', 'main.py', '--log', self.log_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(self.log_path))

if __name__ == '__main__':
    unittest.main()
