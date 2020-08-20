## 장고 앱 시작

`$ mkdir DJANGO_GIT`

`$ cd DJANGO_GIT`

`$ touch .gitignore`

`$ python -m venv venv`

`$ source venv/Scripts/activate`

`$ python -m pip install --upgrade pip`

`$ pip install django`

`$ django-admin startproject django_git .`

##### gitignore.io -> python, django, venv, pycharm 검색 후 .gitignore복붙

##### .idea/ 추가

`$ git init`

`$ git status`

##### 하위의 전체 파일 add

`$ git add .`

`$ git commit -m 'Init project'`

```
$ git config --global user.name 'name'
$ git config --global user.name 'email'
```

#### github 페이지 repository  추가

```
$ git remote add origin https://github.com/baejinsoo/django_git.git
$ git push origin master
```

#### PyCharm interpreter setting

`$ pip freeze > requirements.txt`

