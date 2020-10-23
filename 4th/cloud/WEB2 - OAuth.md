### WEB2 - OAuth

- google, facebook, twitter 등의 웹사이트에서 **access Token**을 획득한 후 이용
- 회원가입을 따로 할 필요가 없음

![image-20201023211509519](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201023211509519.png)

**Resource Server  - Resource owner  - Clinet **

1. Clinet에서 Resourece Server로 사전에 승인을 받아야함(Google Cloud Platform)

   - Client ID

   - Client Secret

   - Authorized redirect URL

2.  Resource Server는 인증이 되면 access Token을 발급해 client에게 보냄

3. Client는 access Token을 저장해 resource owner에 대해 주어진 정보들 알게됨



##### API 호출

(Application Programming Interface)



##### refresh token

유효기간이 지나서 토큰 재발급

rfc 6749

