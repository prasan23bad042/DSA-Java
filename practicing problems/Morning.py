import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        pin = data[i]
        
        current_pos = 1
        total_seconds = 0
        
        for char in pin:
            target_pos = 10 if char == '0' else int(char)
            
            total_seconds += abs(target_pos - current_pos) + 1
            
            current_pos = target_pos
            
        results.append(str(total_seconds))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
