def solution(k, m, score):
    score.sort(reverse=True)
    lst = [[0] * m for _ in range(len(score)//m)]
    idx = row = col = 0
    
    while idx < len(score) and row < len(lst):
        lst[row][col] = score[idx]
        col, idx = col+1, idx+1
        if col == m:
            row, col = row+1, 0

    answer = 0
    for x in lst:
        answer += min(x) * m
    return answer