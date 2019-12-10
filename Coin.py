#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Coin

This class represent a probabilityof a coin

This file can also be imported as a module and contains the following
methods:
    *toss - return true or false depending if the random value is equal
    or less than the probability variable

"""
import random


class Coin:
    """
    A class used to represent a coin probability

    Attributes
    ----------
    probability : float
       The probability threshold
   

    Methods
    -------
    toss 
        return true or false if the value get in random is equal or less 
        than probability threshold
    """
    def __init__(self, probability):
        """
        Parameters
        ----------
        probability : float
           The probability threshold

        """
        self.probability = probability

    def toss(self):
        """Return true or false if the value get in random is equal or less 
        than probability threshold

        Return
        ------
        bool
         True if random value is less or equal than probability treshold and false 
         in other case
        """
        return random.random() <= self.probability
