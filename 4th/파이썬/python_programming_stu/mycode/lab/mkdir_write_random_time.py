import os
from datetime import datetime
from random import random

# log 디렉토리가 없으면 log 디렉토리 생성
if not os.path.isdir('log'):
    os.mkdir('log')

with open("log/count_log.txt", 'a', encoding="utf8") as f:
    # for i in range(100, 111):
    #     data = "%d번째 줄입니다.\n" % i
    #     f.write(data)
    for i in range(1, 11):
        stamp = str(datetime.now())
        value = random() * 100000
        f.write('{}, {}\n'.format(stamp, value))
