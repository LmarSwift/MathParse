import re
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def __mul__(self):
    	return str(float(self.left) * float(self.right))

    def __add__(self):
    	return str(float(self.left) + float(self.right))

    def __sub__(self):
    	return str(float(self.left) - float(self.right))

    def __div__(self):
    	return str(float(self.left) / float(self.right))
    def __repr__(self):
    	return str((self.left, self.data, self.right))

    operation_mapping = {
		'+': __add__,
		'-': __sub__,
		'*': __mul__,
		'/': __div__,
	}

def brackets(expression):
	out = ""
	app = False
	for x in range (len(expression)):
		if (s[x]=='('):
			if (app):
				out = ""
			else:
				app = True
		if (app):
			out+=s[x]
			if (s[x]==')'):
				break
	return out

def parse(exp):
	ops = ('*','/','+','-')
	signs = []
	for each in range(len(exp)):
		if exp[each] in ops:
			signs.append(exp[each])
	return (re.findall(r'\d+\.?\d*', exp), signs)

def subTree(nums, ops, start):
	root = Tree()
	root.data = ops[start]
	root.left = nums[start]
	root.right = nums[start+1]
	del nums[start]
	del nums[start]
	nums = [root.operation_mapping[root.data](root)] + nums
	del ops[start]

	return (nums, ops)

def buildTree(parsed):
	muldiv = '*/'
	nums = parsed[0]
	ops = parsed[1]
	while (len([x for x in ops if x in muldiv]) > 0):
		if (ops[0] not in muldiv and ops[1] in muldiv):
			start=1
		else:
			start = 0
		subtree = subTree(nums, ops, start)
		nums = subtree[0]
		ops = subtree[1]
	while (len(ops) > 0):
		subtree = subTree(nums, ops, 0)
		nums = subtree[0]
		ops = subtree[1]
	return nums

def evaluate(s):
	while ('(' in s):
	    s = s.replace(brackets(s), buildTree(parse(brackets(s)))[0], 1)
	return buildTree(parse(s))[0]