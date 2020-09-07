# python project 시작하기

> ### bash.exe 실행

```
# 프로젝트 생성
i@DESKTOP-CS5B0E0 MINGW64 ~
$ mkdir DJANGO_GIT

# 프로젝트로 이동
i@DESKTOP-CS5B0E0 MINGW64 ~
$ cd DJANGO_GIT/

# .gitignore 파일 생성(git에서 올리지 않을 무시할 파일 목록 저장함)
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ touch .gitignore

# 숨긴파일 확인
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ ls -a
./  ../  .gitignore

# venv 생성(가상환경 만들기 : DJANGO_GIT 만을 위한 파이썬 세팅할 공간)
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ python -m venv venv

# 가상화 환경 시작하기
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ source venv/Scripts/activate   
```



> ### 가상화 환경으로 변경

**(venv) 라는 표시가 있으면 가상화 환경 사용중**

```
# 가상환경 파이썬에 설치된 모듈 확인하기
(venv)
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ pip list
Package    Version
---------- -------
pip        20.1.1
setuptools 47.1.0

# pip 버전 업그레이드 (꼭 안해도 됨)
(venv)
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ python -m pip install --upgrade pip

# django 설치
(venv)
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ pip install django

# django_git 현재폴더에 프로젝트 시작 (뒤에 . 붙임 => 현재 디렉토리에 생성)
(venv)
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ django-admin startproject django_git .
```

* https://www.toptal.com/developers/gitignore/api/python,django,venv,pycharm 에서 가져온 파일을
  .gitignore에 넣기



> ### Pycharm에서 Terminal에서 실행

`$ git init` : git 연동 시작

`$ git add .` : commit 할 내용 임시저장

`git commit -m 'Init Project'` : commit하기 => git에 올리기

```
# git 연동시작
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT
$ git init
Initialized empty Git repository in C:/Users/i/DJANGO_GIT/.git/
```

```
# 모든 정보 git에 add 하기(commit 전에 임시저장)
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT (master)
$ git add .

# 현재 상태 확인하기
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT (master)
$ git status

# Init Project 메시지 주면서 commit하기
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT (master)
$ git commit -m 'Init Project'
```



> ### readme 파일 만들기 : 설명서

```
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT (master)
$ touch README.md
```





# remote 등록하기

> ### github 페이지에서 repository 새로 만들어서 연동하기

```
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT (master)
$ git remote add origin https://github.com/ok2qw66/django_git.git

i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT (master)
$ git push origin master
```

![image-20200820174428736](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200820174428736.png)

- 밑줄 친 부분 실행하기



# 다른 프로젝트 받을 때 venv 설정하기

1. ctl+alt+s 누르고 설정창으로 이동
2. interpreter에서 venv로 설정하기

![image-20200820174936744](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200820174936744.png)

	3. 설정창 제대로 잡혀 있는지 확인하기
 	4. ![image-20200820175029355](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200820175029355.png)



# 사용하는 모듈 리스트 requirements.txt에 생성하기

```
# 필요한 모듈 install 하기
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT (master)
$ pip install django_extensions
```

```
# install list requirements.txt에 넣기
i@DESKTOP-CS5B0E0 MINGW64 ~/DJANGO_GIT (master)
$ pip freeze > requirements.txt
```



### add , commit, push

![image-20200820181937556](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200820181937556.png)

- add :  stage에 올린 상태
  - 무대에 올린 상태 (아무의미 없음)
- HEAD -> master : commit 완료 한 상태(github에는 등록안됨)
  - 사진찍은 상태 (저장됨)
- orgin/master : push 까지 완료한 상태(github에 등록됨)
  - 앨범에 넣은 상태(github에 올림)