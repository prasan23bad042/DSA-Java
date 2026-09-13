from collections import deque

class Solution:
    def solve(self):
        t = int(input())

        for _ in range(t):
            n = int(input())
            grid = [input().strip() for _ in range(2)]

            q = deque([(0, 0)])
            visited = [[False] * n for _ in range(2)]
            visited[0][0] = True

            while q:
                r, c = q.popleft()

                if r == 1 and c == n - 1:
                    break

                for nr in range(max(0, r - 1), min(2, r + 2)):
                    for nc in range(max(0, c - 1), min(n, c + 2)):
                        if (not visited[nr][nc] and
                            grid[nr][nc] == '0'):

                            visited[nr][nc] = True
                            q.append((nr, nc))

            print("YES" if visited[1][n - 1] else "NO")


Solution().solve()
