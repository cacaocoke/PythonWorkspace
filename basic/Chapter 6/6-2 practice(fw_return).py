def open_account():
    print("새로운 계좌가 생성 되었습니다.")

def deposit(balance,money): # 입금
    print("입금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money :
        print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance - money
    else : 
        print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money) :
    commission = 100 #수수료 100 원
    return commission, balance - money - commission

balance = 0 # 잔액 0원 가정하기 위한 과정
balance = deposit(balance, 1000)
print(balance)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 200)

commission, balance=withdraw_night(balance, 500)
print("수수료는 {0}원 이며, 잔액은 {1}원 입니다.".format (commission, balance)) 

