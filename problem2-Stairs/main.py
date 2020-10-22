from itertools import combinations
import numpy as np

def convert_dec2bit(vector):
	bit_strings = []
	for v in vector:
		b = bin(v)[2:]
		b = '0'*(6-len(b))+b
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
				s *= vector[idx]
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

	x = [0, 1, 2, 3, 4, 5]
	cbnts = [] # combinations
	for i in range(7):
		comb = combinations(x, i)
		for c in comb:
			cbnts.append(c)

	inputs = [i for i in range(64)]
	outputs = S

	inputs = convert_dec2bit(inputs)
	outputs = convert_dec2bit(outputs)

	M = [[0]*64 for _ in range(64)]

	for i in range(64):
		m = func_xi(inputs[i], cbnts)
		for j in range(64):
			M[j][i] = m[j]

	AI = []
	for i in range(6):
		si = []
		for j in range(64):
			si.append(outputs[j][i])

		matSi = np.array(si)
		matM = np.array(M)
		matAI = np.matmul(matSi, np.linalg.inv(matM)) % 2

		AI.append([int(v) for v in list(matAI)])

	for i in range(64):
		if AI[0][i] == 1:
			print('{} - {}'.format(AI[0][i], cbnts[i]))
