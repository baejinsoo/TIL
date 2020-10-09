my_dic = {"america": 1,
          'korea': 2,
          'china': 23}
print(my_dic)

for key, value in my_dic.items():
    print("key : {}  Value : {}".format(key, value))

print(my_dic.items())

print(my_dic.keys())
print(my_dic.values())

my_dic['japan'] = 7
print(my_dic)
my_dic['japan'] = 8
print(my_dic)
print("korea" in my_dic.keys())
print(23 in my_dic.values())

result = my_dic.get('korea')
print(result)

my_dic.setdefault('LA', 20)
print(my_dic)
my_dic.setdefault('LA', 50)
print(my_dic.key('LA'))

# zip() 여러 시퀀스 병렬로 순회하기
# days = ['mon', 'tus', 'wed']
# fruits = ['ban', 'app', 'oran']
# drinks = ['coffee', 'milk', 'water']
#
# a = dict(zip(days, drinks))
# print(a)

# for days, fruits, drinks in zip(days, fruits, drinks):
#     print("{}에는 {}를 먹고 {}를 마셔요".format(days, fruits, drinks))


