# 입출력

## 방법 1 - input()

`input()`

- 숫자 여러 개 입력받기

  `map(int, input().split())`

## 방법 2 - input() 보다 빠른 방법

`import sys`

`sys.stdin.readline()`

# print() 서식

%d: 10진수 정수

%x: 16진수 정수

%o: 8진수 정수

%f: 실수

%c: 한 글자

%s: 문자열

- 예시

  `print("%d + %d = %d"%(1, 3, 4))`

  