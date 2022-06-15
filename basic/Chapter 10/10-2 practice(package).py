# 하나의 디렉토리에 모듈 여러개를 넣어 놓은 게 패키지

'''
import travel.thailand # 마지막은 모듈 또는 패키지만 불러올 수 있음
# import travel.thailand.ThailandPackage # 이 경우 불러올 수 없음
trip_to = travel.thailand.ThailandPackage() # 패키지.모듈(py제외).클래스로 불러올 것
trip_to.detail()
'''

from travel.thailand import ThailandPackage # from으로 패키지, 모듈 선택하면 import로 클래스 호출 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()