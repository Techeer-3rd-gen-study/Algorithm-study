select MCDP_CD as '진료과코드', count(MCDP_CD) as '5월예약건수'
from APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%' # LIKE '%'는 문자열 부분일치 검색
group by MCDP_CD
order by count(MCDP_CD) ASC, MCDP_CD ASC;
