
def get_operation(statement: str) -> int:
    if statement[0] == "+" or statement[2] == "+":
        return 1
    else:
        return -1

if __name__ == "__main__":
    n = int(input())

    x = 0
    for _ in range(n):
        x += get_operation(input())

    print(x)
