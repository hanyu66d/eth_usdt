import sqlite3
from data_get import eth_usdt_data_get
import time


conn = sqlite3.connect("testDB.db")


cursor = conn.cursor()

while True:
    a = eth_usdt_data_get()
    cursor.execute(
        "insert or ignore into eth_usdt_data (time,best_ask,best_bid,last ,ask,bid,open_24h,high_24h,low_24h,base_volumn_24h,quote_volume_24h)" \
        "values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
            .format(a['timestamp'], float(a['best_ask']), float(a['best_bid']), float(a['last']),
                    float(a['ask']), float(a['bid']), float(a['open_24h']), float(a['high_24h']),
                    float(a['low_24h']), float(a['base_volume_24h']), float(a['quote_volume_24h'])))
    # print((float(a['best_ask']) + float(a['best_bid'])) / 2)
    sql = "select * from eth_usdt_data"
    cursor.execute(sql)
    conn.commit()
    a = cursor.fetchall()

    print(len(a))
    time.sleep(9)

    

conn.close()