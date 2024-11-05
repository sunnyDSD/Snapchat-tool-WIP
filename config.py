# config.py

TARGET_URL = "https://accounts.snapchat.com/accounts/login"
USERNAME = "target_username"
PASSWORD_FILE = "passwords.txt"
PROXY_LIST = "proxies.txt"
THREAD_COUNT = 10
DELAY_RANGE = (1, 5)
CAPTCHA_TYPE = "interactive"
LOG_FILE = "logs/attempts.log"
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
]
TOR_ENABLED = True  # Enable Tor for IP rotation
