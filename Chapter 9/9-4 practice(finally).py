class BigNumberError(Exception):
    #pass
    def __init__(self,msg): # 잘못 입려된 값을 확인 
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("첫번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 발생 할 에러 구분 
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
    print(err)
finally: # 항상 try 구문 맨 마지막에 위치 # 오류 여부에 관계없이 무조건 출력
    print("계산기를 이용해 주셔서 감사합니다.")
