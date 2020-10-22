from dahuffman import HuffmanCodec

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

def enc_huffman_algo(vector, hmcode):
	bit_string = ''
	# n_pos_elements = len([x for x in vector if x!=0])
	# b_pos_elements = bin(n_pos_elements)[2:]
	# b_pos_elements = '0'*(6-len(b_pos_elements)) + b_pos_elements
	# bit_string += b_pos_elements

	for i in range(N*N-1, -1, -1):
		if vector[i] != '0':
			end_idx = i+1
			break

	vector = vector[:end_idx]
	for e in vector:
		if e == 0:
			e_bit_string = '0'
		else:
			e_bit_string = hmcode[str(e)]
			# e_bit_string = '1'*len(e_bit_string) + '0' + e_bit_string

		bit_string += e_bit_string

	return bit_string

def dec_huffman_algo(bit_string, root):
	message = []
	node = root
	for b in bit_string:
		if b == '0':
			node = node.left
		if b == '1':
			node = node.right
		if type(node) is str:
			message.append(node)
			node = root
	return message



def enc_example_algo(vector):
	bit_string = ''
	n_pos_elements = len([x for x in vector if x!=0])
	b_pos_elements = bin(n_pos_elements)[2:]
	b_pos_elements = '0'*(6-len(b_pos_elements)) + b_pos_elements
	bit_string += b_pos_elements

	for i in range(N*N-1, -1, -1):
		if vector[i] != 0:
			end_idx = i+1
			break

	vector = vector[:end_idx]

	for e in vector:
		if e == 0:
			e_bit_string = '0'
		elif e > 0:
			e_bit_string = bin(e)[2:]
			e_bit_string = '1'*len(e_bit_string) + '0' + e_bit_string
		else:
			e_bit_string = bin(abs(e))[2:]
			e_bit_string = '0' + e_bit_string[1:]
			e_bit_string = '1'*len(e_bit_string) + '0' + e_bit_string
		bit_string += e_bit_string

	return bit_string

def dec_example_algo(bit_string):
	vector = [0]*(N*N)
	b_non_zero = bit_string[:6]
	n_non_zero = int(b_non_zero, 2)
	bit_string = bit_string[6:]
	# assert bit_string[0] == '1'

	idx = 0
	while(len(bit_string) > 0):
		if bit_string[0] == '0':
			vector[idx] = 0
			bit_string = bit_string[1:]
		else:
			len_b = bit_string.index('0')
			sign = bit_string[len_b+1]
			bit_string = bit_string[len_b+1:]
			num_b = bit_string[:len_b]
			if sign == '0':
				num_b = '1' + num_b[1:]

			num = int(num_b, 2)
			if sign == '0':
				vector[idx] = -num
			else:
				vector[idx] = num

			bit_string = bit_string[len_b:]
		idx += 1

	return vector

class NodeTree(object):
	def __init__(self, left=None, right=None):
		self.left = left
		self.right = right

	def children(self):
		return (self.left, self.right)

	def nodes(self):
		return (self.left, self.right)

	def __str__(self):
		return '%s_%s' % (self.left, self.right)

def huffman_code_tree(node, left=True, binString=''):
	if type(node) is str:
		return {node: binString}
	(l, r) = node.children()
	d = dict()
	d.update(huffman_code_tree(l, True, binString + '0'))
	d.update(huffman_code_tree(r, False, binString + '1'))
	return d


if __name__ == '__main__':
	# TEST
	# mat = [	[47, 9, 2, 0, 1, 0, 0 , 0], 
	# 		[-12, 10, -1, -4, 0, 0, 0, 0], 
	# 		[3, -5, 1, 0, 0, 0, 0, 0], 
	# 		[1, -1, 0, 0, 0, 0, 0, 0], 
	# 		[-2, 0, 0, 0, 0, 0, 0, 0], 
	# 		[0, 0, 0, 0, 0, 0, 0, 0], 
	# 		[0, 0, 0, 0, 0, 0, 0, 0], 
	# 		[0, 0, 0, 0, 0, 0, 0, 0]]

	# vector = convert_mat2vec(mat)
	# bit_string = enc_example_algo(vec)
	# res = '0011101111110101111111101001111100100110111111010101101001001110001101110001001011110000101'
	# if bit_string == res:
	# 	print('Test OK!')
	# vector = dec_example_algo(bit_string)
	
	# READ FILE
	f = open(file_name, 'r')
	data = f.readlines()
	f.close()

	data = [line.replace(' \n', '') for line in data if line != '\n' and line != '']
	data = [line.split(' ') for line in data]
	data = [[int(c) for c in line] for line in data]

	matrices = []
	mat = []

	for i, line in enumerate(data):
		mat.append(line)
		if i%N == N-1:
			matrices.append(mat)
			mat = []

	# # GIVEN ALGO
	sum_len1 = 0
	for i, matrix in enumerate(matrices):
		vector = convert_mat2vec(matrix)
		bit_string = enc_example_algo(vector)
		len_b = len(bit_string)
		print('Matrix {} - bit-length: {}'.format(i, len_b))
		sum_len1 += len_b
		decoded = dec_example_algo(bit_string)
		assert decoded == vector

	print('Total bit-length: {}'.format(sum_len1))

	# HUFFMANN CODE
	# build tree
	string = []
	for matrix in matrices:
		vector = convert_mat2vec(matrix)
		for i in range(N*N-1, -1, -1):
			if vector[i] != 0:
				end_idx = i+1
				break
		vector = vector[:end_idx]
		for v in vector:
			string.append(str(v))
	
	freq = {}
	for c in string:
		if c in freq:
			freq[c] += 1
		else:
			freq[c] = 1

	freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
	nodes = freq

	while len(nodes) > 1:
		(key1, c1) = nodes[-1]
		(key2, c2) = nodes[-2]
		nodes = nodes[:-2]
		node = NodeTree(key1, key2)
		nodes.append((node, c1 + c2))
		nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

	root = nodes[0][0]
	huffmanCode = huffman_code_tree(root)

	# print(' Char | Huffman code ')
	# print('----------------------')
	# for (char, frequency) in freq:
	# 	print(' %-4r |%12s' % (char, huffmanCode[char]))


	# encode
	sum_len2 = 0
	for i, matrix in enumerate(matrices):
		vector = convert_mat2vec(matrix)
		vector = [str(c) for c in vector]
		bit_string = enc_huffman_algo(vector, huffmanCode)
		len_b = len(bit_string)
		print('Matrix {} - bit-length: {}'.format(i, len_b))
		sum_len2 += len_b
		decoded = dec_huffman_algo(bit_string, root)
		decoded = decoded + ['0']*(N*N-len(decoded))
		assert decoded == vector

	print('Total bit-length: {} - {}'.format(sum_len1, sum_len2))





