#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Genetic Algorithm

This script allows the user to optimize a context words.

This file can also be imported as a module and contains the following
methods:
     *initializePupulation - initialize a population
     *evaluateIndividual - retrun individual error
     *evaluate - return the mean square error of a population
     *select - return a population optimizing tournament strategy
     *cross - return the new population with the cross of individuals
     *mutate - create a new population with a chromossome swift based in a coin probability
     *runGeneration - return the mean square error of the new generation
     *crossValidation - return a list of mean square errors obtained in each generation
"""
import random
import datetime
from sga.Coin import Coin
from sga.Individual import Individual

class SGA:
    """
    A class used to evolve a context making a new generation of the population, 
    mutating inindividuals, making a cross, evaluating the new individuals.

    Attributes
    ----------
    population_size : int
        size of the population
    tournament_size : int
        the size of the tournament
    generations : int
        how many generations want to evolve
    chromosome_size : int
        the size of chromose of each individual
    mutation_probability : float
        the probability of an individual of mutate or not
    cross_propability : float
        the probability of each individual to cross with another
    mse : float
        the mean square error 
    population : list
        the list of individuals
    best : Individual
        the individual with the best evaluation
    generation : int
        the number of generation to run
    data_dir : str
        the path to load and write the data data

    Methods
    -------
    initializePopulation()
        Generate a population adding individuals according to the population_size
    evaluateIndividual(Individual)
        Evaluate an individual errors
    evaluate()
        Evaluate each individual of a population
    select()
        Generate a population selecting an individual of a sorted list of individuals
    cross()
        Generate a new population using the cross probability
    mutate()
        Mutate an individual chromosome bit according to mutation_probability
    runGeneration()
        Evaluate, select,cross and mutate individuals of a population in each generation
    crossValidation()
        Technique to validate the sga algorithm
    """
    def __init__(self, population_size, tournament_size, generations, chromosome_size, 
                 mutation_probability, cross_probability, data_dir='data/'):
        """
        Parameters
        ----------
        population_size : int
            size of the population
        tournament_size : int
            the size of the tournament
        generations : int
            how many generations want to evolve
        chromosome_size : int
            the size of chromose of each individual
        mutation_probability : float
            the probability of an individual of mutate or not
        cross_propability : float
            the probability of each individual to cross with another
        mse : float
            the mean square error 
        population : list
            the list of individuals
        best : Individual
            the individual with the best evaluation
        generation : int
            the number of generation to run
        data_dir : str
            the path to load the individuals data

        """
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.generations = generations
        self.chromosome_size = chromosome_size
        self.mutation_probability = mutation_probability
        self.cross_probability = cross_probability
        self.mse = 0.0
        self.population = []
        self.best = None
        self.generation = 0
        self.data_dir = data_dir
        #self.initializePopulation()

    def initializePopulation(self):
        """Generate a population appending individuals in population list            
        """
        self.population = []
        for i in range(self.population_size):
            self.population.append(Individual(self.chromosome_size))
        self.best = self.population[0]
        self.best.evaluation = self.evaluateIndividual(self.population[0])

    def evaluateIndividual(self, individual):
        """
        Evaluate the chromosome bits of an individual

        Parameters
        ----------
        individual : Individual
            A class that represent an individual

        Return
        ------
        errors
            If the value of eachbit is 0 add 0.1 to errors variable
        """
        errors = 0
        for gen in individual.chromosome:
            if not gen:
                errors += 0.1
        return errors

    def evaluate(self):
        """ Evaluate each Individual of a population

        Return
        ------
        mse
           The mean square error of a population
        """
        min_error = 100.0
        sum_error = 0.0

        for i in range(self.population_size):
            print("Evaluating individual " + str(i) + " of generation " + str(self.generation))
            evaluation = self.evaluateIndividual(self.population[i])
            self.population[i].evaluation = evaluation

            if evaluation < min_error:
                min_error = evaluation
                if self.best.evaluation >= evaluation:
                    self.best = self.population[i].copy()

            sum_error += evaluation

        self.mse = sum_error / self.population_size
        return self.mse

    # Optimized tournament strategy
    def select(self):
        """Generates a new population using a optimized tournament strategy
        """
        new_population = []
        for i in range(self.population_size):
            individuals = self.population[i:i + self.tournament_size]
            if i + self.tournament_size >= self.population_size:
                individuals += self.population[0:(i - self.population_size)]
            individuals.sort(key=lambda x: x.evaluation)
            new_population.append(individuals[0])
        self.population = new_population

    def cross(self):
        """ Makes a cross to generate new individuals according to a
        probability
        """
        c = Coin(self.cross_probability)
        new_population = []

        for i in range(int(self.population_size) // 2):
            individual_1 = self.population[i * 2]
            individual_2 = self.population[i * 2 + 1]

            if c.toss():
                cross_point = random.randint(0, self.chromosome_size)
                new_population += individual_1.cross(cross_point, individual_2)
            else:
                new_population += [individual_1, individual_2]

        i = 0
        while len(new_population) < self.population_size:
            new_population.append(self.population[i])
            i += 1
        self.population = new_population

    def mutate(self):
        """In a population toggle an individual chromosome bit according to 
        a probability 
        """
        c = Coin(self.mutation_probability)
        for i in range(self.population_size):
            for j in range(self.chromosome_size):
                if c.toss():
                    self.population[i].toggleBit(j)

    def runGeneration(self):
        """Use the evaluate function to get the mean square error of the population,
        select to get the best individual in a new population using a tournament
        strategy, cross to reproduce the individuals,mutate to generate a change in 
        an individual chromosome, all of this cycle represent a new generation

        Return
        ------
        mse
           The mean square error of each new generation
        """
        self.generation += 1
        self.evaluate()
        self.select()
        self.cross()
        self.mutate()
        return self.mse

    def crossValidation(self):
        """Creates new generation according to the generation variable, append
        each generation error in a list and return that variable

        Return
        list
           A list of errors values in each generation
        """
        generation_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
        individuals = open(self.data_dir + "individuals_" + generation_time + ".log", "w")
        error = open(self.data_dir + "errors_" + generation_time + ".log", "w")
        errors = []
        for i in range(self.generations):
            self.runGeneration()
            print("Error " + str(self.mse))
            print("Best individual of generation " + str(i) + " " + str(self.best))
            error.write(str(self.mse) + ",")
            individuals.write(str(self.best) + "\n")
            errors.append(self.mse)
            if i % 10 == 0:
                self.mutation_probability = 0.8 * self.mutation_probability
        error.write(str(self.mse))
        individuals.write(str(self.best) + "\n")
        individuals.close()
        error.close()
        return errors
