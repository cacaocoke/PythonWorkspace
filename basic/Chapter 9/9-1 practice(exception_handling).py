try: # 예외적용시 try 선언 후 하단 내용은 들여쓰기로 종속시킴
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1]))
    #num1 = int(input("첫번째 숫자를 입력하세요 : "))
    #num2 = int(input("두번째 숫자를 입력하세요 : ")) 
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
    #print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError: # except 뒤에 예상 에러코드 넣고 하단에 대체 문구
    print("에러가 발생 했습니다.")
except ZeroDivisionError as err: # as 뒤에 err 선언 후 print로 err 출력 하면 프로그램 에러 문구 그대로 출력
    print(err)
#except : # 특정 에러코드를 선언하지 않으면 모든 에러를 아래 print 지정 구문으로 처리
except Exception as err: # Exception as err 처리 후 print 에서 err 호출 시 발생한 에러메시지 도출
    print(err)