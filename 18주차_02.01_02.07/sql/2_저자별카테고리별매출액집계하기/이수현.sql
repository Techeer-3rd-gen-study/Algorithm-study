SELECT A.AUTHOR_ID,B.AUTHOR_NAME,A.CATEGORY,SUM(A.PRICE*TOTAL_SALES) AS SALES
FROM BOOK A 
JOIN AUTHOR B ON A.AUTHOR_ID=B.AUTHOR_ID
JOIN(SELECT
BOOK_ID,DATE_FORMAT(SALES_DATE,"%Y-%m"),SUM(SALES) AS TOTAL_SALES
FROM BOOK_SALES 
WHERE DATE_FORMAT(SALES_DATE,"%Y-%m")='2022-01'
GROUP BY 1,2)C ON A.BOOK_ID=C.BOOK_ID
GROUP BY A.AUTHOR_ID,B.AUTHOR_NAME,A.CATEGORY 
ORDER BY A.AUTHOR_ID ASC,A.CATEGORY DESC