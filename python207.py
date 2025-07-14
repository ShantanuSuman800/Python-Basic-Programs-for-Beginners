# Program to get Kth Column of Matrix 
def getKthColumn(matrix, k): 
	column = [] 
	for i in range(len(matrix)): 
		column.append(matrix[i][k-1]) 
	
	return column 
 
matrix = [[1, 2, 3, 4], 
		[5, 6, 7, 8], 
		[9, 10, 11, 12]]

K = 2
KthColumn = getKthColumn(matrix, K) 
print(KthColumn)