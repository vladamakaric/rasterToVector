def matrixSize(matrix):
	return len(matrix), len(matrix[0])

def isValidMatrixIndex(matrix,j,i):
	rows, cols = matrixSize(matrix)
	return 0 < j < rows and 0 < i < cols


