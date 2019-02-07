'''
Expecting receive data from monitor devices(blood oxygen, blood pressure, pulse)
Now receive data from other source file(txt file)
Format: float
float type_of_data represent the source of the data.(blood oxygen or pressure or else)
'''

class InputModule():
	def read(path):
		res = []
		#Since we do not have data from the sensor now, we assuse that data is already in txt file
		try:
			with open(path, 'r') as f:
				res=f.read.split()
		except:
			print("Reading data error")

		if len(res)==0:
			print("empty data")
			
		return res

bo = read(path_of_bo)
bp = read(path_of_bp)
pul = read(path_of_pul)