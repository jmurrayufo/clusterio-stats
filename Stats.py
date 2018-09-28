#!/usr/bin/env python3

from code import Gather
from code import SQL
import datetime

sql = SQL('test.db')
sql.generate_tables()
data = Gather().pull()

for row in data:
    # {'instanceID': '-1218240877', 'timestamp': 1538077885360, 
    # 'data': {'cellulose-fiber': '71', 'raw-wood': '26', 'solid-compost': '7', 'solid-mud': '7', 'solid-soil': '7', 'tree-seed': '2', 'wood-pellets': '9', 'steam': '759', 'water': '1229', 'water-heavy-mud': '1560', 'water-viscous-mud': '1560'},
    # '_id': 'dc5dc2aa'}
    print(row)
    # print(row['timestamp']/1000)
    ts = row['timestamp']
    # print(datetime.datetime.fromtimestamp(row['timestamp']/1000))
    for good in row['data']:
        print(good, row['data'][good])
        sql.save_element(row['instanceID'], row['_id'], ts, good, row['data'][good])