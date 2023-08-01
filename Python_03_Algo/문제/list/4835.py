"""
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
"""

T = int(input())  # 테스트 케이스
for tc in range(1, T + 1):  # 테스트 케이스 반복
    N, M = map(int, input().split())
    # 배열의 길이 N과 구간 합의 길이 M을 입력받는다
    arr = list(map(int, input().split()))
    # 배열을 입력받는다

    # 구간합들의 변수를 초기화 시켜줌
    max_num = 0
    min_num = 1000000000
    # min_num 은 문제에서 주어진 배열안의 정수 1개의 범위가 아님 -> 여기서 틀렸음
    # 구간의 개수 최대값 * 범위 이상으로 할것

    # 구간 더하기가 이뤄지는 횟수 - 구간합이 행해지는 첫번째 인덱스
    for i in range(N - M + 1):

        # 각 구간 더하기 초기화
        sum_num = 0
    
        # i번 인덱스 이후의 M개의 정수의 범위
        for j in range(i, i + M):
             
            sum_num += arr[j]
            # 구간 더하기

        # 구간 더하기의 값이 이전에 저장된 max_num 보다 크다면
        if max_num < sum_num:
            max_num = sum_num

        # 구간 더하기의 값이 이전에 저장된 min_num 보다 작다면
        if min_num > sum_num:
            min_num = sum_num
    
    # 최대 구간합 - 최소 구간합
    ans = max_num - min_num

    print(f'#{tc}', ans)
