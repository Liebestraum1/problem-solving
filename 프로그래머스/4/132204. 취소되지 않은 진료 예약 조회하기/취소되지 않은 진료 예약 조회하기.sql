# 2022년 4월 13일 취소되지 않은 CS 진료 예약 내역
# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
SELECT ap.APNT_NO, pt.PT_NAME, pt.PT_NO, dr.MCDP_CD, dr.DR_NAME, ap.APNT_YMD AS APNT_YMD
FROM APPOINTMENT AS ap
INNER JOIN
    DOCTOR AS dr
    ON ap.MDDR_ID = dr.DR_ID
INNER JOIN
    PATIENT AS pt
    ON ap.PT_NO = pt.PT_NO
WHERE ap.APNT_CNCL_YN = 'N' AND dr.MCDP_CD = 'CS' AND APNT_YMD LIKE '2022-04-13%'
ORDER BY APNT_YMD;