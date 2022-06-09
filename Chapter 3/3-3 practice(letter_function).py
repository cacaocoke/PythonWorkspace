python = "Python is Amazing"
print(python.lower()) # 변수 전부 소문자 출력
print(python.upper()) # 변수 전부 대문자 출력
print(python[0].isupper())
print(len(python)) # 글자수 세 주는 함수
print(python.replace("Python", "Java")) # 특정 문자 바꿀땐 'replace'

index = python.index("n")
print(index) # 0부터 세니까 5를 출력 해야 함
index = python.index("n", index + 1) # 특정 글자 + 1 하면 같은 글자의 다음 위치를 찾아 줌 15를 출력 해야 함
print(index)

print(python.find("n"))

print(python.find("Java")) # find는 내가 찾고자 하는 값이 없을 땐 -1 을 출력 함
#print(python.index("Java")) ## index는 내가 찾고자 하는 값이 없을 땐 오류를 출력 함

print(python.count("n")) # 문자열 안에서 원하는 문자가 몇개 있는지 세어줌 2가 나와야 함