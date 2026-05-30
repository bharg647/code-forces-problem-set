if __name__ == "__main__":
    _ = input()
    s = input()

    num_of_a = 0
    num_of_d = 0
    for c in s:
        if c == 'A':
            num_of_a += 1
        else:
            num_of_d += 1

    if num_of_a > num_of_d:
        print("Anton")
    elif num_of_a < num_of_d:
        print("Danik")
    else:
        print("Friendship")
