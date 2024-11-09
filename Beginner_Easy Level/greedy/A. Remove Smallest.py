def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        # Sort the input array
        a.sort()
        
        # Iterate through the array
        for i in range(1, n):
            diff = a[i] - a[i - 1]
            if diff > 1:
                print("No")
                break
        else:
            print("Yes")

# Call the solve function
solve()
