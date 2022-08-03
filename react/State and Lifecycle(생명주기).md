## State and Lifecycle(생명주기)
### 함수에서 클래스로 변환
1. `React.Component`를 확장하는 동일한 이름의 ES6 class를 생성
2. `render()`라고 불리는 빈 메서드를 추가
3. 함수의 내용을 `render()` 메서드 안으로 이동
4. `render()` 내용 안에 있는 `props`를 `this.props`로 변경
5. 남아있는 빈 함수 선언을 삭제
```JSX
// 함수형 컴포넌트
function Clock(props) {
  return (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {props.date.toLocaleTimeString()}.</h2>
    </div>
  );
}

function tick() {
  ReactDOM.render(
    <Clock date={new Date()} />,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
```
```JSX
// 클래스형 컴포넌트
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.props.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

function tick() {
  root.render(<Clock date={new Date()} />);
}

setInterval(tick, 1000);
```
### 클래스에 로컬 State 추가하기
1. render() 메서드 안에 있는 this.props.date를 this.state.date로 변경
2. 초기 this.state를 지정하는 class constructor를 추가
3. <Clock /> 요소에서 date prop을 삭제
```JSX
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```
### 생명주기 메서드
* 마운트: 컴포넌트가 DOM에 렌더링 되는 것 `componentDidMount()`
* 언마운트: 마운트된 컴포넌트가 삭제되는 것 `componentWillUnMount()`

### 타이머 동작 과정(생명주기 메서드 포함)
1. `<Clock />`가 `ReactDOM.render()`로 전달되었을 때 React는 Clock 컴포넌트의 constructor를 호출하여 `this.state`를 초기화
2. React는 Clock 컴포넌트의 `render()` 메서드를 호출하여 React는 화면에 표시되어야 할 내용을 알게되고 React는 Clock의 렌더링 출력값을 일치시키기 위해 DOM을 업데이트
3. Clock 출력값이 DOM에 삽입되면, React는 `componentDidMount()` 생명주기 메서드를 호출하고 그 안에서 Clock 컴포넌트는 매초 컴포넌트의 `tick()` 메서드를 호출하기 위한 타이머를 설정하도록 브라우저에 요청
4. 매초 브라우저가 `tick()` 메서드를 호출. 그 안에서 Clock 컴포넌트는 `setState()`에 현재 시각을 포함하는 객체를 호출하면서 UI 업데이트를 진행. `setState()` 호출 덕분에 React는 `state`가 변경된 것을 인지하고 화면에 표시될 내용을 알아내기 위해 `render()` 메서드를 다시 호출. 이 때 `render()` 메서드 안의 `this.state.date`가 달라지고 렌더링 출력값은 업데이트된 시각을 포함하고 React는 이에 따라 DOM을 업데이트.
5. Clock 컴포넌트가 DOM으로부터 한 번이라도 삭제된 적이 있다면 React는 타이머를 멈추기 위해 `componentWillUnmount()` 생명주기 메서드를 호출
```JSX
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```
### 올바른 State 사용법
#### 직접 State 수정 금지
```JSX
// Wrong
this.state.comment = 'Hello';

// Correct
this.setState({comment: 'Hello'});
```
#### state 업데이트는 비동기
this.props와 this.state는 비동기적으로 업데이트 될 수 있기 때문에 함수를 이용
 ```JSX
// Wrong
this.setState({
  counter: this.state.counter + this.props.increment,
});

// Correct
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```
#### state 업데이트는 병합 가능
 ```JSX
 constructor(props) {
    super(props);
    this.state = {
      posts: [],
      comments: []
    };
  }

  componentDidMount() {
    fetchPosts().then(response => {
      this.setState({
        posts: response.posts
      });
    });

    fetchComments().then(response => {
      this.setState({
        comments: response.comments
      });
    });
  }
```
### 올바른 State 사용법
* state는 로컬 또는 캡슐화
* state를 소유한 컴포넌트만 접근 가능
* 컴포넌트는 자신의 state를 자식 컴포넌트 props로 전달 할 수 있음
* 전달받은 자식 컴포넌트는 전달 받은 props가 부모의 state인지, props인지, 직접 입력한 것인지 구분 불가능
```JSX
<FormattedDate date={this.state.date} />

function FormattedDate(props) {
  return <h2>It is {props.date.toLocaleTimeString()}.</h2>;
}
```