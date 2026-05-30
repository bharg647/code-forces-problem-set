if __name__ == "__main__":
    s = input()
    t = input()

    if len(s) != len(t):
        print("NO")
    else:
        is_reverse = True
        for i,_ in enumerate(s):
            if s[i] != t[len(t)-i-1]:
                is_reverse = False
                
        if is_reverse:
            print("YES")
        else:
            print("NO")



