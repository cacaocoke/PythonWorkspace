'''
import theater_module
theater_module.price(3) # 3명이서 영화보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조할인 보러 갔을 때
theater_module.price_soldier(5) # 5명의 군인이 영화보러 갔을 때
'''

'''
import theater_module as mv # as 뒤에 붙인 말로 호출 됨(일종의 별명)
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
'''

'''
from theater_module import * # 모듈 내 모든 내용을 사용하겠다
# form random import *
price(3)
price_morning(4)
price_soldier(5)
'''

'''
from theater_module import price, price_morning # 원하는 함수 만 불러올 수 있음

price(5)
price_morning(6)
# price_soldier(6) # 모듈이 불러와 지지 않았기 때문에 오류가 남
'''

from theater_module import price_soldier as price # as 를 이용 해 기존 함수 값도 원하는 별칭으로 지정 가능 기존에 선언 된 함수도 무시
price(5)
