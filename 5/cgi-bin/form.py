#!/usr/bin/python3
import cgi
import html
import sqlite3

form = cgi.FieldStorage()
idobject = form.getfirst("id","1")
type_ = form.getfirst("idobject_type","0")
radius = form.getfirst("radius","1")
mass = form.getfirst("mass","1")
name = form.getfirst("name","NULL")

inp = [html.escape(x) for x in (  idobject,"0",type_,name,radius,mass)]
inp[3] = '"' + inp[3] +'"' 

conn = sqlite3.connect('example.db')
cur = conn.cursor()

sql = "INSERT INTO object (idobject,system_idsystem,type_idtye,name,radius,mass) VALUES ({},{},{},{},{},{});"
cur.execute(sql.format(*inp)) 
conn.commit()


attr = ("idobject", "o.name","radius","mass","s.name","t.name")
sql = """
select {},{},{},{},{},{} from
   (object o join system s on o.system_idsystem=s.idsystem) a
   join type t on a.type_idtye = t.idtye;
""".format(*attr)

cur.execute(sql)
result  = cur.fetchall()


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>ОТВЕТ</title>
        </head>
        <body>""")
print("""<style>table {
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid black;
}</style>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>",sql.format(*inp),"</p>")

print("<table>")
print("<tr>")
for x in result:
	print("<tr>")
	for y in x:
		print ("<td>",y,"</td>")
	print("</tr>")




print("</table>")


print("""</body>
        </html>""")