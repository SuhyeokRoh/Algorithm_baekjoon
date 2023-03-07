from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = [0] * 10
    importance = []
    q = deque()
    diff = deque()

    for num in lst:
        q.append(num)
        diff.append(-1)
        cnt[num] += 1

    diff[M] = M

    for idx in range(10):
        if cnt[idx]:
            importance.append(idx)

    number = 0
    while True:
        rst = q.popleft()
        judge_num = diff.popleft()

        if rst == importance[-1]:
            number += 1
            cnt[rst] -= 1
            if judge_num == M:
                break
            if not cnt[rst]:
                importance.pop()
        else:
            q.append(rst)
            diff.append(judge_num)

    print(number)