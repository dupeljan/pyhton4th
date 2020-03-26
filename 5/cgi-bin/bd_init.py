import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()
sql =list()
sql.append( """
CREATE TABLE IF NOT EXISTS system (
  idsystem INT PRIMARY KEY,
  name VARCHAR(45) ,
  size REAL 
  );

"""
)

sql.append(
"""
-- -----------------------------------------------------
-- Table type
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS type (
  idtye INT PRIMARY KEY,
  name VARCHAR(45));
"""
)
sql.append(
"""
-- -----------------------------------------------------
-- Table object
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS object (
  idobject INT PRIMARY KEY,
  system_idsystem INT NOT NULL,
  name VARCHAR(45) NOT NULL,
  radius REAL NOT NULL,
  mass REAL NOT NULL,
  type_idtye INT NOT NULL,
  CONSTRAINT fk_object_system
    FOREIGN KEY (system_idsystem)
    REFERENCES system (idsystem)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_object_type1
    FOREIGN KEY (type_idtye)
    REFERENCES type (idtye)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""
)

for s in sql:
	print("------compile------")
	print(s)
	cur.execute(s)
conn.commit()
conn.close()
#for x in sql:
#	cur.execute()