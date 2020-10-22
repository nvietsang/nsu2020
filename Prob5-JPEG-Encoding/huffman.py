class Tree(object):
	def __init__(self, freq):
		self.freq = freq
		self.root = None

	def build_tree(self):
		nodes = [Node(k,v) for k,v in self.freq.items()]

		while len(nodes) > 1:
			nodes = sorted(nodes, key=lambda x: x.value, reverse=True)
			lnode = nodes[-1]
			rnode = nodes[-2]
			nodes = nodes[:-2]
			new_node = Node(lnode.name+rnode.name, lnode.value+rnode.value, lnode, rnode)
			nodes.append(new_node)

		self.root = nodes[0]
		return self.root

	def get_code(self):


class Node(object):
	"""docstring for Node"""
	def __init__(self, name, value, left=None, right=None):
		self.name = name
		self.value = value
		self.bit_string = ''
		self.left = left
		self.right = right

	def is_leaf(self):
		if not left and not right:
			return True
		else:
			return False

if __name__ == '__main__':
	freq = {'0': 0.05,
			'1': 0.2,
			'2': 0,
			'3': 0.2,
			'4': 0.1,
			'5': 0.25,
			'6': 0.05,
			'7': 0.15
			}

	message = ['1', '3', '3', '7', '1', '5', '4', '5', '1', '5', '5', '1', '3', '5', '7', '0', '6', '3', '4', '7']
	print(freq)
	Tree(freq).build_tree()