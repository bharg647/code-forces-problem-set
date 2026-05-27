
def print_number_dominos(m: int, n: int) -> None:
    area = m*n
    
    if area % 2 == 0:
        print(area//2)
        return
    else:
        result = (area-1)//2
        print(result)

if __name__ == "__main__":
    [m,n] = [int(x) for x in input().split(" ")]

    print_number_dominos(m,n)
