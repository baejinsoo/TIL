colors = ["red", "blue", "green"]
print(colors[0])
print(colors[2])
print(len(colors))
print(len(colors[2]))

colors[0] = 'Yellow'
print(colors)

# list에 엘리먼트를 1개추가
colors.append('Black')
colors.pop()
colors.remove('blue')
print(colors)
del colors[0]
print(colors)

# list에 엘리먼트를 여러개추가
colors.extend(['Orange', 'Red'])
print(colors)
colors[0] = colors[0].title()
print(colors)

print(colors.index('Red'))

print('Red' in colors)
colors.extend(['Red', 'Red'])
print(colors.index('Red'))
print(colors.count('Red'))
score = 12.1253
print(round(score,2))
