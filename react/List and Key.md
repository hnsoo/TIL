## List and Key
### 여러개의 컴포넌트 렌더링
여러개의 컴포넌트를 한번에 렌더링 시키기 위해서는 map 함수를 이용
```jsx
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    <li key={number.toString()}>
      {number}
    </li>
  );
  return (
    <ul>{listItems}</ul>
  );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```
### Key
* React가 어떤 항목을 식별하는 것을 도움
* 배열 내부의 엘리먼트에 지정
* 다른 항목들 사이에서 해당 항목을 고유하게 식별할 수 있는 문자열을 사용
* 주로 데이터의 고유 ID를 사용
* 고유 ID가 없을 경우 리스트 인덱스를 사용하나 추천하지 않음
```jsx
const todoItems = todos.map((todo) =>
  <li key={todo.id}>
    {todo.text}
  </li>
);
```
### Key는 형제 사이에서만 고유한 값
* Key는 배열 안에서 고유해야 하고 전체 범위에서 고유할 필요는 없음
* 두 개의 다른 배열을 만들 때 동일한 key를 사용 가능
```jsx
function Blog(props) {
  const sidebar = (
    <ul>
      {props.posts.map((post) =>
        <li key={post.id}>
          {post.title}
        </li>
      )}
    </ul>
  );
  const content = props.posts.map((post) =>
    <div key={post.id}>
      <h3>{post.title}</h3>
      <p>{post.content}</p>
    </div>
  );
  return (
    <div>
      {sidebar}
      <hr />
      {content}
    </div>
  );
}

const posts = [
  {id: 1, title: 'Hello World', content: 'Welcome to learning React!'},
  {id: 2, title: 'Installation', content: 'You can install React from npm.'}
];
ReactDOM.render(
  <Blog posts={posts} />,
  document.getElementById('root')
);
```
### JSX에 map() 포함 시키기
```jsx
function NumberList(props) {
  const numbers = props.numbers;
  return (
    <ul>
      {numbers.map((number) =>
        <ListItem key={number.toString()}
                  value={number} />
      )}
    </ul>
  );
}
````