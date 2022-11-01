import requests
from Config import USER_AGENT, Endpoints
from Constants import LOG_DIR
from Log import create_logger


class Collector:
    def __init__(self, config: Endpoints):
        self.service = config.Service
        self.url = config.Endpoint
        self.header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
            "Connection": "keep-alive",
            "Referer": config.Referer,
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
        self.logger = create_logger(
            log_location=LOG_DIR,
            logger_name=config.Service.upper(),
            file_name=f"{config.Service}-collector.log",
        )

    def collect(self):
        self.logger.info(f"Retreiving information from {self.service}")
        self.response = self.session.get(url=self.url, headers=self.header, timeout=10)
