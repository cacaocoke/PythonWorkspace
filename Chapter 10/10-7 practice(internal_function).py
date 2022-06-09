# 내장 함수는 내장되어 있어 임포트 할 필요 없이 사용할 수 있는 함수
# input : 사용자 입력을 받는 함수
'''
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))
'''

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
'''
print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())
'''
#import random

#print(dir(random)) # 괄호 안의 모듈 내에서 쓸 수 있는 함수 전체 표시

#lst = [1,2,3]
#print(dir(lst))

name = "Jim"
print(dir(name))

# 구글에 list of python builtins 검색하면 내장 함수 볼 수 있음