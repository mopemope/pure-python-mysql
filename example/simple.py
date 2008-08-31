import pymysql


conn = pymysql.connect(host='localhost', port=3306, user='ma2', \
        password='ma2',db='sample')
#conn.query("show tables")
cur = conn.cursor()
#cur.execute("set names utf8")

print cur.execute("select * from users")
#row = cur.execute("select * from users;select * from users")

print cur.description

r = cur.fetchall()
print r

#print cur.nextset()
#r = cur.fetchall()
#print r
#print r[0], r[1]

#cur.close()
#conn.close()


#reslt = cur.fetchall()
#print reslt



