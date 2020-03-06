#!/usr/bin/python3
import cgi
import html
import sqlite3

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1","не задано")
text1 = html.escape(text1)



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>ОТВЕТ</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))





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
	print(x,"<br>")

print("""</body>
        </html>""")