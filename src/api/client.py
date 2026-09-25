import requests
import logging
from src.config.settings import config

class APIClient:
    def __init__(self):
        self.url = config.API_URL

    def fetch_external_benchmarks(self) -> dict:
        logging.info("Querying external REST API benchmarks metrics tracking loop...")
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return{"status": "success", "external_payload": response.json()}
        except Exception as e:
            logging.error(f"Defensive framework routed network exception safely to offline logs mode: {str(e)}")
            return {"status": "http_network_offline_mode_active", "external_payload": {"market_index_ratio": 1.0}}
        

        