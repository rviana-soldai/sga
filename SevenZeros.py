#!usr/bin/env python
# -*- coding: utf-8 -*-
"""SevenZeros

This class allow to verify that the first 7 chromosome are zero

This file can also be imported as a module and contains the following
methods:
    *evaluateIndividual - return the sum of error if the bits are different of 0

"""
from sga.SGA import SGA
import math

class SevenZeros(SGA):
	"""
    A class used to to verify that the first 7 chromosome are zero

    Methods
    -------
    evaluateIndividual 
        return the sum of error if the bits are different of 0
    """
	def evaluateIndividual(self, individual):
		""""Return the sum of error if the bits are different of 0

		Parameters
		----------
		individual : Individual class
		   Represent an individual of a population

        Return
        ------
        float
           A float with the sum of errors when the bit of chromosome is different to 0
        """
		error = 0
		for i in range(7):
			if individual.getBit(i):
				error += 0.14
		return error