if __name__ == "__main__":
    n = int(input())
    s = input()

    count = 0
    for i,_ in enumerate(s):
        if i+1 < len(s) and s[i] == s[i+1]:
            count += 1
    
    print(count)
