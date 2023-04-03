N, K = map(int, input().split())
weight, value = [], []

for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)


def knapsack(maximum, wt, val, n):
    # maximum : 배낭의 무게 한도, wt : 각 물건의 무게, val : 각 물건의 가치, n : 물건의 개수
    # DP 문제 해결을 위해 이차원 행렬 생성
    arr = [[0 for x in range(maximum+1)] for x in range(n+1)]
    # 이차원 행렬의 모든 칸을 돌아가면서 탐색
    for row in range(n+1):
        for col in range(maximum+1):
            if not row or not col:           # 행의 인덱스가 0이거나 열의 인덱스가 0이면 전부 0의 값을 넣음
                arr[row][col] = 0
            elif wt[row-1] <= col:           # 현재 열 인덱스 값보다 이전에 넣은 물건의 가치가 작거나 같으면 실행
                # 현재 위치에는 같은 열, 위 행의 값과 
                # (현재 행 인덱스 - 1)의 인덱스를 갖는 물건의 가치와 그 물건의 가치에서 열 인덱스를 뺀 값을 열 인덱스로 하는
                # 위 행의 값을 더한 값 중 큰 값을 저장
                arr[row][col] = max(val[row-1]+arr[row-1][col - wt[row-1]], arr[row-1][col])
            else:                            # 현재 행의 현재 열 인덱스보다 이전 행의 현재 열 인덱스에 넣은 물건의 가치가 크면 계속 넣음
                arr[row][col] = arr[row-1][col]
    return arr[n][maximum]                   # 마지막 행렬에 위치한 값을 결과로 출력


rst = knapsack(K, weight, value, N)
print(rst)