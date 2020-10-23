from itertools import combinations
import numpy as np
import math
import json

N36 = 36
N64 = 64
N6 = 6
file_output = 'out.json'

def convert_vec2mat(vector):
	nrow = int(math.sqrt(N36))
	mat = []
	for i in range(nrow):
		row = []
		for j in range(nrow):
			row.append(vector[i*nrow + j])
		mat.append(row)
	return mat

if __name__ == '__main__':
	outputs = []
	bits = [0]*N36

	for i in range(2**N36):
		print('Iteration {}/{}...'.format(i, 2**N36))
		vector = []
		for j in range(N36-1,-1,-1):
			jump = 2**j
			if i != 0 and i%jump == 0:
				bits[j] = (bits[j] + 1)%2
			vector.append(bits[j])

		A = convert_vec2mat(vector)
		
		for x in range(N64):
			out = []
			inputs = bin(x)[2:]
			inputs = '0'*(N6-len(inputs))+inputs
			inputs = [int(b) for b in inputs]

			mat_x = np.array(inputs)
			mat_A = np.array(A)
			mat_n = np.matmul(mat_x, mat_A)%2
			# print(mat_x)
			# print(mat_A)
			# print(mat_n)

			n = ''
			for b in list(mat_n):
				n += str(b)

			n = int(n, 2)
			out.append(n)

		outputs.append(out)

	data = {'data': outputs}
	f = open(file_output, 'w')
	json.dump(data, f)
	f.close()

