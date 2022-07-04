# JSX 소개
## JSX 개념
* Javascript를 확장한 문법

## JSX 표현식
* 중괄호 `{}` 를 사용하여 JS 표현식을 넣을 수 있음
```JSX
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>;
```
* `if`, `for`, 변수, 파라미터, 함수 리턴 등으로 사용 가능
```JSX
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}
```
## JSX 어트리뷰트 정의
* 어트리뷰트에 따옴표 `""` 를 이용해 문자열을 정의
```JSX
const element = <a href="https://www.reactjs.org"> link </a>;
```
* 중괄호를 사용해 JS 표현식 사용 가능
```JSX
const element = <img src={user.avatarUrl}></img>;
```
* 따옴표 또는 중괄호를 단독으로 사용해야함 (두가지 동시 X)
* JSX 어트리뷰트는 카멜 표기법 사용
> class -> className

## JSX 자식 정의
* 태그안에 태그를 작성하여 자식 포함 가능
```JSX
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

## JSX의 인젝션 공격 방지
* 모든 값은 렌더링 전 문자열로 변환
* XSS 공격 방지 가능
```JSX
const title = response.potentiallyMaliciousInput;
// 이것은 안전합니다.
const element = <h1>{title}</h1>;
```

## JSX 컴파일
* Babel은 JSX를 `React.createElement()` 호출로 컴파일
* `React.createElement()`는 몇가지 검사 후 객체 생성
* 이렇게 생성된 객체는 `React Element`
* React는 `React Element`를 읽어서 DOM 구성 및 최신 상태 유지
* 아래 두 코드는 동일

```JSX
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);
```
```JSX
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```