absent = [2,4,5] # 결석자 번호
no_book = [7] # 책을 안가져 온 학생
for student in range(1, 11) : #1~10번 까지 출석 번호
    if student in absent : # if 이후 continue 사용 예시
        continue # continue 만날 경우 다음 행으로 넘어가지 않고 이전행을 반복, 이때 선행 변수 지정값 스킵 이후 range내 모든 순번 이어서
    elif student in no_book :
        print("오늘 수업은 여기까지, {0}는 교무실로 따라와.".format(student))
        break # 후 순번이 있거나 말거나 반복문 탈출
    print("{0}번, 책을 읽어봐".format(student))
