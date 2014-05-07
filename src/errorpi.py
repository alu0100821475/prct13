#! encoding: UTF-8
import time
import timeit
import modulo
import sys
import matplotlib.pyplot as pl

def error(nro_intervalos,nro_test,umbral):
  fallos=0
  for i in range (nro_test):
    s=modulo.aproxpi(nro_intervalos)
    error=abs(s-modulo.pi)
    if error>=umbral:
     fallos=fallos+1
  return ((fallos/nro_test)*100)

x=[]
y=[]
for i in range(10):
 # start=time.time()
#  if (len(sys.argv)==4):
 p1=5
 p2=5
 p3=float(raw_input("Introduzca el valor del umbral: "))
 # else:
  #  print "Usted debe proporcionar tres valores, errorpi.py y tres valores numéricos, ahora se ejecutará por defecto con los valores 5 5 0.1"
   # p1=5
    #p2=5
    #p3=0.1
 s=error(p1,p2,p3)
 print "El porcentaje de error es de: %5.3f" %s
 # finish=time.time()-start
#  print "El tiempo que tarda en realizarse es: %14.13f" %finish
 x=x+[p3]
 y=y+[s]
 # print "Introduzca el nombre del fichero para almacenar los resultados:"
  #nombre_fichero= raw_input();
#  f=open(nombre_fichero, 'a')
  #f.write('El tiempo es:')
  #f.write(str(l[i]) + '\n')
  #f.close()
pl.plot(x,y)
pl.show()
pl.savefig("secons.eps",dpi=72)