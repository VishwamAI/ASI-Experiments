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
        data, errors = data_ingestion.fetch_data()

        self.assertIsNotNone(data)
        self.assertEqual(data, [{"key": "value"}, {"key": "value"}])
        self.assertEqual(errors, [])

    @patch('learning.data_ingestion.requests.get')
    def test_fetch_data_failure(self, mock_get):
        # Mock the API response to raise an exception
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("API error")
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data, errors = data_ingestion.fetch_data()

        self.assertEqual(data, [])
        self.assertEqual(len(errors), 2)
        self.assertIn(("https://api.example.com/data1", "API error", 500), errors)
        self.assertIn(("https://api.example.com/data2", "API error", 500), errors)

    @patch('learning.data_ingestion.requests.get')
    def test_fetch_data_no_response(self, mock_get):
        # Mock the API response to be None
        mock_get.return_value = None

        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data, errors = data_ingestion.fetch_data()

        self.assertEqual(data, [])
        self.assertEqual(len(errors), 2)
        self.assertIn(("https://api.example.com/data1", "No Response", "No Response"), errors)
        self.assertIn(("https://api.example.com/data2", "No Response", "No Response"), errors)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_data_success_json(self, mock_file):
        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data = {"key": "value"}
        file_path = "data.json"

        data_ingestion.save_data(data, file_path, format='json')

        mock_file.assert_called_once_with(file_path, 'w')
        handle = mock_file()
        handle.write.assert_any_call('{')
        handle.write.assert_any_call('"key"')
        handle.write.assert_any_call(': ')
        handle.write.assert_any_call('"value"')
        handle.write.assert_any_call('}')

    @patch('builtins.open', new_callable=mock_open)
    def test_save_data_success_csv(self, mock_file):
        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data = [{"key": "value"}]
        file_path = "data.csv"

        with patch('pandas.DataFrame.to_csv') as mock_to_csv:
            data_ingestion.save_data(data, file_path, format='csv')
            mock_to_csv.assert_called_once_with(file_path, index=False)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_data_success_xml(self, mock_file):
        api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
        data_ingestion = DataIngestion(api_urls)
        data = {"key": "value"}
        file_path = "data.xml"

        with patch('dicttoxml.dicttoxml') as mock_dicttoxml:
            mock_dicttoxml.return_value = b'<root><key>value</key></root>'
            data_ingestion.save_data(data, file_path, format='xml')
            mock_file.assert_called_once_with(file_path, 'wb')
            handle = mock_file()
            handle.write.assert_called_once_with(b'<root><key>value</key></root>')

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
