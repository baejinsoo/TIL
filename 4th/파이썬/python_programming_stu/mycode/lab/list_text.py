import random

for i in range(10):
    hi = random.randint(1, 1000)
    print(hi)

for j in range(10, 1, -1):
    print(j)

idx = 0
while idx < 10:
    print('idx : {}'.format(idx))
    idx += 1
else:
    print('EOP')

print('------break-------')
for val in range(10):
    if val == 5:
        break
    print(val)
else:
    print('EOP')
    
print('------continue-------')
for val in range(10):
    if val == 5:
        continue
    print(val)
else:
    print('EOP')

