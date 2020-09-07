> ### git 연동 : mc pc와 house pc에서 프로젝트 똑같이 사용하게!

##### 아무것도 없는 pc에서 clone 작업

* learn_git_mc  : git에 올린 프로젝트 이름과 상관없음...

![image-20200821094350315](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200821094350315.png)





github에서 url 복사

![B](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200821094541256.png)

git clone https://github.com/ok2qw66/learn_git.git learn_git_house

: learn_git_house 라는 이름으로 내pc에 clone 프로젝트 내려받음(없으면 기존 이름그대로 생성)



#### mc pc에서 저장 -> git 연동 -> house pc에서 받기  

```
#mc pc에서 하는일#

# 새로운 작업 하는중
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git (master)
$ touch 2.txt

# add 하기 (스테이지에 올리기 : 해당 파일 변경 인식)
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git (master)
$ git add 2.txt

# commit 하기 (사진찍기 : local pc에 임시저장)
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git (master)
$ git commit -m 'add 2.txt'

# push 하기 (앨범에 저장 : git 에 올리기)
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git (master)
$ git push origin master
```

```
#house pc에서 하는일#

# pull 하기 (git에서 내려받기)
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)
$ git pull origin master

# 새로운 작업 진행...

# push 하기
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)
$ git push origin master
```

### git push log 확인하기 (가장 최근 부분이 동일해야 문제 없는 상태)

```
git log --pretty=format:"%h %s" --graph
```



***pull ==> 새로운 작업 ==> push***





### commit 합치기

```$ git commit --amend
$ git commit --amend
```



### add 되돌리기

```
$ git reset HEAD 원하는파일이름
```



### 파일에 추가하기 (> : write, >> : append)

```
# board.py 에 # this is comment 추가하기
$ echo '# this is comment' >> board.py
```



### Modified 파일 되돌리기(이전 commit 상태로 되돌아감)

> **이전에 commit 된 상태가 있어야 한다**

```
# board.py 에 마지막 commit 상태로 변경하기(파일 날렸을때/ 수정전으로 되돌릴때)
$ git checkout -- board.py
```



### commit과 push 상태 확인

![image-20200821141423987](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200821141423987.png)

![image-20200821111324501](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200821111324501.png)

commit 과 push 가 동일한 위치에 있다 ==> 모든 commit 이 다 remote에 올라간 상태

commit 과  push 가 다른 위치에 있다 ==> commit 한게 remote에 등록되지 않은게 있다

HEAD -> master : HEAD가 가리키는게 현재 계정



> # branch 생성하기

1.  branch 생성

   ```
   # feature/board 라는 branch 생성
   i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)                            	$ git branch feature/board   
   ```

2. 계정 feature/board 로 변경하기

   ```
   i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)                            	$ git checkout feature/board                                                 	Switched to branch 'feature/board'
   ```

3. 계정 master로 변경하기

   ```
   i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/board)                     	$ git checkout master                                                       	Switched to branch 'master'
   ```

   * 참고 : branch 계정 생성하면서 해당 계정으로 변경
   
     ```
     i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)                            $ git checkout -b feature/auth                                                 Switched to a new branch 'feature/auth'
     ```
   
     

#### 현재 branch 상태 확인하기

```
# * 붙어있는 게 현재 branch 상태
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)                                $ git branch                                                                      feature/board                                                                  * master 
```



#### branch 지우기

```
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)                                  $ git branch -d feature/board                                                     Deleted branch feature/board (was 9e1e09c).
```



```
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)                               $ touch login.py logout.py                                                                                                                               i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)                               $ git add login.py logout.py                                                                                                                             i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)                               $ git status                                                                          On branch feature/auth
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   login.py
        new file:   logout.py


i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)
$ git commit -m 'create login, logout'
[feature/auth 96af16a] create login, logout
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 login.py
 create mode 100644 logout.py
 
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)
$ ls
board.py  logfile  login.py  logout.py  README.md

i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)
$ git checkout master
Switched to branch 'master'



i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)
$ ls
board.py  logfile  README.md

```







```
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)
$ touch signup.py

i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)
$ git add signup.py

i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)
$ git commit -m 'create signup.py'
[feature/auth 0c45092] create signup.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 signup.py

i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (feature/auth)
$ git checkout master
Switched to branch 'master'




i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)
$ touch commerce.py

i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)
$ git add commerce.py                                                                                                                                           i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)                                $ git commit -m 'create commerce.py'                                            [master a4f9f0e] create commerce.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 commerce.py
```





###  merge 하기

```
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_mc (master)
$ git merge feature/auth
Merge made by the 'recursive' strategy.
 login.py  | 0
 logout.py | 0
 signup.py | 0
 3 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 login.py
 create mode 100644 logout.py
 create mode 100644 signup.py
```











# 서로 다른 파일 만들경우 merge



```
$ touch login.py   
```

```
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_together (master)                               $ git checkout -b alla                                                                Switched to a new branch 'alla'
```



```
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_together (alla)                                 $ git push origin alla                                                                Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 303 bytes | 303.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'alla' on GitHub by visiting:
remote:      https://github.com/ok2qw66/learn_git_together/pull/new/alla
remote:
To https://github.com/ok2qw66/learn_git_together.git
 * [new branch]      alla -> alla
```



### github에서 pull request 하기



![](C:\Users\i\AppData\Roaming\Typora\typora-user-images\image-20200821152517247.png)





# 서로 다른 파일 만들경우 merge

```
i@DESKTOP-CS5B0E0 MINGW64 ~/learn_git_together (alla)
$ git add board.py 
```





fetch : 변경된거 받기만 하고 commit은 안함

push?인지 pull인지 모르겠음 : 변경된거 받고 commit 까지 자동으로 해줌











------



### remote 여러 개 설정가능(드라이브 여러개 두는 것과 동일)

##### remote 설정하기 (여러개 가능)

```
git remote add test-server https://~~~
git remote add winner http://~!!~~~
git remote add origin http://....
git remote add backup http:////
```

###### remote 확인

```
git remote -v
test-server ~~~~
winner ~~~~
origin ~~~~
backup ~~~
```

##### remote 삭제하기

```
git remote remove test-server
```

```
git push origin master
git push backup master
....
```

