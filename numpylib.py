#!/usr/bin/python
# -*- coding: UTF-8 -*-

from numpy import *
import matplotlib.pyplot as plt
a = [1,2,3,4]
a = array(a)
b = [2,3,4,5]
b = array(b)
print(a ** b)
print(a[:2]+a[-2:])
print(a.shape)
a.shape = 2,2
print(a)
print(a+a)
print(a*a)

a = linspace(0,2*pi,21)

print(a)
b = sin(a)
print(b)
plot(a,b)