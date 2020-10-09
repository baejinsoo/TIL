# 평균을 계산하는 함수 정의


def connect(server = 'abc.com', port = '5050'):
    str = 'http://' + server + ':' + port
    return str


def average(numbers):
    total = 0
    for num in numbers:
        total += num

    avg = total / len(numbers)
    return avg


def main():
    prices = [29, 21, 55, 10]
    result = average(prices)

    print(result)
    print(connect('test.com', '8080'))
    print(connect(port='8150', server='good.com'))
    print(connect())
    print(connect(port='453'))
    print(connect('afjl.com'))


main()