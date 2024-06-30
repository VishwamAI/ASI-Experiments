import requests
import json
import logging

class DataIngestion:
    def __init__(self, api_urls):
        self.api_urls = api_urls
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def fetch_data(self):
        all_data = []
        errors = []
        for api_url in self.api_urls:
            try:
                response = requests.get(api_url)
                response.raise_for_status()
                data = response.json()
                all_data.append(data)
                logging.info(f"Data fetched successfully from {api_url}")
            except requests.exceptions.RequestException as e:
                logging.error(f"Error fetching data from {api_url}: {e}")
                errors.append((api_url, str(e)))
        return all_data, errors

    def save_data(self, data, file_path, format='json'):
        try:
            if format == 'json':
                with open(file_path, 'w') as file:
                    json.dump(data, file)
            elif format == 'csv':
                import pandas as pd
                df = pd.DataFrame(data)
                df.to_csv(file_path, index=False)
            elif format == 'xml':
                import dicttoxml
                xml_data = dicttoxml.dicttoxml(data)
                with open(file_path, 'wb') as file:
                    file.write(xml_data)
            else:
                raise ValueError("Unsupported format. Use 'json', 'csv', or 'xml'.")
            logging.info(f"Data saved to {file_path}")
        except (OSError, ValueError) as e:
            logging.error(f"Error saving data to {file_path}: {e}")
            raise

if __name__ == "__main__":
    api_urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
    file_path = "data.json"

    data_ingestion = DataIngestion(api_urls)
    data, errors = data_ingestion.fetch_data()

    if data:
        data_ingestion.save_data(data, file_path)

    if errors:
        logging.error(f"Errors encountered during data fetching: {errors}")
