import requests
import json
# import pandas as pd
import csv
import time
# from data_get import get_deep_size
import urllib3

def eth_usdt_data_get():
    URL = 'https://www.okex.me'
    GET_TICK_ETH_USDT = '/api/spot/v3/instruments/eth-usdt/ticker'
    requests.adapters.DEFAUTL_RETRIES = 5
    s = requests.session()
    # s.mount('https://', MyAdapter())
    s.keep_alive = False
    requests.packages.urllib3.disable_warnings()
    eth_usdt = requests.get(URL + GET_TICK_ETH_USDT, verify=False)
    a = json.loads(eth_usdt.text)
    return a


