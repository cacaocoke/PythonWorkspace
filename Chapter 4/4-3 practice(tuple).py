# 튜플은 리스트와 다르게 내용 변경이나 추가 할 수 없음, 대신 속도가 리스트 보다 빠름, 변경없는 목록 사용 시 튜플 사용
menu = ("돈까스", "치즈까스") # 튜플 사용 시 '()' 이용하여 열고 닫고 ','로 구분하여 값 입력
print(menu[0]) # 0번째 메뉴 출력
print(menu[1]) # 1번째 메뉴 출력

# menu.add("생선까스") # tuple은 add를 지원하지 않음

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "hobby") # tuple 사용 시 여러 번수를 한 줄로 선언 및 출력 가능
print(name,age,hobby)