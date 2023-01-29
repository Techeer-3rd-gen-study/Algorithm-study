-- 코드를 입력하세요
SELECT product_code, SUM(price * sales_amount) AS SALES 
from product AS a
INNER JOIN offline_sale AS b
ON a.product_id = b.product_id
GROUP BY product_code
ORDER BY SALES DESC, product_code
