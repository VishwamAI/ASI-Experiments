import unittest
import subprocess
import os
import json
import sys

from unittest.mock import patch, MagicMock

# Ensure the parent directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestMainScript(unittest.TestCase):

    def setUp(self):
        self.config_path = 'test_config.json'
        self.log_path = 'asi.log'
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
        mock_asi_system.get_input.side_effect = ['test_input', Exception("Simulated Exception")]

        # Set environment variable to break the loop
        os.environ['ASI_TEST_BREAK_LOOP'] = '1'

        result = subprocess.run(['python3', 'main.py', '--config', self.config_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertEqual(result.returncode, 0)

        # Check the log file for the "Configuration loaded" message
        with open(self.log_path, 'r') as log_file:
            log_contents = log_file.read()
        self.assertIn("Configuration loaded", log_contents)

        # Clean up environment variable
        del os.environ['ASI_TEST_BREAK_LOOP']

    @patch('main.ASIMainControlLoop')
    def test_main_script_with_custom_config(self, MockASIMainControlLoop):
        mock_asi_system = MagicMock()
        MockASIMainControlLoop.return_value = mock_asi_system
        mock_asi_system.get_input.side_effect = ['test_input', Exception("Simulated Exception")]

        # Set environment variable to break the loop
        os.environ['ASI_TEST_BREAK_LOOP'] = '1'

        result = subprocess.run(['python3', 'main.py', '--config', self.config_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertEqual(result.returncode, 0)

        # Check the log file for the "Configuration loaded" message
        with open(self.log_path, 'r') as log_file:
            log_contents = log_file.read()
        self.assertIn("Configuration loaded", log_contents)

        # Clean up environment variable
        del os.environ['ASI_TEST_BREAK_LOOP']

    @patch('main.ASIMainControlLoop')
    def test_main_script_with_custom_log(self, MockASIMainControlLoop):
        mock_asi_system = MagicMock()
        MockASIMainControlLoop.return_value = mock_asi_system
        mock_asi_system.get_input.side_effect = ['test_input', Exception("Simulated Exception")]

        # Set environment variable to break the loop
        os.environ['ASI_TEST_BREAK_LOOP'] = '1'

        result = subprocess.run(['python3', 'main.py', '--log', self.log_path, '--config', self.config_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(self.log_path))

        # Check the log file for the "Configuration loaded" message
        with open(self.log_path, 'r') as log_file:
            log_contents = log_file.read()
        self.assertIn("Configuration loaded", log_contents)

        # Clean up environment variable
        del os.environ['ASI_TEST_BREAK_LOOP']

if __name__ == '__main__':
    unittest.main()
