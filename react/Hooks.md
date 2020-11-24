## Hooks

#### 1.useState

useState 함수의 파라미터에는 상태의 기본값을 넣음.

##### 1-1 useState 여러 번 사용

*Info.js

```js
import React, { useState } from 'react';

const Info = () => {
    const [name, setName] = useState('');
    const [nickname, setNickname] = useState('');

    const onChangeName = e => {
        setName(e.target.value);
    };

    const onChangeNickname = e => {
        setNickname(e.target.value);
    };

    return (
        <div>
            <div>
                <input value={name} onChange={onChangeName} />
                <input value={nickname} onChange={onChangeNickname} />
            </div>
        <div>
            <b> 이름:</b> {name}
        </div>
        <div>
            <b> 닉네임:</b> {nickname}
        </div>
        </div>
    )
}

export default Info;
```

*App.js

```js
import React from 'react';
import Info from './Info';

const App = () => {
  return <Info />
}

export default App;

```

![image-20201124170138221](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201124170138221.png)

#### 2.useEffect

리액트 컴포넌트가 랜더링될 때마다 특정 작업을 수행하도록 설정할 수 있는 Hook

*Info.js 추가

```js
const Info = () => {
    const [name, setName] = useState('');
    const [nickname, setNickname] = useState('');
    useEffect(() => {
        console.log('렌더링이 완료되었습니다.');
        console.log({
            name,
            nickname
        });
    });

    const onChangeName = e => {
        setName(e.target.value);
    };
```

![image-20201124170721665](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201124170721665.png)

- 렌더링 될때마다 실행되는 모습 확인



#### 3.useReducer

useState 보다 더 다양한 컴포넌트 상황에 따라 다양한 상태를 다른 값으로 업데이트 하고 싶을 때 사용하는  Hook

reducer: 현재 상태, 그리고 업데이트를 위해 필요한 정보를 담은 액션 값을 전달받아 새로운 상태를 반환하는 함수. 리듀서 함수에서 새로운 상태를 만들 때는 반드시 불변성을 지켜 줘야함.

*Counter.js

```js
import React, { useReducer } from 'react';

function reducer(state, action) {
    //action.type 에 따라 다른 작업 수행
    switch (action.type) {
        case 'INCREMENT':
            return {value: state.value + 1};
        case 'DECREMENT':
            return {value: state.value - 1};
        default:
            //아무것도 해당되지 않을 때 기존 상태 반환
            return state;
    }
}

const Counter = () => {
    const [state, dispatch] = useReducer(reducer, {value:0});

    return (
        <div>
            <p>
                현재 카운터 값은 <b>{state.value}</b>입니다.
            </p>
            <button onClick={() => dispatch({type: 'INCREMENT'})}>+1</button>
            <button onClick={() => dispatch({type: 'DECREMENT'})}>-1</button>
        </div>
    );
};
export default Counter;
```

useReducer의 첫번째 파라미터에는 리듀서 함수, 두번째는 해당 리듀서의 기본값을 넣어 줌

이 Hook을 사용하면 state 값과 dispatch 함수를 받아 옴.

state :  현재 가리키고 있는 상태

dispatch:  액션을 발생시키는 함수

=> 함수 안에 파라미터로 액션 값을 넣어 주면 리듀서 함수가 호출되는 구조

useReducer 장점: 컴포넌트 업데이트 로직을 컴포넌트 바깥으로 빼낼 수 있음