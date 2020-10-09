books = list()

books.append({'제목': '개발자의코드', '출판연도': '2013.02.28', '출판사': 'A출판', '쪽수': 213, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도': '2013.03.28', '출판사': 'B출판', '쪽수': 580, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2013.02.12', '출판사': 'A출판', '쪽수': 290, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2013.02.28', '출판사': 'B출판', '쪽수': 520, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.02.28', '출판사': 'C출판', '쪽수': 240, '추천유무': True})

title_list = list()
pub_comp = set()
many_title = list()
recommend_list = list()
all_pages = int()

for book in books:
    title_list.append(book['제목'])
    pub_comp.add(book['출판사'])
    if book['쪽수'] > 250:
        many_title.append(book['제목'])
    if book['추천유무']:
        recommend_list.append(book['제목'])
    all_pages += book['쪽수']

print(title_list)
print(pub_comp)
print(many_title)
print(recommend_list)
print(all_pages)

print('-----------------------------')


# List Comprehension 스타일
title_list = [book['제목'] for book in books]
pub_comp = set(book['출판사'] for book in books)
many_title = [book['제목'] for book in books if book['쪽수'] < 250]
recommend_list = [book['제목'] for book in books if book['추천유무']]
all_pages = sum(book['쪽수'] for book in books)

print(title_list)
print(pub_comp)
print(many_title)
print(recommend_list)
print(all_pages)