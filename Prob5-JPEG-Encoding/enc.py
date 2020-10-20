file_name = "JPEG_Encoding-test_data_matrices.txt"
N = 8

def get_new_idx(idx, row, col):
	diago = row + col

	if diago <= N:
		sum_diago = int(diago*(diago+1)/2)
		if diago % 2 == 0:
			new_idx = sum_diago + col
		else:
			new_idx = sum_diago + row
	else:
		sum_diago = int(N*(N+1)/2)
		diago = diago - N
		sum_diago = sum_diago + diago*N - int(diago*(diago+1)/2)
		if diago % 2 == 1:
			new_idx = sum_diago + N - row - 1
		else:
			new_idx = sum_diago + N - col - 1

	return new_idx



def convert_mat2vec(matrix):
	vector = [0]*(N*N)
	for idx in range(N*N):
		col = idx % N
		row = int((idx - col)/N)
		vec_idx = get_new_idx(idx, row, col)
		vector[vec_idx] = matrix[row][col]

	return vector


def enc_example_algo(vector):
	n_pos_elements = sum([x for x in vector if x>0])
	b_pos_elements = bin(n_pos_elements)[2:]


if __name__ == '__main__':
	# f = open(file_name, 'r')
	# data = f.readlines()
	# f.close()

	# data = [line.replace(' \n', '') for line in data if line != '\n' and line != '']
	# data = [line.split(' ') for line in data]
	# data = [[int(c) for c in line] for line in data]

	# matrices = []
	# mat = []

	# for i, line in enumerate(data):
	# 	mat.append(line)
	# 	if i%N == N-1:
	# 		matrices.append(mat)
	# 		mat = []

	mat = [	[47, 9, 2, 0, 1, 0, 0 , 0], 
			[-12, 10, -1, -4, 0, 0, 0, 0], 
			[3, -5, 1, 0, 0, 0, 0, 0], 
			[1, -1, 0, 0, 0, 0, 0, 0], 
			[-2, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0]]

	vec = convert_mat2vec(mat)
	print(vec)
