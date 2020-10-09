# 1. %formating : c언어 스타일
# 2. String format 함수 : { }에 대응하는 값을 format()의 인자로 전달
# 3. f-string : python3.6 이상에서만 사용

tem = 36
print('1.온도 값은 : %d %.2f' %(tem, tem))
print('2.온도 값은 : {}'.format(tem))
print(f'3.온도 값은 : {tem}')

print("Art: %5d, Price per Unit: %8.2f" % (453, 59.058))
print("Art: {0:5d}, Price per Unit: {1:8.2f}".format(453, 59.058))

# padding
print("Product: {0:10s}, Price per Unit: {1:10.3f}".format("apple", 59.058))
print("Product: {0:>10s}, Price per Unit: {1:10.3f}".format("apple", 59.058))