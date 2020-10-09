cities = ["서울","부산","인천", \
        "대구","대전","광주","울산","수원"]
print(cities[0:6])
print(cities[0:6:2])
print(cities[:])
print(cities[-50:50])
print(cities[::2], " AND ", cities[::-1])

hi = 'falkdjlkdsajflajsdfl'
print(hi)
aa = list(hi)
a1 = aa[::4]
b1, b2, b3, b4, b5 = a1
print(b1+b2+b3+b4+b5)
