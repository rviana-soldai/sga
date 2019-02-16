from SGA import SGA
import math

class SevenZeros(SGA):

	def evaluateIndividual(self, individual):
		error = 0
		for i in range(7):
			if individual.getBit(i):
				error += 0.14
		return error