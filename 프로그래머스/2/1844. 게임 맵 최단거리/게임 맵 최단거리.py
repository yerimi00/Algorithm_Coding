from collections import deque


def solution(maps):
    N, M = len(maps), len(maps[0])
    answer = deque([(0, 0)])
    
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    
    while answer:
        x, y = answer.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                answer.append((nx, ny))
    
    return maps[N-1][M-1] if maps[N-1][M-1] != 1 else -1