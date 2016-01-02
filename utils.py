def matrixSize(matrix):
	return len(matrix), len(matrix[0])

def isValidMatrixIndex(rows, cols, j,i):
	return 0 <= j < rows and 0 <= i < cols


