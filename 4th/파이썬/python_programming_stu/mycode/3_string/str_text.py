greet = 'Hello' * 4 + '\n'
end = 'Goodbye'
print(greet + greet + end)

greet = 'Hello' * 4 + '\t'
end = 'Goodbye'
print(greet + greet + end + end)

print('i like\'apple\'')

greeting = 'hi Hello world haha!'
print(greeting[0])
print(greeting[11])

len(greeting)
print(len(greeting))
print(greeting.upper())
print(greeting.capitalize())
print(greeting.title())
print(greeting.count('l'))
print(greeting.split('ll'))
print(greeting.isdigit())
print(greeting.lstrip())

print(type(greeting.split()), greeting.split())

my_wordlist = greeting.split(' ')
print(my_wordlist)
print(my_wordlist[2])

# list -> str : unpacking
str1, str2, str3, str4= my_wordlist
print(str1)
print(str2)
print(str3)
print(str4)

my_list = ['a', 'b', 'c',]
a1, a2, a3  = my_list
print(a1)
print(a2)
print(a3)
print(a1+a2+a3)

print(greeting.title())
print(greeting.capitalize())