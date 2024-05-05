--- The sires of the goats whos BWT was greater than 5

SELECT a.sire, COUNT(*) as offspring_count
FROM Animals a
JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
WHERE s.trait_code = 357 -- BWT trait code
  AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 5.0
      ELSE FALSE
      END
  AND s.alpha_value IS NOT NULL
  AND (a.sire IS NOT NULL AND a.sire<> '')
GROUP BY a.sire;

---The sires of the goats who’s BWT was greater than 8 

SELECT a.sire, COUNT(*) as offspring_count
FROM Animals a
JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
WHERE s.trait_code = 357 -- BWT trait code
  AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 8.0
      ELSE FALSE
      END
  AND s.alpha_value IS NOT NULL
  AND (a.sire IS NOT NULL AND a.sire<> '')
GROUP BY a.sire;






--- The dam of the goats whos BWT was greater than 5 

SELECT a.dam, COUNT(*) as offspring_count
FROM Animals a
JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
WHERE s.trait_code = 357 -- BWT trait code
  AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 5.0
      ELSE FALSE
      END
  AND s.alpha_value IS NOT NULL
  AND (a.sire IS NOT NULL AND a.sire<> '')
GROUP BY a.dam;

--- The dam of the goats whos BWT was greater than 8

SELECT a.dam, COUNT(*) as offspring_count
FROM Animals a
JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
WHERE s.trait_code = 357 -- BWT trait code
  AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 8.0
      ELSE FALSE
      END
  AND s.alpha_value IS NOT NULL
  AND (a.sire IS NOT NULL AND a.sire<> '')
GROUP BY a.dam;






--- Parent of goats who’s BWT was greater than 5

SELECT a.sire, a.dam, COUNT(*) as offspring_count
FROM Animals a
JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
WHERE s.trait_code = 357 -- BWT trait code
  AND CASE
      WHEN s.alpha_value ~ '^[+-]?[0-9]*\.?[0-9]+$' THEN s.alpha_value::numeric > 5.0
      ELSE FALSE
      END
  AND s.alpha_value IS NOT NULL
  AND (a.sire IS NOT NULL AND a.sire <> '')
  AND (a.dam IS NOT NULL AND a.dam <> '')
GROUP BY a.sire, a.dam;

--- view All the good graft goats

SELECT a.dam, COUNT(s.animal_id) AS total_grafted_goats
FROM Animals a
JOIN sessionanimaltrait s ON a.animal_id = s.animal_id
WHERE s.trait_code = 735
GROUP BY a.dam
ORDER BY total_grafted_goats DESC;

--- Pregnant Dams that have previously had a baby goat over 7 pounds

WITH PregnantDams AS (
    SELECT animal_id
    FROM sessionanimaltrait
    WHERE trait_code = 847
),
OffspringOver7lbs AS (
    SELECT animal_id
    FROM sessionanimaltrait
    WHERE trait_code = 357
      AND CASE 
          WHEN alpha_value ~ '^\s*$' THEN FALSE -- Excludes empty strings and strings with only whitespace
          WHEN alpha_value ~ '^[+-]?[0-9]+(\.[0-9]+)?$' THEN alpha_value::numeric > 10
          ELSE FALSE
      END
)
SELECT DISTINCT s.animal_id, s.dam
FROM Animals s
JOIN Pregnantdams p ON s.animal_id = p.animal_id
JOIN OffspringOver7lbs o ON s.animal_id = o.animal_id;

