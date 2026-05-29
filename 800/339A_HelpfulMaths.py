if __name__ == "__main__":
    num_list = list(map(int, input().split("+")))
    num_list.sort()
    print("+".join(map(str,num_list)))