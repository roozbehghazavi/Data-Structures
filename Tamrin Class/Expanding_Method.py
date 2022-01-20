import numpy as np

def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]




def determinant(mat):

	if(len(mat) == 2):
		value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
		return value

	Sum = 0

	# loop to traverse each column
	for current_column in range(len(mat)):

		sign = (-1) ** (current_column)
		sub_det = determinant(getcofactor(mat, 0, current_column))
		Sum += (sign * mat[0][current_column] * sub_det)


	return Sum



if __name__ == '__main__':

	mat = [[1, 0, 2, -1],
		[3, 0, 0, 5],
		[2, 1, 4, -3],
		[1, 0, 5, 2]]

	print('Determinant of this Matrix =', determinant(mat))
	
	

