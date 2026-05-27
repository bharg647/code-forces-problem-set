

if __name__ == "__main__":
    [n,k] = [int(x) for x in input().split(" ")]

    arr = [int(x) for x in input().split(" ")]

    arr.sort()

    num = arr[len(arr)-k]

    result = 0
    for x in arr:
        if x >= num and x > 0:
            result += 1
    
    print(result)
