import sqlite3

import time


conn = sqlite3.connect("testDB.db")


cursor = conn.cursor()
cursor.execute('drop table eth_usdt_data')
sql = "create table eth_usdt_data (time varchar(40) primary key,best_ask float ,best_bid float ,last float ,ask float, " \
      "bid float ,open_24h float ,high_24h float ,low_24h float,base_volumn_24h float ,quote_volume_24h float )"

cursor.execute(sql)