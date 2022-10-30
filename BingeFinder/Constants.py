from pathlib import Path

CWD = Path(__file__).resolve().parent
LOG_DIR = CWD / "LOGS"
LOG_DIR.mkdir(exist_ok=True, parents=True)

DB_LOG_LOCATION = LOG_DIR / "DB_LOGS"
DB_LOG_LOCATION.mkdir(exist_ok=True, parents=True)
