from datetime import timedelta, datetime
import requests
import json
from pytz import timezone
from settings import log
import settings


# Old function
# def utc_to_local(utc_dt):
#     return utc_dt.astimezone(settings.TIMEZONE)

def utc_to_local(utc_dt, hours):
    return utc_dt + timedelta(hours=hours)


def getUserState(chat_id):
    r = requests.get(settings.BASE_URL + settings.get_tg_users +
                     str(chat_id), headers=settings.master_token)
    responce = r.json()
    user_id = json.loads(json.dumps(responce['id']))
    is_active = json.loads(json.dumps(responce['is_active']))
    log.info(f"request user state for id: {user_id} by {chat_id}")
    if is_active:
        return True
    else:
        return False


def getUserID(chat_id):
    r = requests.get(settings.BASE_URL + settings.get_tg_users +
                     str(chat_id), headers=settings.master_token)
    responce = r.json()
    user_id = json.loads(json.dumps(responce['id']))
    log.info(f"request user id ({user_id}) from: {chat_id}")
    return user_id


def getData(user_id):
    r = requests.get(settings.BASE_URL + settings.get_data +
                     str(user_id), headers=settings.master_token)
    responce = r.json()
    data = json.loads(json.dumps(responce[0]['data']))
    date = utc_to_local(datetime.fromisoformat(responce[0]['datetime']), 9)
    reply_date_msg = f"Time: {date.strftime('%H:%M %d.%m.%Y')}"
    reply_data_msg = "\n".join(f'{k}: {v}' for k, v in data.items())
    return reply_date_msg + "\n" + reply_data_msg
