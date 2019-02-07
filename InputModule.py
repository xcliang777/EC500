class InputModule():
	def read(path):
		res = []
		try:
			with open(path, 'r') as f:
				res=f.read.split()
		except:
			print("Reading data error")

		if len(res)==0:
			print("empty data")
			
		return res

bo = read(path1)
bp = read(path2)
pul = read(path3)