#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Individual

This class represent a individual in a population

This file can also be imported as a module and contains the following
methods:
     *setBit - Set the bit n of a chromosome to a new value
     *toggleBit - toggle the bit n of an individual chromosome
     *getBit - return the bit n of an individual chromosome
     *size - return the lenght of the individual chromosome
     *copy - return a copy of the indiviual
     *cross - return two new individuals
     *activeGens - return the number of chromosome bit active(1)
     *getActivationPercentage - return a percentage ofgens activated
     *__str__ -change the numberto string representation of individual chromosome

"""
from sga.Coin import Coin


class Individual:
    """
    A class used to represent an Individual

    Attributes
    ----------
    lenght : int
       The size of a chromosome
    chromosome : list
       List of zeros and ones that represent a chromosome
    evaluation : float
       Float number that represent how good is the individual

    Methods
    -------
    setBit(n,value) 
        Set the bit n of a chromosome to a new value
    toggleBit(n) 
        toggle the bit n of an individual chromosome
    getBit(n) 
        return the bit n of an individual chromosome
    size 
        return the lenght of the individual chromosome
    copy 
        return a copy of the indiviual
    cross(n, another) 
        return two new individuals
    activeGens 
        return the number of chromosome bit active(1)
    getActivationPercentage 
        return a percentage ofgens activated
    __str__ 
        change the number to string representation of individual chromosome
    """

    def __init__(self, lenght):
        """
        Parameters
        ----------
        lenght : int
           The size of a chromosome
        chromosome : list
           List of zeros and ones that represent a chromosome
        evaluation : float
           Float number that represent how good is the individual

        """
        self.lenght = lenght
        self.chromosome = []
        self.evaluation = 0
        c = Coin(0.5)
        for i in range(self.lenght):
            self.chromosome.append(c.toss())

    def setBit(self, n, value):
        """ Set the value of a chromosome bit in the position n

        Parameters
        ----------

        n : int
          The position of a bit in the chromosome
        value : int
          A value of the bit chromosome (0 or 1)
        """
        self.chromosome[n] = value

    def toggleBit(self, n):
        """ Toggle the value of a chromosome bit in the position n

        Parameters
        ----------

        n : int
          The position of a bit in the chromosome
        """
        self.chromosome[n] = not self.chromosome[n]

    def getBit(self, n):
        """ Return the value of a chromosome bit in the position n

        Parameters
        ----------

        n : int
          The position of a bit in the chromosome

        Return
        ------
        int
          The value of the bit
        """
        return self.chromosome[n]

    def size(self):
        """ Return the size of the chromosome

        Return
        ------
        int
          The size of the chromosome
        """
        return self.lenght

    def copy(self):
        """ Return a copy of an Individual


        Return
        ------
        Individual
          Copy of individual class
        """
        copy = Individual(self.lenght)
        copy.chromosome = []
        for gen in self.chromosome:
            copy.chromosome.append(gen)
        copy.evaluation = self.evaluation
        return copy

    # TODO implement individual sons
    def cross(self, n, another):
        """ Return two individuals building the chromosome of each one and split with
        value of n

        Parameters
        ----------

        n : int
          The value to split the chromosome
        another : Individual
          An Individual to make the cross
        
        Return
        ------
        list
          list of two new Individuals
        """
        sons_0 = Individual(self.lenght)
        sons_1 = Individual(self.lenght)
        sons_0.chromosome = self.chromosome[:n] + another.chromosome[n:]
        sons_1.chromosome = another.chromosome[:n] + self.chromosome[n:]
        return [sons_0, sons_1]
    
    def activeGens(self):
        """ Return the number of actived bits
        
        Return
        ------
        int
          The number of actived bits
        """
        active = 0.0
        for i in range(self.lenght):
            if self.chromosome[i]:
                active += 1
        return active
    
    def getActivationPercentage(self):
        """ Return the percentage of activated bits with respect 
        chromosome lenght
        
        Return
        ------
        float
          A percentage of activated bits
        """
        return (self.activeGens() / self.lenght)

    def __str__(self):
        """ Fuction to represent the chromosome like a string

        Return
        ------
        str
          An individual chromosome
        """
        ret = ''
        for bit in self.chromosome:
            if bit:
                ret += '1'
            else:
                ret += '0'
        return ret
