# ifelse.py
#다중 라인 주석 처리 : ctrl + /

# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score <= 90:
#     grade = "B"    
# elif 70 <= score <= 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

#반복구문
value = 5
while value > 0:
    print(value)
    value -= 1

print("전체 실행 종료")

lst = ["문자열", 100, 3.14]
for item in lst:
    print(item, type(item))

print(len(lst))    