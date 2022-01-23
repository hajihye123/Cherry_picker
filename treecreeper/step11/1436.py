n = int(input())
cnt = 0
six = 666

while True:
    if '666' in str(six):
        cnt += 1
    if cnt == n:
        print(six)
        break
    six += 1    # 숫자를 붙이는게 아니라, 계속 +1 해서 666을 찾는 방식