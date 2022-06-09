'''
def profile(name, age, lang1, lang2, lang3, lang4, lang5): # 사용할 수 있는 언어가 많다고 가정
    print("이름 : {0}\t 나이 : {1}\t".format(name,age), end=" ") # end=" "는  줄바꿈을 하지 않고 문장을 계속 출력 한다는 의미
    print(lang1, lang2, lang3, lang4, lang5)


profile("유재석", 25, "Python", "Java", "C+", "C++", "C#")
profile("김태호", 20, "kotlin", "Swift", "", "", "")
'''

def profile(name, age, *language): # *변수 사용하여 다수의 반복 변수에 대응
    print("이름 : {0}\t 나이 : {1}\t".format(name,age), end=" ") # end=" "는  줄바꿈을 하지 않고 문장을 계속 출력 한다는 의미
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 25, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 20, "Kotlin", "Swift")
# 서로 다른 값이라도 가변인자에 따라 갯수에 맞춰 출력 함

