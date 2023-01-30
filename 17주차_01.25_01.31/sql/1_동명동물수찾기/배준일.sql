select NAME, count(NAME) as 'count'
from ANIMAL_INS
group by NAME 
having count(NAME) >= 2 
order by NAME;

# where은 group by 로 묶이기 전에 조건을 처리하고 묶는다. / 집계함수 이용 불가능
# having은 group by로 묶이고 조건을 처리한다. / 집계함수 이용 가능