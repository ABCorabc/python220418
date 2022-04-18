# DemoTupleDict.py
# Tuple
tp = (1,2,3)
print(type(tp))
print(tp)
print(len(tp))
print(tp[0])

#주로 데이터를 담아서 전달
#함수 정의
def calc(a,b):
    return a+b, a*b

#호출
result = calc(3,4)
print(result)  

#한방에 입력
args = (5,6)
print(calc(*args))

#딕셔너리
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device)
print(type(device))
print(len(device))
print(device["아이폰"])

#입력
device["갤럭시폴더"] = 15
device["아이폰"] = 6
print(device)

#삭제
del device["아이폰"]
print(device)

#반복문
for item in device.items():
    print(item)