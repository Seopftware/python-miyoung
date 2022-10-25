# def name():
#     print("이름 함수 호출")
# name()

# def sum(a,b):
#     print("a+b")
#     print(a+b) # 7
#     return a+b

# total = sum(3,4)    
# print("total")
# print(total) # None


# Q.성적과 이름을 입력하고, 성적에 따른 등급을 알려주는 프로그램을 만드시오.
# 단, 함수를 사용하시오.

# 90점 이상 A등급
# 80점 이상 B등급
# 70점 이상 C등급
# 60점 이상 D등급
# 60점 미만 F등급

# grade = ""
# def check_grade(성적):
#     if 성적 >=90:
#         grade = 'A'
#     elif 성적 >=80:
#         grade = 'B'
#     return grade
    
# a = check_grade(100)
# print(a)

# range(1,10)
# len()
# print()
# int()

# a = "python"
# a = a.upper()
# "Python", "python"
# print(a)

import random

# b = random.random(1,10)
# print(b)

# a = [1,2,3]
# random.shuffle(a)

import sys
print(sys.argv) # 파이썬 실행시 파일 뒤에 붙여준 어떠한 값들이 리스트의 값으로 추가됨.
sys.path # 파이썬 라이브러리들이 설치되어 있는 위치
print(sys.version) # 파이썬 버전

import os
print(os.getcwd())

from datetime import datetime
os.mkdir(datetime.now().strftime("%Y-%m-%d")) # 폴더생성

import module
module.name("인섭")