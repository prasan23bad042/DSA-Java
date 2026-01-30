import sys
def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    ans = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int,data[idx:idx+n]))
        idx += n
        s = sum(a)
        if s % 2 == 1:
            ans.append("YES")
        else:
            odd = False
            even = False
            for v in a:
                if v % 2 == 0:
                    even = True
                else:
                    odd = True
                if odd and even:
                    break
            ans.append("YES" if odd and even else "NO")
    print("\n".join(ans))
if __name__ == "__main__":
    solve()
