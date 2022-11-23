import streamlit as st
import sqlite3, os, time, re, pytz, json, ssl
from io import BytesIO
#from pyxlsb import open_workbook as open_xlsb
import pandas as pd
from datetime import datetime, timedelta
import urllib.request, urllib.parse, urllib.error
import requests

form1 = st.form(key="Options")
main_container = st.container()
main_container.write("")
form1.title("查单助手")
text = form1.text_area("请直接输入查单单号： ")
bt1 = form1.form_submit_button("开始 查单")

if bt1 :
    headers = {
        'authority': 'map.cluster.uniexpress.org',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'access-control-allow-credentials': 'true',
        'access-control-allow-headers': 'Origin, X-Requested-With, Content-Type, Accept, origin, content-type, accept',
        'access-control-allow-methods': 'GET, PUT, POST, DELETE, OPTIONS',
        'access-control-allow-origin': '*',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vbWFwLmNsdXN0ZXIudW5pZXhwcmVzcy5vcmcvbWFwL2xvZ2luIiwiaWF0IjoxNjY5MDkzMzQ0LCJleHAiOjE2NjkxNzk3NDQsIm5iZiI6MTY2OTA5MzM0NCwianRpIjoidGI5RVZobmRGUXNKeVNmbCIsInN1YiI6MjE3LCJwcnYiOiJlOGNmNTQ2ZTZiNTNmMmIxOWY3ZTQ1OWJkMzEyZjcxMTQwODkxMzllIiwiaWQiOjIxNywibW9kZWwiOiJlY3NfY3NfYWNjb3VudCIsInJvbGVzIjpbIkRyaXZlciBBZG1pbmlzdHJhdG9yIiwiSW5jaWRlbnQgTWFuYWdlbWVudCJdLCJ1aV9hYmlsaXRpZXMiOlsxLDIsMyw0LDUsNiw3LDgsOSwxMCwxMSwxMiwxMywxNSwxNiwxNywxOCwxOSwyMiwyMywzMDEsMzAzLDMwMiwzMDQsMzIsMjcsMzFdLCJ3YXJlaG91c2UiOlsiMiIsIjIwIiwiMTAiLCI5Il0sInVzX2ZsYWciOmZhbHNlfQ.mYsEWO_TU9JfMTq8BRa18GmvWYW7v8txJAYqCqX47L0',
        'origin': 'https://unimap.cluster.uniexpress.org',
        'referer': 'https://unimap.cluster.uniexpress.org/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    #x = 'MBORDU7012624903'
    params = {
        'tno': text,
    }

    response = requests.get('https://map.cluster.uniexpress.org/map/getorderdetail', params=params, headers=headers)
    js = json.loads(response.content)
    st.write(js)
