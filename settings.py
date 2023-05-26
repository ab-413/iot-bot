
import logging
import os

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)

console = logging.StreamHandler()
file = logging.FileHandler('logs/bot.log', mode='a', encoding='utf-8')
console.setLevel(logging.INFO)
file.setLevel(logging.INFO)

logFormat = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                              '%d.%m.%Y %H:%M:%S')

file.setFormatter(logFormat)
console.setFormatter(logFormat)

log.addHandler(console)
log.addHandler(file)

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")
MASTER_TOKEN = os.getenv("MASTER_TOKEN")

get_data = "get_data/"
get_tg_users = "tg_users/"

master_token = {'Token': MASTER_TOKEN}
