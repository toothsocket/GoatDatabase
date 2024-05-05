CREATE VIEW animal_weights_view AS
SELECT 
    animal_id,
    last_weight,
    last_weight_date,
    sex
FROM 
    Animal;

This transaction requires entity integrity (the goats need to exist for their weights to be gathered). It shows the animal (indicated by animal ID), their last weight and the date of it, and their sex.

*******************************************Baseline********************************************************
CREATE VIEW animals AS 
SELECT
animal_id, 
breed, 
sex, 
dob, 
dam, 
Sire
FROM
	Animal;

This gives a view of the animal with their respective mother and father. This will be useful when doing application side functions like creating the family tree.
******************************************************************************

CREATE VIEW animals_traits AS 
SELECT
animal_id, 
trait_code, 
alpha_value, 
alpha_unit, 
FROM
	Session_animal_traits

This pulls up specific animal traits for a specific goat. It will be useful when the user wants to know something specific about a goat (like the color or breed)

******************************************************************************

CREATE VIEW goat_lineage AS
SELECT 
    animal_id,
    breed,
    sex,
    dam,
    sire
FROM 
    animal
WHERE 
    breed = '????????????????';


– This transaction requires entity integrity (the goats need to exist for their traits and family trees to be gathered). It shows the animal (indicated by animal ID), their sex, mother, father, and breed. The “breed” clause is one example where a view could be made based on a specific trait the user wants to look at. Here, the transaction constraint is the breed must be whatever specified breed is wanted (it would replace the x’s). –




