import sys

def solve():
    # Read all input at once for maximum speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # t is the number of test cases
    t = int(input_data[0])
    ptr = 1
    results = []
    
    for _ in range(t):
        # n is the number of friends in current test case
        n = int(input_data[ptr])
        ptr += 1
        
        # a is the list of candies each friend has
        # Slicing and mapping is faster than a manual loop in Python
        a = list(map(int, input_data[ptr : ptr + n]))
        ptr += n
        
        total_sum = sum(a)
        
        # Case 1: Total candies cannot be divided equally
        if total_sum % n != 0:
            results.append("-1")
        else:
            # Case 2: Calculate target average
            avg = total_sum // n
            
            # Minimum k is the number of friends with candies > avg
            # These are the only people we MUST pick to redistribute their excess
            k = 0
            for candies in a:
                if candies > avg:
                    k += 1
            results.append(str(k))
    
    # Print all results separated by newlines
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()