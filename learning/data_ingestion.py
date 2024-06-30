import requests
import json
import logging

class DataIngestion:
    def __init__(self, api_urls):
        self.api_urls = api_urls
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def fetch_data(self):
        all_data = []
        for api_url in self.api_urls:
            try:
                response = requests.get(api_url)
                response.raise_for_status()
                data = response.json()
                all_data.append(data)
                logging.info(f"Data fetched successfully from {api_url}")
            except requests.exceptions.RequestException as e:
                logging.error(f"Error fetching data from {api_url}: {e}")
        return all_data

    def save_data(self, data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            logging.info(f"Data saved to {file_path}")
        except OSError as e:
            logging.error(f"Error saving data to {file_path}: {e}")
            raise

if __name__ == "__main__":
    api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
    file_path = "data.json"

    data_ingestion = DataIngestion(api_urls)
    data = data_ingestion.fetch_data()

    if data:
        data_ingestion.save_data(data, file_path)
