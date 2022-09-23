'''

dict = {'apple' : '사과',
        'banana' : '바나나',
        'school' : '학교',
        'book' : '책',
        'desk' : '책상'
        }
word = input()

print(dict[word])





"""
투입 금액 : myMoney
제품 금액 ; xxCost
제품 개수 : xxFlag
"""

myMoney = 0

coffeeCost = 1000
orangeCost = 1500
cokeCost = 2000

coffeeFlag = 0
orangeFlag = 0
cokeFlag = 0

runStat = True
end = 1000

myMoney = int(input('안녕하세요, 자판기를 이용하시려면 돈을 투입하세요 : '))
print('%d원을 투입하셨습니다.' %myMoney)
print('\n----메뉴-----',
      '\n1. 커피 :', coffeeCost,
      '\n2. 콜라 :', cokeCost,
      '\n3. 오렌지 쥬스 :', orangeCost,
      '\n0. 종료')

while myMoney >= end or runStat == True :
    selMenu = int(input('\n메뉴 번호를 입력하세요 : '))

    if selMenu == 1 :
        if myMoney >= coffeeCost :
            myMoney = myMoney - coffeeCost
            coffeeFlag += 1
            print("커피를 구매하였습니다. 잔액은 %d원 입니다." %myMoney)
        else :
            print("잔액이 부족합니다.")
            runStat = False
    
    elif selMenu == 2 :
        if myMoney >= cokeCost :
            myMoney = myMoney - cokeCost
            cokeFlag += 1
            print("콜라를 구매하였습니다. 잔액은 %d원 입니다." %myMoney)
        else :
            print("잔액이 부족합니다.")
            runStat = False

    elif selMenu == 3 :
        if myMoney >= orangeCost :
            myMoney = myMoney - orangeCost
            orangeFlag += 1
            print("오렌지 쥬스를 구매하였습니다. 잔액은 %d원 입니다." %myMoney)
        else :
            print("잔액이 부족합니다.")
            runStat = False

    elif selMenu == 0 :
        runStat = False

    else :
        print("다시 입력해 주세요.")

print("구매하신 물품은 ")


print("이용해 주셔서 감사합니다.")

'''

def factorial(n) :
    if n==1 :
        return 1
    elif n>1 :
        return n*factorial(n-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))