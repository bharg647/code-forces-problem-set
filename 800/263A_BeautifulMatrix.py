if __name__ == "__main__":
    
    one_index = None
    for i in range(5):
        matrix_row = input().split()
        if "1" in matrix_row:
            one_index = (i, matrix_row.index("1"))
            break
    
    target_index = (2,2)
    
    min_moves = abs(one_index[0]-target_index[0])+abs(one_index[1]-target_index[1])
    print(min_moves)