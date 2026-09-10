```python
a, b = map(int, input().split())

first = 0
draw = 0
second = 0

for x in range(1, 7):
    d1 = abs(a - x)
    d2 = abs(b - x)

    if d1 < d2:
        first += 1
    elif d1 == d2:
        draw += 1
    else:
        second += 1

print(first, draw, second)
```
