import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import requests
from learning.data_ingestion import DataIngestion

class TestDataIngestion(unittest.TestCase):
    @patch('learning.data_ingestion.requests.get')
    def test_fetch_data_success(self, mock_get):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"key": "value"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data = data_ingestion.fetch_data()

        self.assertIsNotNone(data)
        self.assertEqual(data, [{"key": "value"}, {"key": "value"}])

    @patch('learning.data_ingestion.requests.get')
    def test_fetch_data_failure(self, mock_get):
        # Mock the API response to raise an exception
        mock_get.side_effect = requests.exceptions.RequestException("API error")

        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data = data_ingestion.fetch_data()

        self.assertEqual(data, [])

    @patch('builtins.open', new_callable=mock_open)
    def test_save_data_success(self, mock_file):
        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data = {"key": "value"}
        file_path = "data.json"

        data_ingestion.save_data(data, file_path)

        mock_file.assert_called_once_with(file_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('{')
        handle.write.assert_any_call('"key"')
        handle.write.assert_any_call(': ')
        handle.write.assert_any_call('"value"')
        handle.write.assert_any_call('}')

    @patch('builtins.open', new_callable=mock_open)
    def test_save_data_failure(self, mock_file):
        # Mock the open function to raise an OSError
        mock_file.side_effect = OSError("File error")

        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data = {"key": "value"}
        file_path = "data.json"

        with self.assertRaises(OSError):
            data_ingestion.save_data(data, file_path)

if __name__ == "__main__":
    unittest.main()
