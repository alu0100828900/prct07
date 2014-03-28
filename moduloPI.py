#!/usr/bin/python
#!encoding:UTF-8
PI = 3.1415926535897931159979634685441852
def aproximacion (nn):
  n =int(nn)
  sumatorio = 0.0
  for i in range (1, n+1):
    xi = (i-0.5)/float(n)
    fxi = 4/(1 + (xi**2))
    sumatorio += fxi
  c = sumatorio/float(n)
  return c
