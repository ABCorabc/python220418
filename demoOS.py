# demoOS.py

from os.path import *

print(abspath("python.exe"))
print(basename("python.exe"))
print(getsize("C:\\python39\\python.exe"))
print(exists("C:\\python39\\python.exe"))
print(isfile("C:\\python39\\python.exe"))

#운영체제정보
from os import *
print("운영체제이름:", name)
#다른 실행파일 실행
#system("notepad.exe")

#파일 리스트
import glob
print(glob.glob("c:\\work\\*.py"))