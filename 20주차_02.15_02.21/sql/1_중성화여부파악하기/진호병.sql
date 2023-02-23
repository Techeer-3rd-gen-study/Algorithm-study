-- 코드를 입력하세요
SELECT animal_id, name, IF(SEX_UPON_INTAKE LIKE '%NEUTERED%' OR SEX_UPON_INTAKE LIKE '%SPAYED%','O','X') AS '중성화' 
from animal_ins
ORDER BY animal_id