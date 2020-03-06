CREATE TABLE IF NOT EXISTS system (
  idsystem INT NOT NULL,
  name VARCHAR(45) NULL,
  size VARCHAR(45) NULL,
  PRIMARY KEY (idsystem))
;

CREATE TABLE IF NOT EXISTS system (
  idsystem INT NOT NULL,
  name VARCHAR(45) NULL,
  size VARCHAR(45) NULL,
  PRIMARY KEY (idsystem))
;

CREATE TABLE IF NOT EXISTS object (
  idobject INT NOT NULL AUTO_INCREMENT,
  system_idsystem INT NOT NULL,
  name VARCHAR(45) NOT NULL,
  radius INT NOT NULL,
  mass INT NOT NULL,
  type_idtye INT NOT NULL,
  PRIMARY KEY (idobject, type_idtye),
  INDEX fk_object_system_idx (system_idsystem ASC),
  INDEX fk_object_type1_idx (type_idtye ASC),
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
