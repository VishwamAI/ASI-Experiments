import requests
import json

class DataIngestion:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def save_data(self, data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            print(f"Data saved to {file_path}")
        except IOError as e:
            print(f"Error saving data: {e}")

if __name__ == "__main__":
    api_url = "https://api.example.com/data"
    file_path = "data.json"

    data_ingestion = DataIngestion(api_url)
    data = data_ingestion.fetch_data()

    if data:
        data_ingestion.save_data(data, file_path)
