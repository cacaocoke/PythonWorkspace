# print("Python", "Java") # ',' 사용 시 한칸 띄어서 출력 됨
# print("Python" + "Java") # '+' 사용 시 띄어쓰기 없이 붙여서 출력 됨
# print("Python", "Java", sep=",") # sep 사용 시 원하는 구분 기호를 넣을 수 있음
# print("Python", "Java", "JavaScript", sep=" vs ") # sep안에 띄어쓰기는 구분 됨


from os import sep


print("Python", "Java", sep=",", end="?") # '?'의 의미는 문장의 마지막을 '?'로 끝나게 해달라는 말
print("무엇이 더 재밌을까요?")

'''
import sys
print("Python", "Java", file=sys.stdout) # 'stdout'은 표준 출력으로 찍힘
print("Python", "Java", file=sys.stderr) # 'stderr'은 표준 에러로 처리
'''

'''
# 시험성적
scores = {"수학": 0, "영어": 50, "코딩": 100} # dictionary
for subject, score in scores.items(): # items 하게되면 키, 밸류가 페어로 나옴 예시에선 'subject'가 '키', 'score'가 'value'
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust는 왼쪽 정렬, rjust는 오른쪽 정렬, '()' 안에 숫자 만큼 공간 확보
'''
'''
# 은행 대기 순번표
# 001, 002, 003 ...

for num in range(1, 21):
    print("대기번호 : " +str(num).zfill(3)) # zfill은 0을 채움 () 안에 숫자는 자릿수, 공백은 0으로 채움
'''

# answer = input("아무값이나 입력 하세요 : ") #입력값이 예문상 answer에 들어감
# print("입력하신 값은 " + answer+ "입니다.")
answer = 10 # int 로 출력 됨
print(type(answer))

# 사용자 입력일 경우 항상 문자열로 출력 됨