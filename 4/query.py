import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()

attr = ("idobject", "o.name","radius","mass","s.name","t.name")
sql = """
select {},{},{},{},{},{} from
   (object o join system s on o.system_idsystem=s.idsystem) a
   join type t on a.type_idtye = t.idtye;
""".format(*attr)

cur.execute(sql)
resutl  = cur.fetchall()
print(attr)
for x in resutl:
	print(x)
