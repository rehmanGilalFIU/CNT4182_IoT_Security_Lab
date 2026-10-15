import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE = str(BASE_DIR / 'iot_demo.sqlite3')
SECRET_KEY = os.getenv('IOT_SECRET_KEY', 'demo-building-2026-secret')
DEBUG_MODE = True
DEFAULT_ADMIN = ('admin', 'admin123')
DEVICE_TOKEN = 'iot-control-token-123'
MAX_TELEMETRY_ITEMS = 200
