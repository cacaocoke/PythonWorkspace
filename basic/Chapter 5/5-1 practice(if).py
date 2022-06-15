# 상황에 맞는 코드를 실행

# 조건에 맞으면 명령문 실행
# weather = "비"
# weather = "미세먼지"
# weather = "맑음"
'''
weather = input("오늘 날씨 어때요? ")
'''
# if 조건 :
#     실행 명령문 

# '=' 기호는 반드시 2개 입력
# if weather == "비" :
# if weather == "미세먼지" :
'''
if weather == "비" or weather =="눈" : # 변수가 if 조건에 맞을 경우 아래 문구 출력 # 조건 추가 할때는 or 입력 후 변수 선언 한 뒤 추가 조건 입력
    print("우산을 챙기세요")  
elif weather == "미세먼지" : # 변수가 없을 경우 elif 조건을 비교해서 하단 문구 출력
    print("마스크를 챙기세요")
else : # 변수가 if 또는 elif 모두 해당이 안될 경우 출력
    print("준비물 필요 없어요.")
'''

temp = int(input ("기온은 어때요? ")) # 숫자일 경우 'int'로 감쌈
if 30 <= temp :
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp <30 :  # 범위값을 입력할땐 양 끝단 사이에 'and' 입력하는 방법이 있음
    print("괜찮은 날씨에요")
elif 0<= temp <10 : # 하지만 'and' 값이 필수는 아님
    print("쌀쌀해요, 외투를 챙기세요")
else :
    print("너무 추워요, 밖에 나가지 마세요")