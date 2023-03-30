from datetime import datetime
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
import environ
import logging
import hashlib
import json


log = logging.getLogger(__name__)

env = environ.Env()
environ.Env.read_env()

def get_var(val, default=None):
    try: return env(val)
    except: return default

def send_email(*args, **kwargs):
    pass

def get_now_date_time():
    return datetime.now()

jsonDec = json.decoder.JSONDecoder()

def getMD5(data):
    return hashlib.md5(data.encode()).hexdigest()

def timeNow():
    return timezone.localtime()

def timeAfter(days=0,hours=0,minutes=0):
    return datetime.datetime.now()+datetime.timedelta(days=days, hours=hours, minutes=minutes)

def timeBefore(days=0,hours=0,minutes=0):
    return datetime.datetime.now()-datetime.timedelta(days=days, hours=hours, minutes=minutes)

def dateDiff(_from, _to):
    return (_from-_to).days

def json_to_str(value):
    return json.dumps(value)
    
def str_to_json(value):
    return json.loads(value)
    
def list_to_str(value):
    return json.dumps(value)

def str_to_list(value):
    return jsonDec.decode(value)

def getUserFromUsername(username):
    try: return get_user_model().objects.get(username=username)
    except: return None

def getUserFromUid(id):
    try: return get_user_model().objects.get(id=id)
    except: return None
