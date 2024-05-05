(INSERTING NEW ENTRY OF GOATS INTO DATABASE)

CREATE TABLE animals (
	animal_id int,
	breed varchar(255),
	sex varchar(255),
	dob varchar(255),
	dam varchar(255),
sire varchar(255) 
);

CREATE TABLE session_animal_activites (
	session_id int,
	animal_id int,
	activity_code varchar(255),
	when_measured varchar(255)
);

CREATE TABLE session_animal_traits (
	session_id int,
	animal_id int,
	trait_code varchar(255),
	alpha_value varchar(255),
	alpha_unit varchar(255),
	when_measured varchar(255)
);



CREATE TABLE PickListValue(
	PickList_Value int,
	PickList_Value_ID int,
	Note_varchar(255)
);
	


CREATE TABLE Note(
	Animal_id varchar(255);
	Note varchar(255);
);


INSERT INTO animals (animal_id, breed, sex, dob, dam, sire)
VALUES (?, ?, ?, ?, ?, ?);

UPDATE animals
SET animal_id = ‘?’, breed, sex = ‘?’ , dob = ‘?’, dam = ‘?’, sire = ‘?’
WHERE animal_id = ‘?’;

INSERT INTO session_animal_traits  (session_id, trait_code, alpha_value, alpha_unit, when_measured)
WHERE animal_id = ‘?’
VALUES (?, ?, ?, ?, ?);

UPDATE session_animal_traits
SET session_id = ‘?’, trait_code = ‘?’ , alpha_value  = ‘?’, alpha_unit = ‘?’, sire = ‘?’, when_measured = ‘?’
WHERE animal_id = ‘?’;

INSERT INTO session_animal_activites (session_id, animal_id, activity_code, when_measured)
VALUES (?, ?, ?, ?);

UPDATE session_animal_activites
SET session_id = ‘?’, activity_code = ‘?’ , when_measured  = ‘?’
WHERE animal_id = ‘?’;

INSERT INTO picklist_value (PickList_Value, PickList_Value, Note) 
VALUES (?, ?, ?);
UPDATE picklist_value
SET value  = ‘?’
WHERE PickList_Value = ‘?’ AND PickList_Value_ID = ‘? ;

(INSERTING NEW ENTRY OF SESSION INTO DATABASE)

INSERT INTO 








