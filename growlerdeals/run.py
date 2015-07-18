from pygeocoder import Geocoder

import psycopg2

try:
    conn = psycopg2.connect("dbname='django' user='django' host='' password='uPYBQtVnSF'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
try:
    cur.execute("""SELECT * from growlerdeals_brewery""")
except:
    print "I can't SELECT from growlerdeals_brewery"
rows = cur.fetchall()
for row in rows:
    print "   ", row['brewery_name'][1]