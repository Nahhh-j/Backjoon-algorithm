# 비슷한 순열

'''
문제
1부터 n까지의 수들을 중복 없이 나열한 것을 순열이라 한다. 순열이 하나 주어졌을 때, 그 순열과 비슷한 순열들 중에서 제일 작은 것을 구하는 프로그램을 작성하시오.
순열이 비슷하다는 것은, 순열의 각 위치의 수들의 차이가 1 이하인 경우를 말한다. 순열의 크기를 비교할 때는 순열의 제일 앞의 수부터 차례로 비교한다.
예를 들어 [1, 2, 3]과 [2, 1, 3]은 비슷한 순열이고, [1, 2, 3]과 [3, 1, 2]는 1과 3의 차이가 2이므로 비슷한 순열이 아니다. n = 3일 때의 순열들을 작은 순서대로 나열하면 [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]이 된다.

입력
첫째 줄에 n(3 ≤ n ≤ 50,000)이 주어진다. 다음 줄에는 순열의 각 수를 나타내는 자연수가 n개 주어진다.

출력
첫째 줄에 답을 출력한다.
'''