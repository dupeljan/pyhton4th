import xml.etree.ElementTree as ET
import sqlite3


conn = sqlite3.connect('example.db')
cur = conn.cursor()
attr = ('idobject','name','radius','mass','system_idsystem','type_idtye')

INPUT = "result.xml"
tree = ET.parse(INPUT)
root = tree.getroot()
for child in root.iter("spaceObject"):
	print(child.attrib)
	res = child.attrib
	res['name'] = "\"" + res['name']  + "\"" 
	keys = ",".join(list(res.keys()))
	vals = ",".join(list(res.values()))
	cur.execute("INSERT OR REPLACE INTO object ("+keys+") VALUES ("+vals+");")
	result = cur.fetchall()

conn.commit()
conn.close()
	

