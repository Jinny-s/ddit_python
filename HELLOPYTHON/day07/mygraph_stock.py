from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql
import random

conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()
def getPrices(s_name):
    ret = []
    sql = "select s_price from stock where s_name = '{}' order by crawl_date".format(s_name)
    
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
        
    return ret

names = []
sql = "select s_name from stock group by s_code"

curs.execute(sql)
rows = curs.fetchall()

fig = plt.figure()
ax = plt.axes(projection='3d')

for row in rows:
    names.append(row[0])

for i, name in enumerate(names):
    r = random.random()
    g = random.random()
    b = random.random()
    color = (r, g, b)
    
    a = np.array(getPrices(name))
    
    z = a / a[0]
    x = np.array([1,1,1,1,1,1,1,1,1,1])
    y = np.array([0,1,2,3,4,5,6,7,8,9])
    ax.plot3D(x+i, y, z, c = color)

conn.close()

ax.set_title('Stock Flow')
plt.show()