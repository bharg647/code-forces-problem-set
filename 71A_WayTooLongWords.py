
def print_abbr(s: str) -> None:
    if len(s) > 10:
        print(s[0]+str(len(s)-2)+s[len(s)-1])
    else:
        print(s)


if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        s = input()
        
        print_abbr(s)