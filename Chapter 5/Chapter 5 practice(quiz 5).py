# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import * # 난수니까 빼먹지 말고 선언 해줘야 함
count = 0 # 총 탑승 승객 수
for i in range(1,51): # 1 ~ 50 이라는 승객 수
    time = randrange(5,51) # 5분부터 51분의 소요 시간
    if 5 <= time <= 15 : # [매칭 성공] 5분에서 15분 이내의 손님, 탐승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        count += 1 # 매칭되면 1만큼씩 증가
    else : # [매칭 실패]
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 : {0} 분".format(count))