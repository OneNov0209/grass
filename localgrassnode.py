import os
import asyncio
import random
import ssl
import json
import time
import uuid
import websockets
from loguru import logger
from fake_useragent import UserAgent
from dotenv import load_dotenv  # Import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve USER_ID and ORIGIN_URL from environment variables
user_id = os.getenv('USER_ID')  # Ganti dengan ID pengguna Anda dari .env
origin_url = os.getenv('ORIGIN_URL')

user_agent = UserAgent(os='windows', browsers='chrome')
random_user_agent = user_agent.random

async def connect_to_wss(user_id):
    device_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, "155.133.22.148"))
    logger.info(device_id)
    while True:
        try:
            await asyncio.sleep(random.uniform(0.1, 1))
            custom_headers = {
                "User-Agent": random_user_agent,
                "Origin": origin_url  # Menggunakan URL dari .env
            }
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            urilist = ["wss://proxy.wynd.network:4444/", "wss://proxy.wynd.network:4650/"]
            uri = random.choice(urilist)
            server_hostname = "proxy.wynd.network"

            async with websockets.connect(uri, ssl=ssl_context, extra_headers=custom_headers) as websocket:
                async def send_ping():
                    while True:
                        send_message = json.dumps(
                            {"id": str(uuid.uuid4()), "version": "1.0.0", "action": "PING", "data": {}})
                        logger.debug(send_message)
                        await websocket.send(send_message)
                        await asyncio.sleep(5)

                await asyncio.sleep(1)
                asyncio.create_task(send_ping())
                while True:
                    response = await websocket.recv()
                    message = json.loads(response)
                    logger.info(message)
                    if message.get("action") == "AUTH":
                        auth_response = {
                            "id": message["id"],
                            "origin_action": "AUTH",
                            "result": {
                                "browser_id": device_id,
                                "user_id": user_id,
                                "user_agent": custom_headers['User-Agent'],
                                "timestamp": int(time.time()),
                                "device_type": "extension",
                                "version": "4.26.2",
                                "extension_id": "lkbnfiajjmbhnfledhphioinpickokdi"
                            }
                        }
                        logger.debug(auth_response)
                        await websocket.send(json.dumps(auth_response))
                    elif message.get("action") == "PONG":
                        pong_response = {"id": message["id"], "origin_action": "PONG"}
                        logger.debug(pong_response)
                        await websocket.send(json.dumps(pong_response))
        except Exception as e:
            logger.error(e)

async def main():
    await connect_to_wss(user_id)

if __name__ == '__main__':
    asyncio.run(main())
