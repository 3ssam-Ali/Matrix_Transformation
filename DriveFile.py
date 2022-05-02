import MatrixTransformation as mt

if __name__ == "__main__":
    # a 2 x 3 x 4 matrix as an initial test
    mat = [
        [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]],
        [[3, 2, 31, 45],
        [57, 64, 72, 123],
        [91, 10, 181, 129]]
    ]
    flat=mt.MatList(mat) # passing the matrix within the constructor
    print(flat.getItem(1,1,0))
    
    flat2=mt.MatList()
    flat2.setList(mat)
    print(flat2.getItem(1,1,0))
