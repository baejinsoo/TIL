# 값의 변경이 불가능한 리스트 - tuple
# 프로그램을 작동하는 동안 변경되지 않는 데이터의 저장
my_tuple = (10, 20, 30, 40, 20)
print(my_tuple)


# 값의 중복이 불가능한 리스트 - set
a = {10, 20, 30, 40, 20}
print(a)
s = set([1, 2, 3, 5, 1])
print(s)
s.add(4)
print(s)
s.add(3)
print(s)
s.remove(3)
print(s)
s.update([4, 8, 9, 10])
print(s)
s.discard(5)
print(s)
s.clear()
print(s)