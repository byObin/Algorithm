SELECT A.PRODUCT_ID, A.PRODUCT_NAME, (SUM(B.AMOUNT) * A.PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT A
JOIN FOOD_ORDER B ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE B.PRODUCE_DATE LIKE '2022-05%'
GROUP BY A.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID