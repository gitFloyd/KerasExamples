
class su:

	@staticmethod
	def YesNo(question):
		reply = str(input(question+' (y/n): ')).lower().strip()
		if reply[0] == 'y':
			return True
		if reply[0] == 'n':
			return False
		else:
			return su.YesNo("Invalid response. Please try again.")