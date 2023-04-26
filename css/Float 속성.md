# Float 속성
## float
* 붕 뜬 상태가되어서, 공간을 차지하지 않음
* `float` 상태끼리는 서로 공간을 차지
* 텍스트 등의 인라인 요소들도 `float` 요소에 밀려남

## clear
* 적용된 요소가 다른 `float`의 공간을 인정해줌

```css
.blue {
  float: none;
}
.red {
  float: left;
}
.green {
  float: right;
}
.gray {
  clear: both;
}
```