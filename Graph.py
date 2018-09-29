#!/usr/bin/env python3


from code import SQL
import datetime
from matplotlib import pyplot as plt

sql = SQL('test.db')

target_good = "steam"

data = sql.cursor.execute(f"SELECT * FROM data WHERE name='{target_good}'").fetchall()

x = []
y = []

for row in data:
    # print(row)

    x.append( datetime.datetime.fromtimestamp(row['timestamp']/1000) )
    y.append(row['amount'])
fig, ax = plt.subplots()

plt.plot(x,y)
plt.ylabel(target_good.title())
plt.ylim(bottom=0)
ax.set_yscale('symlog')
fig.autofmt_xdate()
plt.grid()
plt.show()