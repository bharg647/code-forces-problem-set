if __name__ == "__main__":
    [n,h] = list(map(int, input().split()))
    list_of_heights = list(map(int, input().split()))

    current_amount = 0
    width = 0
    for height in list_of_heights:
        current_amount += height
        if current_amount < h:
            continue
        elif current_amount == h:
            current_amount = 0
            width += 1
        else:
            if (current_amount-height) != 0:
                width += 1
            
            if height > h:
                current_amount = 0
                width += 2
            elif height == h:
                current_amount = 0
                width += 1
            else: 
                current_amount = height

    if current_amount > 0:
        width += 1

    print(width)






