import insertUtil as ut
import psycopg2

conn = psycopg2.connect(database='covid19_postgresql', user='postgres', password='12345678', host='database-postgresql.cbhm0ux6rqan.us-east-1.rds.amazonaws.com', port='5432')
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')