# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:41:26 2017

@author: RXJ5620
"""

import numpy as np
from decimal import Decimal
a = [1,2,3,4,5]
b = [Decimal(x) for x in a]
print(b[1])
print(b)
q1a = np.array([[8.218],[-9.341]])
q1b = np.array([[-1.129],[2.111]])
q2a = np.array([[7.119],[8.215]])
q2b = np.array([[-8.223],[0.878]])
q3a = 7.41
q3b = np.array([[1.671],[-1.012],[-0.318]])
#print(q1a+q1b)
#print(q2a-q2b)
#print(q3a*q3b)
def magnitude(vec):
    return np.sqrt(vec.transpose().dot(vec))
def direction(vec):
    mag = magnitude(vec)
    return vec/mag
q4a = np.array([[-0.221],[7.437]])
q4b = np.array([[8.813],[-1.331],[-6.247]])
'''print(q4a)
print(q4a.shape)
print(q4a.transpose().shape)
print(q4a.transpose().dot(q4a))'''
print(magnitude(q4a))
print(magnitude(q4b))
q4c = np.array([[5.581],[-2.136]])
q4d = np.array([[1.996],[3.108],[-4.554]])
print(direction(q4c))
print(direction(q4d))


