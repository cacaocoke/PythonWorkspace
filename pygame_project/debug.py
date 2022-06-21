''' 2중 for 문 빠져 나오는 법 '''

balls = [1,2,3,4]
weapons = [11,22,3,44]

for ball_idx, ball_val in enumerate(balls):
    print("ball :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons: ", weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print("공과 무기가 충돌")
            break # break가 두번째 for문만 탈출하므로 첫번째 for문은 계속 진행 됨
    else : 
        continue
    print("바깥 for 문 break")
    break

    # if 조건:
    #     동작
    # else : 
    #     그 외의 동작
    