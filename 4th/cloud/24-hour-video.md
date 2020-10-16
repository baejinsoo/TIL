### 1. Users 생성

### 2. CLI 환경에서 작업할 수 있도록 액세스 키 ID, 비밀 액세스 키, 리전 등의 정보를 설정



**Access key ID**

AKIATYDURGJKICG5YYMN

**Secret access key**

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



![image-20201016143754405](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201016143754405.png)

### 3. 사용자 권한 설정

![image-20201016143959322](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201016143959322.png)

인라인 정책 추가:  일반적으로 일회성으로 적용

관리형 정책: 정책 업데이트하면 연결된 모든 사용자와 그룹에 적용



![image-20201016144648168](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201016144648168.png)



### 4.  S3 버킷 생성

- 원본 동영상을 업로드 후 저장할 버킷
- Elastic Transcoder에 의해 트랜스코딩된 동영상을 저장할 버킷

![image-20201016150020341](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201016150020341.png)



### 5. IAM 역할 생성

Lambda 함수가 S3 및 Elastic Transcoder와 상호작용할 수 있는 역할

![image-20201016150135107](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201016150135107.png)

![](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201016150341033.png)



### 5. Lambda 생성

![image-20201016150632334](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201016150632334.png)



### 7. Elastic Transcoder 구성

![image-20201016151221482](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201016151221482.png)

### 8. npm 설정

cmd 창

```
cd /
mkdir serverless
cd serverless
mkdir transcode-video
cd transcode-video
npm init -y
npm install aws-sdk
```



### 9. ZIP 설치

http://gnuwin32.sourceforge.net/packages/zip.htm

- Complete package except sources **Setup** 다운로드
- 환경변수에 압춘 푼 곳에 경로 추가 **C:\Program Files (x86)\GnuWin32\bin**



