# 자료 구조의 변경
# 커피샵
menu ={"커피","우유", "주스"}
print(menu, type(menu)) # type 이용 시 class를 구분하여 보내 줌 'set' 출력 해야 함 {}로 구분 됨

menu = list(menu)
print(menu,type(menu)) # class 'list' 출력 해야 함 []로 구분 됨

menu = tuple(menu)
print(menu,type(menu)) # class 'tuple' 출력 해야 함 ()로 구분 됨

menu = set(menu)
print(menu,type(menu))