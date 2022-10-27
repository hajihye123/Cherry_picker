# 문제 풀 때 사용하는 문법 정리



## 입출력

### 방법 1 - input()

`input()`

- 숫자 여러 개 입력 받기

  `map(int, input().split())`

### 방법 2 - sys.stdin.readline()

- 이 방법은 input()보다 속도가 빠르다.

`import sys`
`sys.stdin.readline()`

- 숫자 여러 개 입력 받기

  `map(int, sys.stdin.readline().split())`

- 숫자 배열로 입력 받기

  `list(map(int, sys.stdin.readline().split()))`

## print() 서식

%d: 10진수 정수

%x: 16진수 정수

%o: 8진수 정수

%f: 실수

%c: 한 글자

%s: 문자열

- ### 예시

  `print("%d + %d = %d"%(1, 3, 4))`

  출력: 1 + 3 = 4

### 소수점 표현

- 소수점 아래 n 자리 표현

```
print("{:.3f}".format(num))		# 3 대신 다른 숫자를 넣으면 된다.
```

## try-except

```
try:
	명령
except:
	명령
```

## shallow copy & deep copy

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

## math

`import math`

- `math.ceil(num)`: 올림
- `math.floor(num)`: 버림

- `round(num)`: 반올림

### sum

- 숫자 i의 각 자릿수 합 구하기

  `sum((map(int, str(i))))`

## 정렬

- python의 정렬은 기본적으로 stable 정렬이다.

  ex) 카드의 숫자와 모양이 그대로 유지된 채로 정렬

- 내가 원하는 key로 정렬하는 법

  1. list의 길이순으로 정렬: `list.sort(key=len)`
  2. list가 다중 원소로 구성된 경우 원하는 원소로 정렬: `list.sort(key=lambda x: x[0])`

## 배열

- 2차원 배열 선언

  `배열 = [[0 for _ in range(10)] for _ in range(10)] `

- 3차원 배열 선언

  `배열 = [[[0 for _ in range(10)] for _ in range(10)] for _ range(10)]`

## 딕셔너리

1. 딕셔너리 초기화
   `딕셔너리이름 = {"key값" : "value값"} `
   `딕셔너리이름 = dict()`
2. key 중복 허용 X
3. key가 중복될 경우, 마지막에 입력된 key의 value를 출력

```
a = {"key1":"value1", "key2":"value2", "key1":"value3"}
print(a["key1"])

결과: value3
```

4. 원소 가져오기

   - get

     ```
     dict['key']
     dict.get('key', 0)		# default값 = 0
     ```

5. 값 넣기, 수정하기

   ```
   dict['key'] = 100
   ```

6. 값 삭제하기

   ```
   del dict['key']
   dict.pop('key', 0)		# 삭제하는 값 리턴하는데, key가 없을 경우 default값 = 0
   ```

7. 딕셔너리 순회하기

   ```
   for key in dict:
   	print(key)
   
   for key, value in dict:
   	print(key, value)
   ```

8. key, value 추출하기

   ```
   dict.keys()
   dict.values()
   dict.items()
   ```

   

