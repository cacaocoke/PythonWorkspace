# 지역변수 : 함수 내에서만 사용, 함수 호출될때만 사용 됐다가 호출 끝나면 사라 짐
# 전역변수 : 프로그램 내에서 어디서든 부를 수 있는 변수
# 헷갈리니 챕터 한번 더 봐라

gun = 10 # 전역 변수의 참고 값

def checkpoint(soldiers): # 경계근무
    # gun = 20 # 지역 변수
    global gun # 전역 공간에 있는 gun 사용 # 앞선 선언 참고
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) # 들여쓰기 함부로 하지 말자

'''
print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
'''

# 전역 변수를 많이 쓰면 코드 관리가 어려움, 권장되지 않음
# 함수의 전달 값으로 파라미터로 던져서 계산 하고 반환 값으로 받아서 사용 하는 법을  체크

def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers # 함수 내에서는 지역 변수가 됨
    print("[함수 내] 남은 총 : {0}")
    return gun 

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun=checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))
