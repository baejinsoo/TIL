print("구구단 몇단을 계산할까요?")
x = input()
x = int(x)

while x is not 0:
    if 1 <= x <= 9:
        print("구구단 {}단을 계산합니다".format(x))
        for i in range(1, 10):
            print("{0} X {1} = {2}".format(x, i, x*i))
    else:
        print("1부터 9까지만 입력하세요")
    print("구구단 몇단을 계산할까요?")
    x = input()
    x = int(x)
print("구구단 게임을 종료합니다")
