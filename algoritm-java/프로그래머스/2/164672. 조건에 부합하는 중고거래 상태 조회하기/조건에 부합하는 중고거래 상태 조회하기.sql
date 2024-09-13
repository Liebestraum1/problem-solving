-- 코드를 입력하세요
SELECT      BOARD_ID, WRITER_ID, TITLE, PRICE,
        CASE STATUS
            WHEN 'SALE' THEN '판매중'
            WHEN 'RESERVED' THEN '예약중'
            WHEN 'DONE' THEN '거래완료'
        END AS STATUS
FROM        USED_GOODS_BOARD
WHERE       DATE_FORMAT(CREATED_DATE, '%y%m%d') = '221005'
ORDER BY    BOARD_ID DESC;