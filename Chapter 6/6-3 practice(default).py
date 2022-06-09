'''
def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}"\
        .format(name, age, main_lang)) # '\' 입력 후 엔터 하면 줄바꿈 후 내용은 이어서


profile("유재석", 25, "파이썬")
profile("김태호", 20, "자바")
'''

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17, main_lang="파이썬"): # default는 '=지정값'으로 선언
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}"\
        .format(name, age, main_lang)) # '\' 입력 후 엔터 하면 줄바꿈 후 내용은 이어서
        # \t는 문자열 사이에 탭 간격을 줄 때 사용하는 '이스케이프 코드'

profile("유재석")
profile("김태호")