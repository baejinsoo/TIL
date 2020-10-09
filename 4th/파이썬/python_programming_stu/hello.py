import sys


def say_hello(msg):
    return 'Hello ' + msg


def main():
    print(sys.argv[0])
    msg = sys.argv[1]
    print(msg)
    if msg is None:
        print('Enter msg')
    else:
        print(say_hello(msg))


if __name__ == '__main__':
    print('직접 실행')
    main()
else:
    print('import 되어 실행')
