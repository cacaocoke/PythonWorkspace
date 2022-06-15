# while (반복문)

'''스타벅스에서 손님을 5번 불렀는데 대답이 없는 경우 커피를 버리는 정책을 시행한다고 가정'''
# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요).".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}) 회".format(customer, index))
#     index +=1 #무한 루프 예시
    
customer = "토르"
person = "Unknown"

while person != customer : #!=는 질의애 대한 응답이 아님을 의미
        print("{0}, 커피가 준비 되었습니다.".format(customer))
        person = input("이름이 어떻게 되세요?") # 예시 기준 person 값을 물어 보는데 customer 값이 아니면 반복, 맞으면 종료