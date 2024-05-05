DROP TABLE Animals;
CREATE TABLE Animals AS
SELECT
    animal_id,
    breed,
    sex,
    dob,
    dam,
    sire
FROM
    Animal;


DROP TABLE SessionAnimalActivities;
CREATE TABLE SessionAnimalActivities AS
SELECT
    session_id,
    animal_id,
    activity_code,
    when_measured
FROM
    SessionAnimalActivity;




DROP TABLE SessionAnimalTraits;
CREATE TABLE SessionAnimalTraits AS
SELECT
    session_id,
    animal_id,
    trait_code,
    alpha_value,
    alpha_units,
    when_measured
FROM
    SessionAnimaltrait;

DROP TABLE PickListValues;
CREATE TABLE PickListValues AS
SELECT
    PickList_id,
    PickListValue_id,
    value
FROM
    PickListValue;

DROP TABLE Notes;
CREATE TABLE Notes AS
SELECT
    animal_id,
    Note
FROM
    Note;

DROP TABLE MasterTraits;
CREATE TABLE MasterTraits AS
SELECT
    s.animal_id,
    s.trait_code,
    s.alpha_value,
    p.value
FROM
    SessionAnimalTraits s
JOIN
    picklistvalue p ON s.trait_code = p.picklistvalue_id;

