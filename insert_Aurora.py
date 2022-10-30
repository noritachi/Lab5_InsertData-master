import insertUtil as ut
import MySQLdb

conn = MySQLdb.connect(host='database-aurora.cluster-c1fgj4kohtt1.us-east-1.rds.amazonaws.com', user='admin', passwd='12345678', db='covid19_aurora', port=3306)
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')


