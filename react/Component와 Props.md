## Components와 Props
### 함수 컴포넌트
* JavaScript 함수
* 객체 인자를 받은 후 React 엘리먼트 반환
```JSX
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```
### 클래스 컴포넌트
```JSX
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```
### 사용자 정의 컴포넌트
* 항상 대문자로 시작
* JSX 어트리뷰트로 props 전달
```JSX
const element = <Welcome name="Sara" />;
```
### 컴포넌트 렌더링
1. `<Welcome name="Sara" />` 엘리먼트로 `ReactDOM.render()`를 호출
2. React는 `{name: 'Sara'}`를 props로 하여 `Welcome` 컴포넌트를 호출
3. `Welcome` 컴포넌트는 결과적으로 `<h1>Hello, Sara</h1>` 엘리먼트를 반환
4. React DOM은 `<h1>Hello, Sara</h1>`엘리먼트와 일치하도록 DOM을 효율적으로 업데이트
```JSX
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="Sara" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```
### 컴포넌트 합성
* 컴포넌트의 재사용가능
```JSX
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```
### 컴포넌트 추출
* 컴포넌트 합성을 통해 기능별로 컴포넌트 분리 가능

### props는 읽기 전용
* **모든 React 컴포넌트는 자신의 props를 다룰 때 반드시 순수 함수처럼 동작해야함**

#### 순수함수
* 입력값을 수정하지 않음
* 동일한 입력값에 대해 동일한 결과를 반환
```javascript
// 입력값 a, b의 값을 수정하지 않음
function sum(a, b) {
  return a + b;
}
```
#### 순수함수가 아님
```javascript
// 입력값을 수정함
function withdraw(account, amount) {
  account.total -= amount;
}
```