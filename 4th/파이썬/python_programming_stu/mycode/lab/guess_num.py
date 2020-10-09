import random

guess_number = random.randint(1, 100)
check = 1

while check < 100:
    print("1부터 100사이의 숫자를 입력하세요 :")
    input_number = input()
    if guess_number == int(input_number):
        print('맞췄습니다. {}번만에 맞췄네요'.format(check))
        print('입력한숫자= ', input_number, ' 정답은= ', guess_number)
        break
    elif int(input_number) > guess_number:
        print('숫자가 너무 큽니다')
    elif int(input_number) < guess_number:
        print('숫자가 너무 작습니다')
    else:
        print('숫자를 잘못 입력했습니다')
    check += 1
