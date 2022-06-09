# 출석번호가 1,2,3 인데 앞에 100을 붙이기로 함 ex) 101,102,103
student =[1,2,3,4,5]
print(student)
student = [i+100 for i in student] # student 변수 내 값(i)에 100씩을 더한다는 의미
print(student) 

# 학생 이름을 글자수 길이로 변환
student = ["Iron man", "Thor", "Groot"]
student = [len(i) for i in student] # len을 사용하여 글자수 갯수 파악
print(student)

# 학생 이름을 대문자로 변환
student = ["Iron man", "Thor", "Groot"]
student = [i.upper() for i in student]
print(student)