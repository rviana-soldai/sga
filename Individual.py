from Coin import Coin

class Individual:

	def __init__(self, lenght):
		self.lenght = lenght
		self.chromosome = []
		self.evaluation = 0
		c = Coin(0.5)
		for i in range(self.lenght):
			self.chromosome.append(c.toss())

	def setBit(self, n, value):
		self.chromosome[n] = value

	def toogleBit(self, n):
		self.chromosome[n] = not self.chromosome[n]

	def getBit(slef, n):
		return self.chromosome[n]

	def size(self):
		return self.lenght

	#TODO implement individual sons
	def cross(self, n, another):
		sons_0 = Individual(self.lenght)
		sons_1 = Individual(self.lenght)
		sons_0.chromosome = self.chromosome[:n] + another.chromosome[n:]
		sons_1.chromosome = another.chromosome[:n] + self.chromosome[n:]
		return [sons_0, sons_1]

	def print(self):
		ret = ''
		for bit in self.chromosome:
			if bit:
				ret += '1'
			else:
				ret += '0'
		return ret

