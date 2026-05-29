if __name__ == "__main__":
    temp=set()
    user_name = input()
    
    for c in user_name:
        temp.add(c)
        
    if len(temp) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")