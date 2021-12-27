# Ryan Franco
# CS610 Homework 3 Question 4

def matrix(mat1, mat2):
    resultxa =len(mat1[0])
    resultxb = len(mat1)
    resultya = len(mat2[0])
    resultyb = len(mat2)
    res = [[0 for x in range(resultxa)]
    for y in range (resultxb)]
     
    for i in range (resultxb):
        for j in range (resultyb):
            res[i][j] = 0
            for x in range(resultxa):           
                res[i][j] += (mat1[ i][x] *
                              mat2[ x][j])
    return res
mat1 = [[1,0,0], [-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(matrix(mat1, mat2))
mat1=[[0]]
mat2=[[0]]
print(matrix(mat1, mat2))
