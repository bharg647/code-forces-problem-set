if __name__ == "__main__":
    n = int(input())
    
    ans = 0
    for _ in range(n):
        arr = input().split(" ")
        
        num = arr.count("1")
        
        if num >= 2:
            ans += 1
    
    print(ans)   