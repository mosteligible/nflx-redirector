import threading
from typing import List

import requests
from Collector import Collector
from Config import COLLECTION, SHOW_DB
from Log import APP_LOGGER
from utils import getShowDetails


def UpdateDatabase(collectorResponse: List[requests.models.Response], service: str):
    allItems = collectorResponse.json()
    APP_LOGGER.info(f"Number of items received from {service}: {len(allItems)}")
    for item in allItems:
        show = getShowDetails(item)
        SHOW_DB.AddEntry(dbPayload=show)


def main():
    threads = []
    for endpoint in COLLECTION:
        APP_LOGGER.info(f"Collecting and adding information for {endpoint.Service}")
        collector = Collector(config=endpoint)
        collector.collect()
        db_thread = threading.Thread(
            target=UpdateDatabase, args=(collector.response, endpoint.Service), daemon=False
        )
        threads.append(db_thread)
        db_thread.start()


if __name__ == "__main__":
    main()
