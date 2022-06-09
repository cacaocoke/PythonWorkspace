# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 을 활용

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
#  -- 축하합니다 --

#  (활용 에제)
# from random import * # random 모듈 임포트 명령
# list = [1,2,3,4,5]
# print(list)
# shuffle(list)
# print(list)
# print(sample(list,1))

from random import *
coders=range(1,21) # range 함수 사용 하면 범위 내 숫자 지정 가능,뒷자리는 작성 숫자 이전 숫자 까지
print(type(coders)) # range 에는 shuffle 등의 함수를 사용할 수 없음
coders=list(coders)
print(type(coders))
shuffle(coders)
print(coders)

winners=sample(coders, 4) # 4명 중에서 1명은 치킨, 3명은 커피



print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0])) # format 앞에는 '.' 꼭 찍어야 함
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")