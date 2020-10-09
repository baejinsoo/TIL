# id_num = [1, 2, 3, 4]
# name = ['Hong', 'Lee', 'Jang', 'King']
# email = ['hong@mail.com', 'lee@mail.com', 'jang@mail.com', 'king@mail.com']
# hp_num = ['010-1234', '010-4565', '010-5679', '010-7856']
#
# dic1 = dict(zip(id_num, name))
# dic2 = dict(zip(email, hp_num))
#
# print(dic1)
# print(dic2)
#
# list_result = list(zip(id_num, name, email, hp_num))
# print(list_result)

users = [{'id':1,'name':'홍길동','email':'hong@mail.com','hp_num':'010-2343-1234'},
         {'id': 2, 'name': '이순신', 'email': 'lee@mail.com', 'hp_num': '010-3333-5555'}]

users.append({'id': 3, 'name': '장영실', 'email': 'jang@mail.com3', 'hp_num': '010-7777-1233'})
users.append({'id': 4, 'name': '세종대왕', 'email': 'sejong@mail.com3', 'hp_num': '010-4567-1233'})
print(users)

for user in users:
    print("---------------")
    for key, value in user.items() :
        print(f'{key} = {value}')
print("---------------")