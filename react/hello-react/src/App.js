import React, { Fragment } from 'react';
import './App.css';
import MyComponent from './MyComponent';
import Counter from './Counter';
import Say from './Say';
import EventPractice from './EventPractice';

function App() {
  const style = {
    backgroundColor: 'black',
    color: 'aqua',
    fontSize: '60px',
    fontWeight: 'bold',
    padding: 30
  };
  const name = '리액트';
  return (
    <>
      <div className='react'>{name}</div>
      <input />
      //하지만 이런 주석이나
      /* 이런 주석은 페이지에 나옵니다.*/
      <MyComponent name="JINSOO" favoriteNumber={1} />
      <MyComponent favoriteNumber={1}>자식</MyComponent>
      <Counter />
      <Say />
      <EventPractice />
    </>
  );
}

export default App;
