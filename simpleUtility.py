from io import StringIO 
import sys




#######################################
# function: dump(var)
# Input: one of the following -- str, int, list, tuple, set, dict, Numpy Array
# Return: none
# This function takes a list (or tuple, set, ...) and pretty prints it.
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
# class TextWrapper()
# Inherited by Hide and Pre
#
class TextWrapper():
	def __init__(self, tagname, classList=''):
		self.tagname = tagname
		self.classAttribute = '';
		if len(classList) > 0:
			self.classAttribute = ' class="{}"'.format(classList)
	def __enter__(self):
		print('<{}{}>'.format(self.tagname, self.classAttribute))
	def __exit__(self, *args):
		print('</{}>'.format(self.tagname))
#
# END OF class Hide()
#######################################


#######################################
# class Hide()
# Some library functions leak output
# to stdout. Use this class to hide
# that output.
# Usage:
# with Hide():
# 	# invoke leaky function
#
class Hide(TextWrapper):
	def __init__(self):
		super().__init__('div', 'hidden')
#
# END OF class Hide()
#######################################


#######################################
# class Pre()
# Used to wrap some output in <pre> and
# </pre> tags.
# Usage:
# with Pre():
# 	# code that outputs text
# 	# to stdout
#
class Pre(TextWrapper):
	def __init__(self):
		super().__init__('pre')
#
# END OF class Pre()
#######################################


#######################################
# nl2br(str)
# Input: a string to convert \n or \r\n to <br>
# Return: the converted string
# This function converts newline characters to <br>
#
def nl2br(var):
	return var.replace('\r\n','<br>').replace('\n','<br>')
#
# END OF nl2br()
#######################################


#######################################
# printbr(str)
# Input: a string to convert \n or \r\n to <br>
# Return: none
# This function converts newline characters to <br>
# and then invokes print(str_with_br)
#
def printbr(var):
	print(nl2br(var))
#
# END OF printbr()
#######################################


#######################################
# has_tf_and_gpu()
#
# Return: bool
# Is tensorflow available and does it
# have access to the gpu?
#
def has_tf_and_gpu():
	import tensorflow as tf
	return tf.test.is_gpu_available()
#
# END OF has_tf_and_gpu()
#######################################