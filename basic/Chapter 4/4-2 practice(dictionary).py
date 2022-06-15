cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 함수 내 번호를 불러올땐 [] 사용
print(cabinet[100])

print(cabinet.get(3)) #get 사용 할때는 () 사용
# print(cabinet[5]) # [] 사용 시 지정 값이 없으면 오류 후 종료
print(cabinet.get(5)) # get 사용 시 지정 값이 없으면 none 출력 후 프로그램 이어서 실행
print(cabinet.get(5, "사용 가능")) # get 사용 시 특정 문자열도 삽입하여 출력 가능
print("hi")

print(3 in cabinet) # 사전 자료 안에 어떤 자료가 있는 지 확인 '키 in 변수' True 나와야 함
print(5 in cabinet) # False 나와야 함

cabinet = {"A-3" : "유재석", "B-100" : "김태호"} # String도 사용 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호" # 새로운 손님을 새로운 항번에 부여
cabinet["A-3"] = "김종국" # 부여 된 항번에 새로운 이름 부여시 최종 입력값을 기준으로 업데이트 하여 출력 함, 유재석 자리에 김종국이 출력 됨
print(cabinet)

# 간 손님
del cabinet["A-3"] # del 명령어로 부여된 값을 지울 수 있음
print(cabinet)

# key 들만 출력
print(cabinet.keys()) # keys 출력, A-3을 지웠으므로 B-100과 C-20이 출력 되어야 함

# value 들만 출력
print(cabinet.values()) # values 출력, 항번에 부여된 값만 출력, 김태호, 조세호 출력되어야 함

# key, value 쌍으로 출력
print(cabinet.items()) # items 사용 시 모두 출력 항번과 값이 같이 나와야 함

# 목욕탕 폐점
cabinet.clear() # clear 사용 시 모두 삭제, ()로 닫아 줘야 함
print(cabinet)