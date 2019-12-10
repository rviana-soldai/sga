#!usr/bin/env python
# -*- coding: utf-8 -*-
"""SevenOnes

This class allow evaluate each bit of the individual chromosome

This file can also be imported as a module and contains the following
methods:
    *evaluateIndividual - return the sum of error if the bits are different of 1

""" 
from sga.SGA import SGA
import math

class SevenOnes(SGA):
	"""
    A class used to verify in the chromosome seven 1

    Methods
    -------
    evaluateIndividual 
        return the sum of error if the bits are different of 1
    """
	def evaluateIndividual(self, individual):
		""""Return the sum of error if the bits are different of 1

		Parameters
		----------
		individual : Individual class
		   Represent an individual of a population

        Return
        ------
        float
           A float with the sum of errors when the bit of chromosome is different to 1
        """
		zeros = 0
		for i in range(self.chromosome_size):
			if not individual.getBit(i):
				zeros += 1
		return abs(zeros - 3) * 0.1