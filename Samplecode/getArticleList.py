#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
import urllib
import hashlib
import json
# Key Setting
access_key = 'replace_your_accesskey_here1'
secret_key = 'replace_your_accesskey_here1'
# GetTimestamp
ts = int(time.time())
# Define httpParams
httpParams = \
 'access_key=' + access_key + \
 '&date=' + str(ts) + \
 '&secret_key=' + secret_key
hl = hashlib.md5()
hl.update(httpParams.encode(encoding='utf-8'))
md5_key = hl.hexdigest()
md5_key = urllib.parse.quote(md5_key)
# Set signString
signString = {
    'access_key': access_key,
    'date': ts,
    'sign': md5_key
}
# getData
r = requests.get('http://api.coindog.com/topic/list?', params=signString)
r = r.json()
print(r)
# writeData
with open('Data.json', 'w') as f:
    json.dump(r, f)
