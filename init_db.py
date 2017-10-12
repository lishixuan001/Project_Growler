import sqlite3

conn = sqlite3.connect('growls.db')

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS growls (name, datetime, growl)")
c.execute("INSERT INTO growls VALUES ('oski', '100', 'Hello Cal Hacks!')")
c.execute("SELECT * FROM growls")
print(c.fetchall())

conn.commit()
conn.close()
