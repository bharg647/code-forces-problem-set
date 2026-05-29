if __name__ == "__main__":
    [a,b] = list(map(int, input().split()))

    num_of_years = 0
    while a <= b:
        a *= 3
        b *= 2
        num_of_years += 1

    print(num_of_years)
