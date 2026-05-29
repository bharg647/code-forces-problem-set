if __name__ == "__main__":
    string_one = input().lower()
    string_two = input().lower()
    
    if string_one < string_two:
        print("-1")
    elif string_two < string_one:
        print("1")
    else:
        print("0")