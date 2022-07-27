class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        N, M = len(mat[0]), len(mat) # No. of rows and no. of columns of the given matrix
        T = r * c # Number of elements in the required matrix
        
        # If the number of elements of given matrix is not equal to the required matrix dimentions spalce
        
        if N*M != T:    return mat
        
        # Populating the output matrix with 0's
        output = [[0 for _ in range(c)] for _ in range(r)]
        
        k = 0
        for i in range(M):
            for j in range(N):
                output[k//c][k%c] = mat[i][j]
                k += 1
        return output