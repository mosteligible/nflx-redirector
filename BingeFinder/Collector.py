import time

import requests
from Config import USER_AGENT, Endpoints


class Collector:
    def __init__(self, config: Endpoints):
        self.endpoints = config
        self.header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
            "Connection": "keep-alive",
            "Referer": self.endpoints.Referer,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
            "User-Agent": USER_AGENT,
            "X-Requested-With": "XMLHttpRequest",
        }
        self.session = requests.Session()
        self.retries = requests.adapters.Retry(
            total=5, connect=3, read=2, redirect=3, backoff_factor=2
        )
        self.session.mount(
            prefix="https://",
            adapter=requests.adapters.HTTPAdapter(max_retries=self.retries),
        )

    def collect(self):
        self.response = self.session.get(
            url=self.endpoints.Endpoint, headers=self.header, timeout=10
        )
