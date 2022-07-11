# 모듈 추가
import sqlite3

# 데이터베이스 열기
conn = sqlite3.connect('C:/Users/hyun/python/python_basic/part2/python_advanced/myvenv/Chapter05/SQL_DDL.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
DELETE_SQL = "DELETE FROM item WHERE code='A00002';"

# SQL 명령 실행
cur.execute(DELETE_SQL)

# 커밋
conn.commit()

# 데이터베이스 닫기
conn.close()
    