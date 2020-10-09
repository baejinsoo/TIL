# 파일을 읽어서 Yesterday, yesterday, YESTERDAY 몇번 나오는지 카운트

# r(read), w(write), a(append), rb, wb(binary file)
file = open('yesterday.txt', 'r')
yesterday_lyric = ''
while 1:
    line = file.readline()
    if not line:
        break
    # yesterday_lyric = yesterday_lyric + line.strip() + '\n'
    yesterday_lyric += line
# print(yesterday_lyric)
yesterday_lyric = yesterday_lyric.lower()
print('yesterday는 총', yesterday_lyric.count('yesterday'), '번 나옵니다')
print(len(yesterday_lyric))
file.close()

