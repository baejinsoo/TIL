print('태어난 년도를 입력하세요 :')
year = input()
age = 2020 - int(year) + 1

if 17 <= age < 20: print('고등학생 입니다')
elif 20 <= age < 27: print('대학생 입니다')
else: print('학생이 아닙니다')