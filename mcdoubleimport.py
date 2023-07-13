#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 18:27:16 2023

@author: David Piolo
"""

from mcdouble import MCinteg


def f(x):
    return x**2


n = 10
x0 = 0
x1 = 1
y0 = 0
y1 = 1

area = MCinteg(f, x0, x1, y0, y1, 100)

print(area)

