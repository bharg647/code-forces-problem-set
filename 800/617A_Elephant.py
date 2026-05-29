if __name__ == "__main__":
    x = int(input())

    num_of_steps = 0
    while x > 0:
        if (x-5) >= 0:
            x = x-5
            num_of_steps += 1
        elif (x-4) >= 0:
            x = x-4
            num_of_steps += 1
        elif (x-3) >= 0:
            x = x-3
            num_of_steps += 1
        elif (x-2) >= 0:
            x = x-2
            num_of_steps += 1
        else:
            x = x-1
            num_of_steps += 1

    print(num_of_steps)
