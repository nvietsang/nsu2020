from itertools import combinations
import numpy as np

N6 = 6
N64 = 64

def convert_dec2bit(vector):
	bit_strings = []
	for v in vector:
		b = bin(v)[2:]
		b = '0'*(N6-len(b))+b
		bstr = [int(bit) for bit in b]
		bit_strings.append(bstr)

	return bit_strings

def func_xi(vector, cbnts):
	out = []
	for c in cbnts:
		s = 1
		if len(c) == 0:
			out.append(1)
		else:
			for idx in c:
				s *= vector[idx-1]
			out.append(s)

	return out



if __name__ == '__main__':
	S = [13,18,20,55,23,24,34, 1,
		62,49,11,40,36,59,61,30, 
		33,46,56,27,41,52,14,45, 
		 0,29,39, 4, 8, 7,17,50, 
		 2,54,12,47,35,44,58,25,
		10, 5,19,48,43,31,37, 6,
		21,26,32, 3,15,16,22,53,
		38,57,63,28,60,51, 9,42]

	x = [1, 2, 3, 4, 5, 6]
	cbnts = [] # combinations
	for i in range(N6+1):
		comb = combinations(x, i)
		for c in comb:
			cbnts.append(c)

	inputs = [i for i in range(N64)]
	outputs = S

	inputs = convert_dec2bit(inputs)
	outputs = convert_dec2bit(outputs)

	M = [[0]*N64 for _ in range(N64)]

	for i in range(N64):
		m = func_xi(inputs[i], cbnts)
		for j in range(N64):
			M[j][i] = m[j]

	AI = []
	for i in range(N6):
		si = []
		for j in range(N64):
			si.append(outputs[j][i])

		matSi = np.array(si)
		matM = np.array(M)
		matAI = np.matmul(matSi, np.linalg.inv(matM)) % 2

		AI.append([int(v) for v in list(matAI)])

	# for i in range(N64):
	# 	if AI[0][i] == 1:
	# 		print('{} - {}'.format(AI[0][i], cbnts[i]))

	for i, c in enumerate(cbnts):
		print('{}-{}-{}-{}-{}-{} : {}'.format(AI[0][i], AI[1][i], AI[2][i], AI[3][i], AI[4][i], AI[5][i], c))


	A = []
	for i in range(N6):
		row = []
		for j in range(N6):
			row.append(AI[j][i+1])
		A.append(row)

	B_cbnts = cbnts[N64-N6-1: N64-1]
	B = []

	for i in range(N64-N6-1, N64-1, 1):
		row = []
		for j in range(N6):
			row.append(AI[j][i])
		B.append(row)

	A1 = []
	for x in inputs:
		mat_x = np.array(x)
		mat_A = np.array(A)
		mat_n1 = np.matmul(mat_x, mat_A)%2
		n1 = ''
		for c in list(mat_n1):
			n1 += str(c)

		n1 = int(n1, 2)
		A1.append(n1)

	print(A1)

	print(B)
	B1 = []
	for y in outputs:
		mat_y =np.array(y)
		mat_B = np.array(B)
		mat_n2 = np.matmul(mat_y, np.linalg.inv(mat_B))%2
		n2 = ''
		for c in list(mat_n2):
			n2 += str(c)
		n2 = int(n2, 2)
		B1.append(n2)
	print(B1)



