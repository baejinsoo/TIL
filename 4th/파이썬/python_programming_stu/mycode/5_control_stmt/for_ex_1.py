for i in range(0, 11):
    print(i)

for i in range(0, 20, 3):
    print(i)

# 문자열 타입의 리스트
favorite_hobby = ['reading', 'fishing', 'shopping']
for hobby in favorite_hobby:
    print('{} is my favorite hobby'.format(hobby))

# 사전 타입
# key와 vaule를 출력할 때 keys() 함수 사용
wish_travel_city = {'bangkok': 'Thai',
                    'LA': 'USA',
                    'Manila': 'Philiphines'}

print(type(wish_travel_city))
print(wish_travel_city.items())
print(wish_travel_city['LA'])

# key와 vaule를 출력할 때 items() 함수 사용
for city, country in wish_travel_city.items():
    print('{} {}'.format(city, country))
    print('{} in {}'.format(city, wish_travel_city[city]))