import React, { Fragment } from 'react';
import './App.css';
import MyComponent from './MyComponent';
import Counter from './Counter';
import Say from './Say';
import EventPractice from './EventPractice';
import IterationSample from './IterationSample';

function UserAction() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
           alert(this.responseText);
       }
  };
  xhttp.open("POST", "http://52.72.27.238:8000/stock/", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(JSON.stringify({username: 'django', password: 'django'}));
}

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
      {/* <MyComponent name="JINSOO" favoriteNumber={1} />
      <MyComponent favoriteNumber={1}>자식</MyComponent>
      <Counter />
      <Say />
      <EventPractice />
      <IterationSample /> */}
      <button type="submit" onclick="UserAction()">Search</button>
    </>
  );
}

export default App;
