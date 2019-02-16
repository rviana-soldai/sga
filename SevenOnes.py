from SGA import SGA
import math

class SevenOnes(SGA):

	def evaluateIndividual(self, individual):
		zeros = 0
		for i in range(self.chromosome_size):
			if not individual.getBit(i):
				zeros += 1
		return abs(zeros - 3) * 0.1