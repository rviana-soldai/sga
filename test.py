from Individual import Individual
from SGA import SGA
import matplotlib.pyplot as plt
import numpy as np
from SevenOnes import SevenOnes 
from SevenZeros import SevenZeros

def plotError(errors, file=None):
	fig, ax = plt.subplots()
	ax.set(xlabel='Generacion', ylabel='Error', title='Error por generación')
	ax.legend('Leyenda')
	x = np.arange(0, 100)
	plt.plot(x, errors, 'b')
	if file:
		plt.savefig('data/' + file + '.png')
	plt.show()

i = Individual(7)
j = Individual(7)

print(i.print())
print(j.print())
for it in range(7):
	i.setBit(it, True)
	j.setBit(it, False)

print(i.print())
print(j.print())

sons = i.cross(2, j)
print(sons[0].print())
print(sons[1].print())

#population_size, tournament_size, generations, 
#chromosome_size, mutation_probability, cross_probability
sga = SGA(101, 5, 100, 10, 0.05, 0.95)
plotError(sga.crossValidation(), 'figura_error_all_1')
print("Best individual all ones " + sga.best.print() + " -> Score: " + str(sga.best.evaluation))

#Seven Ones exactly
svo = SevenOnes(99, 5, 100, 10, 0.05, 0.95)
plotError(svo.crossValidation(), 'figura_error_7_1')
print("Best individual seven ones " + svo.best.print() + " -> Score: " + str(svo.best.evaluation))


#First Seven Zeros
svz = SevenZeros(100, 5, 100, 10, 0.05, 0.95)
plotError(svz.crossValidation(), 'figura_error_7_0')
print("Best individual first seven zeros " + svz.best.print() + " -> Score: " + str(svz.best.evaluation))
