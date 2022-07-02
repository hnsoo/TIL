# 백준 2460번
# 지능형 기차2

result = 0
_max = 0
for i in range(10):
    _out, _in = map(int, input().split())
    result = result - _out + _in
    if _max < result:
        _max = result
print(_max)