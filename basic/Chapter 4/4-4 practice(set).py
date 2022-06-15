# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3} # set 선언 시 '{}'로 구분하여 묶어 줌 set에서는 값만 쭉 나열 해주면 됨
print(my_set) # 중복값은 무시하고 출력 '{1,2,3}' 출력 되어야 함

java={"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # set은 {}로 묶거나 set 명령어 이용 시 ([]) 로 묶어 줌

# 교집합 출력 (java, python 모두 사용할 수 있는 개발자)
print(java & python) # '&' 표시로 여러 변수 중 교집합 출력
print(java.intersection(python)) # 교집합 뽑을 때 'intersection' 사용할 수 있음

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # | or 역할을 함
print(java.union(python)) # 또는 'union'을 사용할 수 있음
# 순서에 관계 없이 합집합이면 모두 출력

# 차집합(java 할 수 있지만 python 할 줄 모르는 개발자
print(java-python) # - 이용하여 빼주기
print(java.difference(python)) # 또는 'difference' 사용할 수 있음

# python을 할 줄 아는 사람이 늘어났을때
python.add("김태호") # set은 add 사용할 수 있음
print(python)

# java를 잊었을 때
java.remove("김태호") # 값을 뺄 때는 remove 
print(java)