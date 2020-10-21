## Node.js

- Chorm V8 자바스크립트 엔진으로 빌드된 자바스크립트 런타임 환경으로  주로 서버 사이드 애플리케이션 개발에 사용되는 소프트웨어 플랫폼
- node.js는 브라우저 외부 환경에서 자바스크립트 애플리케이션 개발에 사용되며 이에 필요한 모듈, 파일시스템, http등 built-in API를 제공
- 자바스크립트를 사용해 개발, front-end와 back-end에서 자바스크립트를 사용할 수 있다는 동형성의 장점
- 모든 api는 비동기 방식으로 동작하여 **Non-blocking I/O**가 가능하고 단일 스레드 이벤트 루프 모델을 사용하여 보다 가벼운 환경에서 높은 Request 처리 성능을 가짐
- 데이터를 실시간 처리하여 빈번한 I/O 가 발생하는 single page application에 적합, 하지만 cpu 사용률이 높은 애플리케이션에는 권장하지 않음
- *socket.io* 라는 실시간 통신을 실현하는 라이브러리 사용가능 - 대량의 데이터 처리, 실시간 통신 구현



####  url 형식

예시) http://opentutorials.org:3000/main?id=HTML&page=12

- **http** : protocol 통신규칙 - 사용자가 서버에 접속할때 어떤방식으로 통신할까

- **opentutorials.org**:  도메인 네임,  host(인터넷에 접속되어있는 각각의 컴퓨터)

- **3000**: port 포트번호 => 3000번 포트에 연결되 있는 서버와 통신하고 있음

- **main**: path 그 컴퓨터 안에있는 어떤 디렉터리의 어떤 파일인지

- **id=HTML&page**=12: query string 



##### query string

```js
// localhost:3000/?id=CSS 실행결과
var url = require('url')

var queryData = url.parse(_url, true).query;
console.log(queryData.id); // css
response.end(queryData.id); // css가 화면에 출력
```

