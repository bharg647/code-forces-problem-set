def print_number_dominos(m: int, n: int) -> None:
    area = m*n
    print(area//2)
        

if __name__ == "__main__":
    [m,n] = [int(x) for x in input().split(" ")]

    print_number_dominos(m,n)