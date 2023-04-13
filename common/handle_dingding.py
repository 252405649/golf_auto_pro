"""
==========================
Author:sunk123
Time:2022-07-26 16:51
Company:力石科技有限公司
==========================
"""
import time
import hmac
import hashlib
import base64
import urllib.parse
from dingtalkchatbot.chatbot import DingtalkChatbot

class Dingding(object):
    def get_sign(self, timestamp):
        # timestamp = str(round(time.time() * 1000))
        secret = 'this is secret'
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        print(timestamp)
        print(sign)
        return sign
if __name__ == '__main__':
    dd = Dingding()
    timestamp = str(round(time.time() * 1000))
    dd.get_sign(timestamp)

