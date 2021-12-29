# 입출력

## 방법 1 - input()

`input()`

- 숫자 여러 개 입력 받기

  `map(int, input().split())`

## 방법 2 - sys.stdin.readline()

- 이 방법은 input()보다 속도가 빠르다.

`import sys
sys.stdin.readline()`

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