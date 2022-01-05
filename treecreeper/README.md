# 입출력

## 방법 1 - input()

`input()`

- 숫자 여러 개 입력 받기

  `map(int, input().split())`

## 방법 2 - sys.stdin.readline()

- 이 방법은 input()보다 속도가 빠르다.

`import sys`
`sys.stdin.readline()`

- 숫자 여러 개 입력 받기

  `map(int, sys.stdin.readline().split())`

- 숫자 배열로 입력 받기

  `list(map(int, sys.stdin.readline().split()))`

# print() 서식

%d: 10진수 정수

%x: 16진수 정수

%o: 8진수 정수

%f: 실수

%c: 한 글자

%s: 문자열

- 예시

  `print("%d + %d = %d"%(1, 3, 4))`

  출력: 1 + 3 = 4

### 소수점 표현

- 소수점 아래 n 자리 표현

```
print("{:.3f}".format(num))		# 3 대신 다른 숫자를 넣으면 된다.
```

# try-except

```
try:
	명령
except:
	명령
```

# shallow copy & deep copy

shallow copy(얕은 복사)

```
import copy
a = [1, 2, 3]
b = copy.copy(a)
```

- 단순한 대입, 슬라이싱 또한 얕은 복사이다.

deep copy(깊은 복사)

```
import copy
a = [1, 2, 3]
b = copy.deepcopy(a)
```

