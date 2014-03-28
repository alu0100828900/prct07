#! /usr/bin/python
#!encoding: UTF-8

import umbralerror
def fichero (nombre, intervalo, umbral):
    intervalo = 10 
    f = open(nombre, "w")
    for i in range (len(t_upla_inter)):
        f.write(str(t_upla_inter[i]) + '\n')
        for j in range (len(t_upla_umbral)):
            sol = umbralerror.error(t_upla_inter[i], intervalo, t_upla_umbral)
            f.write(str(sol) + '\n')

if (__name__ == "__main__"):
    import sys 
    t_upla_inter = (1e1, 1e2, 1e3, 1e4, 1e5, 1e6)
    t_upla_umbral = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)
    if (len(sys.argv) == 1):
        nombre = raw_input("\nIntroduzca el nombre del fichero donde se almacenará la información:\n")
    else:
        nombre = sys.argv[1]
    fichero(nombre, t_upla_inter, t_upla_umbral)