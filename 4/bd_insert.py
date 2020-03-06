import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()
sql =list()
sql.append("INSERT INTO system (idsystem,name,size) VALUES (0,\"Solar System\",1);")
sql.append("INSERT INTO type (idtye,name) VALUES  (0,\"Planet\");")
sql.append("INSERT INTO type (idtye,name) VALUES  (1,\"Star\");")
sql.append("INSERT INTO type (idtye,name) VALUES  (2,\"Satellite\");")
sql.append("INSERT INTO type (idtye,name) VALUES  (3,\"Dwarf Planet\");")

for s in sql:
	print("------compile------")
	print(s)
	cur.execute(s)

objects = [
	(0,1,'"Sun"',696,332946),
	(0,0,'"Mercury"',2,0.055),
	(0,0,'"Venus"',0.95,0.815),
	(0,0,'"Earth"',1,1),
	(0,2,'"Moon"',0.0273,0.0123),
	(0,0,'"Mars"',0.532,0.107),
	(0,0,'"Jupiter"',11.209,317.8),
	(0,0,'"Saturn"',9.449,95.159),
	(0,0,'"Uranus"',4.007,14.536),
	(0,0,'"Neptune"',3.883,17.147),
	(0,3,'"Pluto"',0.1868,0.00218),
]
sql = "INSERT INTO object (idobject,system_idsystem,type_idtye,name,radius,mass) VALUES ({},{},{},{},{},{});"
for i,o in enumerate(objects):
	print("------compile------")
	print(sql.format(i,*o))
	cur.execute(sql.format(i,*o)) 

conn.commit()
conn.close()

