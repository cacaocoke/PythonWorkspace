# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

'''
for waiting_no in range(1, 6) : # range 사용 시 0 부터 지정 숫자 -1 한 범위까지, 또는 앞 뒤로 숫자 범위 지정 이때에도 마지막 자리는 -1 됨
    print("대기번호 : {0}" .format(waiting_no))
'''

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks :
    print("{0}, 커피가 준비되었습니다.".format(customer))