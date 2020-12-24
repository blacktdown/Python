"""
날짜 : 2020/12/24
이름 : 박준우
내용 : 파이썬 데이터베이스 프로그래밍
"""

import pymysql as db

# 1단계 - 데이터베이스 접속
conn = db.connect(host='192.168.10.114',
                  user='pjw',
                  password='1234',
                  db='pjw',
                  charset='UTF8')

# 2단계 - 쿼리문 실행객체 생성
cursor = conn.cursor()

# 3단계 - 쿼리문 실행
sql = "DELETE FROM `USER1` WHERE `uid`='P101';"
cursor.execute(sql)

# 4단계 - 쿼리문 실행 확정 단계
conn.commit()

# 5단계 - 데이터베이스 종류
conn.close()

print('DELETE 완료...')