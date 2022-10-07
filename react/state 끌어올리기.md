## State 끌어올리기
### 개념
* 부모 컴포넌트와 자식 컴포넌트가 있을 때 자식 컴포넌트가 부모 컴포넌트의 state 를 변경할 수 있는 방법
* 여러 자식 컴포넌트 사이에 공유하는 state가 있을때 state를 변경할때도 사용
* 단방향 데이터 흐름 원칙 준수

### 방법
1. 부모의 상태 변화 함수를 자식으로 넘겨준다.
2. 자식은 전달받은 상태 변화 함수를 사용하여 부모의 state 를 변경한다.

### 예제
* 자식이 부모의 숫자 state를 변경하는 간단 예제

```jsx
function Child({state, setState}) {
    const onClick = () => {
        setState(state + 1)
    }

    return (
        <div>
            <button onClick={onClick} />
            {state}
        </div>
    );
}

export default function Parent() {
    const [state, setState] = useState(0);

    return (
        <div>
            <p>this is Parent State</p>
            {state}
            <p>this is Child State</p>
            // state 끌어올리기
            <Child state={state} setState={setState}> 
        </div>
    );
}
```