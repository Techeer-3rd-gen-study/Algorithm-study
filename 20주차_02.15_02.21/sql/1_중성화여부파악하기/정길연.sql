SELECT ANIMAL_ID, NAME,
    CASE 
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' 
            OR SEX_UPON_INTAKE LIKE '%Spayed%'
        THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE '%Intact%'
        THEN 'X'
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID