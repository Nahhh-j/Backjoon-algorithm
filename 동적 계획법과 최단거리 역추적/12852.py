# 1로 만들기 2

'''
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.
'''

import sys
input = sys.stdin.readline

N = int(input())
mem = [0]*(N+1)
path = ["" for _ in range(N+1)]
path[1] = "1"

for idx in range(2, N+1):
    mem[idx] = mem[idx-1] + 1
    prev = idx-1
    if idx % 3 == 0 and mem[idx//3]+1 < mem[idx]:
        mem[idx] = mem[idx//3] + 1
        prev = idx // 3
    if idx % 2 == 0 and mem[idx//2]+1 < mem[idx]:
        mem[idx] = mem[idx//2] + 1
        prev = idx // 2
    path[idx] = str(idx) + " " + path[prev]

print(mem[N])
print(path[N])