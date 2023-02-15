-- 코드를 입력하세요
SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth,'%Y-%m-%d') AS "date_of birth" from member_profile
where MONTH(date_of_birth) = 03 AND tlno is not null AND gender = "W"
order by member_id