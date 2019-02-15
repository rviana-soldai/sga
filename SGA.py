import Coin
import Individual

class SGA:

	def __init__(self, population_size, tournament_size, generations, 
		chromosome_size, mutation_probability, cross_probability):
	self.population_size = population_size
	self.tournament_size = tournament_size
	self.generations = generations
	self.chromosome_size = chromosome_size
	self.mutation_probability = mutation_probability 
	self.cross_probability = cross_probability
	self.mse = 0.0
	self.population = []
	self.best = None


	def initializePopulation(self):
		self.population = []
		for i in range(self.population_size):
			self.population.add(Individual(self.chromosome_size))
		self.best = self.population[0]