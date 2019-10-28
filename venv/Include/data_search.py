import sqlite3



conn = sqlite3.connect("testDB.db")


cursor = conn.cursor()


cursor.execute('select * from eth_usdt_data')
conn.commit()
a = cursor.fetchall()
print(a[2])