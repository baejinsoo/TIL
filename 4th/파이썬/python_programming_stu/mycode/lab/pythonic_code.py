# colors = ['red', 'blue', 'green', 'yellow']
# print(colors)
# result = '  '.join(colors)
# for s in colors:
#     result += s

# print(result)
# items = result.split()
# print(items)

# result = [i for i in range(4, 31) if i % 2 == 0]
# print(result)

# result = [i if i % 2 == 0 else 10 for i in range(15) ]
# print(result)

# word1 = 'hello'
# word2 = 'how are you'
# result = [i + j for i in word1 for j in word2]
# print(result)

# fin = [i + j for i in word1 for j in word2 if not(i == j)]
# print(fin)
# fin.sort()
# print(fin)

# word = 'this quick brown fox jumps over lazy dog'.split()
# print(word)
# stuff = [[w.upper(), w.lower(), len(w)]for w in word]
# print(stuff)

# mylist = ['a', 'b', 'c', 'd', 'e']
# a = list(enumerate(mylist))
# print(a)

# enumerate(list의 element를 추출할 때 번호를 붙여서 추출)
# list = {i: j for i, j in enumerate('brown university is an academic institute located'.split())}
# print(list)
import idx as idx
#
# word1 = ['a1', 'b2', 'c3']
# word2 = ['e1', 'g2', 'e3']
# list_word = [a+b for a, b in zip(word2, word1)]
# print(list_word)
#
word1 = ['a1', 'b2', 'c3']
word2 = ['e1', 'g2', 'e3']
for i, (a, b) in enumerate(zip(word1, word2)):
    print('{0} : {1} {2}'.format(i,a,b))


lang_list = 'hi my name is MJ'.split()

for i, lang in enumerate(lang_list):
    print('idx: {0}  value: {1}'.format(i, lang))

words = 'brown university is an academic institute located'
a = {i: j for i, j in enumerate(words.split())}
print(a)

word1 = ['a1', 'b2', 'c3']
word2 = ['e1', 'g2', 'e3']
b = {k: i+j for k, (i, j) in enumerate(zip(word1, word2))}
print(b)