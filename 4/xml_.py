import sqlite3
import xml.etree.cElementTree as ET

conn = sqlite3.connect('example.db')
cur = conn.cursor()
attr = ('idobject','name','radius','mass','system_idsystem','type_idtye')
cur.execute("SELECT {},{},{},{},{},{} FROM object".format(*attr))
result = cur.fetchall()
dic = []
for x in result:
	dic.append(list(zip(attr,x))) 

print(result)
print(dic)

# Create xml
root = ET.Element("root")
for i,elem in enumerate(dic):
	i_leaf = ET.SubElement(root, "spaceObject")
	
	print(elem)
	for a in elem:
		i_leaf.set(a[0],str(a[1]))

tree = ET.ElementTree(root)
tree.write("result.xml")