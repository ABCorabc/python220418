# db2.py 
import sqlite3

#연결객체를 만들기
#파일에 데이터베이스를 저장
#con = sqlite3.connect("c:\\work\\test.db")
con = sqlite3.connect("c:\\work\\test2.db")
#구문을 수행할 커서 객체 
cur = con.cursor() 
#테이블 구조(테이블 스키마):SQL구문은 대소문자 구분안함. 

cur.executemany("insert into PhoneBook values (?, ?);", datalist)
#검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

