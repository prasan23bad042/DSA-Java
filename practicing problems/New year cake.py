t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    def calculate(white, dark):
        layers = 0
        size = 1

        while True:
            if layers % 2 == 0:
                if white < size:
                    break
                white -= size
            else:
                if dark < size:
                    break
                dark -= size

            layers += 1
            size *= 2

        return layers

    ans = max(calculate(a, b), calculate(b, a))
    print(ans)
  
