# React를 배우기 전에 알아야 할 자바스크립트 기초

- [ES6 classes](https://dev.to/nsebhastian/javascript-basics-before-you-learn-react-38en#es6-classes)
- [The new variable declaration let/const](https://dev.to/nsebhastian/javascript-basics-before-you-learn-react-38en#declaring-variables-with-es6-let-and-const)
- [Arrow functions](https://dev.to/nsebhastian/javascript-basics-before-you-learn-react-38en#the-arrow-function)
- [Destructuring assignment](https://dev.to/nsebhastian/javascript-basics-before-you-learn-react-38en#destructuring-assignment-for-arrays-and-objects)
- [Map and filter](https://dev.to/nsebhastian/javascript-basics-before-you-learn-react-38en#map-and-filter)
- [ES6 module system](https://dev.to/nsebhastian/javascript-basics-before-you-learn-react-38en#es6-module-system)





# Create React App 탐험하기

대부분의 사람이 `create-react-app`을 커맨드 라인에 입력하면서 React 학습을 시작했을 겁니다. 이 패키지엔 React를 실행하기 위한 모든 것이 세팅되어 있습니다. 패키지 설치가 끝난 후, `src/app.js`을 열어보면 아래와 같이 React 클래스(class)를 볼 수 있습니다.

```js
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
```



# ES6 클래스

## React에서 어떻게 쓰이나요?

ES6의 클래스와 상속에 관한 개념을 학습했기 때문에, 이제 `src/app.js`에 쓰인 React 클래스가 뭔지 알 수 있습니다. React 클래스는 React 컴포넌트(component)입니다. 이 컴포넌트는 단순히 React 패키지로부터 import 한 React 컴포넌트 클래스를 상속받은 평범한 ES6 클래스일 뿐입니다.

```js
import React, { Component } from 'react';

class App extends Component {
  // class content
  render(){
    return (
      <h1>Hello React!</h1>
    )
  }
}
```

이렇게 React 컴포넌트 클래스를 상속받았기 때문에 우리는`render()` 메서드, JSX, `this.state`등의 다양한 메서드를 사용할 수 있게 되었습니다. 이 메서드들은 모두 `Component` 클래스에 정의되어 있기 때문입니다. 만약 상태(state)나 라이프사이클과 관련된 메서드(lifecycle method)가 필요하지 않다면 Component 클래스를 상속받는 대신 함수를 사용할 수도 있습니다.

# let과 const로 변수 선언하기

이 두 키워드는 변수 선언 시 쓰인다는 공통점이 있습니다. 차이점은 `const`로 선언한 변수는 선언 이후에 값을 바꿀 수 없고, `let`으로 선언한 변수는 바꿀 수 있다는 점입니다. 두 키워드로 선언한 변수는 지역변수가 됩니다. 따라서 함수 스코프 안에서 `let`으로 선언한 변수는 함수 밖에서 호출할 수 없습니다.

```js
import React, { Component } from 'react';

class App extends Component {
  // class content
  render(){
    const greeting = 'Welcome to React';
    return (
      <h1>{greeting}</h1>
    )
  }
}
```

greeting 변수는 어플리케이션의 전체 생명주기(lifecycle)동안 변하지 않기 때문에 `const`키워드를 사용해 변수를 선언했습니다.

# 화살표 함수

화살표 함수(arrow function)는 ES6에서 도입된 새로운 피처입니다. 코드를 간결하고 읽기 쉽게 해주기 때문에 모던 언어에서 많이 쓰입니다. 화살표 함수를 쓰면 함수를 좀 더 짧은 문법(syntax)으로 작성할 수 있습니다.

```js
// regular function
const testFunction = function() {
  // content..
}

// arrow function
const testFunction = () => {
  // content..
}
```

1. function 키워드 지우기
2. `()`다음에 뚱뚱한 화살표(fat arrow, =>) 기호 넣기

화살표 함수에서도 기존 함수 선언 방식에서와 마찬가지로 괄호는 매개변수를 감싸는 용도로 사용됩니다. 만약 매개변수가 하나라면 괄호를 생략할 수 있습니다. 아래 코드에서 두 번째 함수 singleParam은 매개변수가 firstName 하나이기 때문에 괄호를 생략하였습니다.

```js
const testFunction = (firstName, lastName) => {
  return firstName+' '+lastName;
}

const singleParam = firstName => {
  return firstName;
}
```

## 암묵적 반환(Implicit return)

화살표 함수의 본문(body)이 한 줄로만 구성되었다면, 반환 값 앞의 `return` 키워드를 생략할 수 있습니다. 몸체를 감싸는 중괄호 `{}`역시 생략 가능합니다.

```js
const testFunction = () => 'hello there.';
testFunction(); 


const HelloWorld = (props) => {
  return <h1>{props.hello}</h1>;
}
```

```js
class HelloWorld extends Component {
  render() {
    return (
      <h1>{props.hello}</h1>;
    );
  }
}
```

화살표 함수는 코드를 좀 더 간결하게 만들어줍니다. 하지만 간결해진 대신 컴포넌트에서 라이프사이클을 활용하지 못한다는 단점이 있습니다. 이런 종류의 컴포넌트는 **stateless** **함수형 컴포넌트(functional component)**라 불립니다. 리액트와 관련된 튜토리얼에서 이 용어를 많이 만나보시게 될 겁니다.



# 구조 분해 할당

ES6에서 새로 도입된 구조 분해 할당(destructuring assignment, 비구조화 할당)을 사용하면 객체나 배열 일부를 쉽게 변수로 해체할 수 있습니다. 예시를 살펴보겠습니다.

```js
const developer = {
  firstName: 'Nathan',
  lastName: 'Sebhastian',
  developer: true,
  age: 25,
}

//destructure developer object
const { firstName, lastName } = developer;
console.log(firstName); // returns 'Nathan'
console.log(lastName); // returns 'Sebhastian'
console.log(developer); // returns the object
```

`developer` 객체의 `firstName` 과`lastName`프로퍼티를 해체하여 새로운 변수인 `firstName` 과`lastName` 에 할당하였습니다. 그런데 만약 `firstName` 프로퍼티를 새로운 변수인 `name`에 할당하고 싶다면 어떻게 해야할까요? 아래와 같이 하면 됩니다.

```js
const { firstName:name } = developer;
console.log(name); // returns 'Nathan'
```

구조 분해 할당은 배열에도 적용할 수 있습니다. 객체에선 key를 사용했지만, 배열에선 배열 순서대로 대응한다는 점만 다릅니다.

```js
const numbers = [1,2,3,4,5];
const [one, two] = numbers; // one = 1, two = 2

// , 을 사용하면 중간 인덱스를 건너 뛰고 분해 할당하는게 가능
const [one, two, , four] = numbers; // one = 1, two = 2, four = 4
```



## React에서 어떻게 쓰이나요?

React에서는 메서드 안에서 `state`를 해체할당 하는데 자주 쓰입니다.

```js
reactFunction = () => {
  const { name, email } = this.state;
};
```

stateless 함수형 컴포넌트에서도 자주 쓰입니다. 화살표 함수에서 썼던 예제 코드를 다시 보도록 하죠.

```js
const HelloWorld = (props) => {
  return <h1>{props.hello}</h1>;
}

// 매개변수를 바로 분해해서 대입=================>

const HelloWorld = ({ hello }) => {
  return <h1>{hello}</h1>;
}
```

# 맵과 필터

이 튜토리얼은 ES6에서 새롭게 도입된 피처에 대해 다루고 있긴 하지만, 자바스크립트 ES5의 배열 메서드인 `map` 과`filter`메서드는 꼭 언급하고 넘어가야 할 것 같습니다. 두 메서드는 React 애플리케이션을 만들 때 가장 많이 쓰이는 ES5 피처이기 때문입니다. 특히 데이터를 가공할 때 유용하게 쓰입니다.

API를 통해 받아온 데이터가 JSON 배열이라 가정해 봅시다.

```js
const users = [
  { name: 'Nathan', age: 25 },
  { name: 'Jack', age: 30 },
  { name: 'Joe', age: 28 },
];
```

배열의 각 요소를 map을 이용해 뽑아내 render()에서 사용할 수 있습니다.

```js
import React, { Component } from 'react';

class App extends Component {
  // class content
  render(){
    const users = [
      { name: 'Nathan', age: 25 },
      { name: 'Jack', age: 30 },
      { name: 'Joe', age: 28 },
    ];

    return (
      <ul>
        {users
          .map(user => <li>{user.name}</li>)
        }
      </ul>
    )
  }
}
```

data를 필터링(filter, 가공하여 필요한 것만 남겨서)해서 render()에서 쓸 수도 있습니다.

```js
<ul>
  {users
    .filter(user => user.age > 26)
    .map(user => <li>{user.name}</li>)
  }
</ul>
```

# ES6 모듈 시스템

ES6 모듈 시스템(module system)은 자바스크립트가 파일(모듈)을 호출(import)하고, 선언하여 내보낼 수 있게(export) 해 줍니다. `src/app.js` 코드로 이를 살펴보도록 하겠습니다.

```js
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
```

코드 맨 윗줄을 보면 import 키워드가 있는걸 발견할 수 있습니다. 맨 아랫줄엔 `export default` 문이 있는걸 볼 수 있습니다.

이 코드를 이해하려면 모듈 문법에 대하여 먼저 알아야 합니다.

모듈은 `export` 키워드를 통해 하나 혹은 다수의 값(객체나 함수, 또는 변수)을 선언하여 외부로 내보낼 수 있게 해주는 자바스크립트 파일입니다. 이를 확인하기 위해 `src` 폴더에 새로운 파일, `util.js` 을 만들어보도록 합시다.

```js
// util.js
export function times(x) {
  return x * x;
}
export function plusTwo(number) {
  return number + 2;
}
```

이제 `src/App.js`에서 export 한 함수들을 불러올 수 있게 되었습니다.

```js
import { times, plusTwo } from './util.js';
console.log(times(2));
console.log(plusTwo(3));
```

모듈 하나에 여러 개의 named exports가 있을 수 있지만, default export는 딱 하나만 허용됩니다. default export는 {}를 사용하지 않으면서, 상응하는 이름 없이도 import 할 수 있습니다.

```js
// in util.js
export default function times(x) {
  return x * x;
}
// in app.js
import k from './util.js';
console.log(k(4)); // returns 16
```

반면, named exports는 {}을 이용해 import 해야 하고, 정확한 이름도 명시해 주어야 합니다. as 키워드를 사용해 별칭을 사용하면 모듈 이름이 겹치는 경우를 할 수 있습니다.

```js
// in util.js
export function times(x) {
  return x * x;
}
export function plusTwo(number) {
  return number + 2;
}
// in app.js
import { times as multiplication, plusTwo as plus2 } from './util.js';
```

## React에서 어떻게 쓰이나요?

```js
//index.js file

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
```



`./App` 디렉토리에서 import 한 App은 확장자가 없다는 점에 주목하시기 바랍니다. 자바스크립트 파일을 import 할 땐, 확장자를 생략해도 됩니다. 하지만 `.css`같이 다른 종류의 파일은 확장자를 반드시 써 줘야 합니다. DOM 렌더링에 사용되는 노드 모듈인 `react-dom`도 import 해 주었습니다.

맨 아랫줄의 서비스 워커(service worker)는 React 애플리케이션이 오프라인에서도 작동할 수 있게 해줍니다. 이 피처는 기본적으로 꺼져있기 때문에, 본 튜토리얼에선 이에 대해서 더 자세히 알아보진 않겠습니다. React 유저 인터페이스(UI)를 만드는데 자신감이 생기면, 그때 PWA(Progressive Web App)을 학습하면서 서비스 워커를 알아봐도 늦지 않습니다.



- [Navigating the React.JS Ecosystem](https://www.toptal.com/react/navigating-the-react-ecosystem)(React.JS 생태계 탐험하기)
- [Efficient React Components: A Guide to Optimizing React Performance](https://www.toptal.com/react/optimizing-react-performance)(효율적인 React 컴포넌트: React 퍼포먼스 최적화를 위한 가이드)
- 모던 JavaScript 튜토리얼 페이지 https://ko.javascript.info/

