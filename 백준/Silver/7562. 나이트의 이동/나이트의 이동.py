knight = [(1, 2), (2, 1), (2, -1), (1, -2), (-2, -1), (-2, 1), (-1, 2), (-1, -2)]


def knight_move(start, end):
    queue = [start + [0]]
    rear, front = 0, -1
    while front != rear:
        front += 1
        start = queue[front]
        if start[:-1] == end:
            return start[-1]
        visit[start[0]][start[1]] = True
        for x, y in knight:
            nx, ny = start[0] + x, start[1] + y
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                rear += 1
                queue.append([nx, ny, start[-1] + 1])
                visit[nx][ny] = True


for _ in range(int(input())):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    start, end = list(map(int, input().split())), list(map(int, input().split()))
    print(knight_move(start, end))