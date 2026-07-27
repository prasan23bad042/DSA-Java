import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    idx = 0
    t = int(data[idx])
    idx += 1

    out = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2

        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)

        # 1. Standard BFS to find shortest path from 1 to N and check parity
        dist = [-1] * (n + 1)
        parent = [0] * (n + 1)
        dist[1] = 0
        q = deque([1])

        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)

        if dist[n] == -1:
            out.append("-1")
            continue

        # Reconstruct shortest path
        path = []
        curr = n
        while curr != 0:
            path.append(curr)
            curr = parent[curr]
        path.reverse()

        # If the shortest path length is already even, it's optimal and simple!
        if len(path) % 2 == 1: # length = nodes - 1, so odd length means even number of nodes
            out.append(str(len(path) - 1))
            out.append(" ".join(map(str, path)))
            continue

        # 2. Shortest path is ODD. We need an EVEN simple path.
        # Find 2-parity states with BFS tracking explicit path nodes for small bounds,
        # or find an odd cycle reachable to detour through without self-intersection.
        
        # State BFS: (u, parity) -> state graph BFS
        # To ensure simplicity when shortest odd path exists, search for alternative paths.
        visited_state = {}
        # We perform a tracking BFS over (u, mask_of_visited) or (u, parity)
        # Since sum(N^3) <= 1000^3, we can do a localized search for even paths.
        
        found_path = None
        
        # BFS with path tracking for even simple path
        q_even = deque([(1, (1,))])
        seen_states = set([(1, 1)]) # (node, path_length % 2)

        while q_even:
            u, p_tuple = q_even.popleft()
            
            if u == n and (len(p_tuple) - 1) % 2 == 0:
                found_path = p_tuple
                break

            if len(p_tuple) > n + 2: # Cutoff depth for simple path search
                continue

            for v in adj[u]:
                if v not in p_tuple:
                    new_p = p_tuple + (v,)
                    new_parity = (len(new_p) - 1) % 2
                    
                    # We accept state if not seen with this parity or short path
                    state_key = (v, len(new_p))
                    if state_key not in seen_states:
                        seen_states.add(state_key)
                        q_even.append((u_next := v, new_p))
                        if v == n and new_parity == 0:
                            found_path = new_p
                            q_even.clear()
                            break

        if found_path and (len(found_path) - 1) % 2 == 0:
            out.append(str(len(found_path) - 1))
            out.append(" ".join(map(str, found_path)))
        else:
            out.append("-1")

    print("\n".join(out))
solve()
