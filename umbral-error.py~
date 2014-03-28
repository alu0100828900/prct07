#! /usr/bin/python
#!encoding: UTF-8

import moduloPI

def error (intervalo, veces , umbral):
    p = 0.0
    x = 0.0
    ref = moduloPI.PI
    for j in range (veces):
        pi = moduloPI.aproximacion(intervalo)
        if (abs(pi - ref) > umbral):
           x= x + 1
    return (x/veces) * 100

if __name__=="__main__":
  import sys
  
  if (len(sys.argv) == 4):
    intervalo = int (sys.argv[1])
    veces = int (sys.argv[2])
    umbral = float(sys.argv[3])
  else:
    print 'Es necesario adjuntar en la línea de comando un entero que determine el número de intervalos deseados y otro para el número de veces:'
    print 'nombre.py intervalo veces'
    intervalo = 10
    veces = 10
    umbral=0.000001

  devolver = error(intervalo, veces, umbral)
  print "\nEl porcentaje de errores es %f" %devolver

  