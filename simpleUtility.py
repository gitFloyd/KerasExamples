




#######################################
# function: dump()
#
class _dump:
	def __init__(self, tab_size):
		if __name__ == '__main__':
			self.tabchar = ' ' * tab_size
			self.newlinechar = '\n'
		else:
			self.tabchar = '&nbsp;' * tab_size
			self.newlinechar = '<br>'
	
	def execute(self, var, depth = 0, prefix = ''):
		tab = ''.join([self.tabchar for num in range(0,depth)])
		typename = type(var).__name__
		if typename in ('int', 'str', 'float', 'float64'):
			return tab + prefix + str(var) + self.newlinechar
		elif typename == 'list' or typename == 'tuple' or typename == 'set' or typename == 'ndarray':
			brace = '['
			endbrace = ']'
			if typename == 'tuple':
				brace = '('
				endbrace = ')'
			elif typename == 'set':
				brace = '{'
				endbrace = '}'
			output = tab + prefix + brace + self.newlinechar
			output += ''.join([self.execute(value, depth+1) for value in var])
			output += tab +endbrace + self.newlinechar
			return output
		elif typename == 'dict':
			output = tab + prefix + '{' + self.newlinechar
			output += ''.join([self.execute(var[key], depth+1, key + ': ') for key in var.keys()])
			output += tab + '}' + self.newlinechar
			return output

def dump(var, tab_size = 4):
	print(_dump(tab_size).execute(var))
#
# END OF dump()
#######################################


#######################################
# printbr()
# 
# converts newline characters to <br>
#
def printbr(var):
	from io import StringIO
	from contextlib import redirect_stdout

	output = StringIO()
	with redirect_stdout(output):
		print(var)
	print(output.getvalue().replace('\r\n','<br>').replace('\n','<br>'))
#
# END OF printbr()
#######################################


#######################################
# has_tf_and_gpu()
#
# Is tensorflow available and does it
# have access to the gpu?
#
def has_tf_and_gpu():
	import tensorflow as tf
	return tf.test.is_gpu_available()
#
# END OF has_tf_and_gpu()
#######################################