if __name__ == "__main__":
    [k,n,w] = list(map(int, input().split()))
    
    total = 0
    for i in range(1,w+1):
        total += k*i

    borrow_amount = total-n
    if borrow_amount <= 0:
        print(0)
    else:
        print(borrow_amount)
