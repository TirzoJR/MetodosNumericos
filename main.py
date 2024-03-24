import tkinter as tk

#METODO DE JACOBI PARA RESOLVER SISTEMAS DE ECUACIONES LINEALES
def jacobi (A,b, vectorSolucion,iteracciones):
  iteraccion = 0
  vectorAux = [0] * len(vectorSolucion)
  while iteraccion < iteracciones:
    for i in range (len(A)):
      x = b[i]
      for j in range (len(A):
        if i ! = j:
          x-=A[i][j]* vectorSolucion[j]
          x/= A[i][i]
          vectorAux[i] = x
          print('X da etapa: ', iteraccion, ' Aproximacion: ', vectorSolucion)
          iteraccion += 1
          for p in range (len(vectorAux)):
            vectorSolucion[p]= vectorAux[p]
   print('X da etapa: ', iteraccion, ' Aproximacion: ', vectorSolucion)

#METODO DE EULER PARA RESOLVER ECUACIONES DIFERENCIALES ORDINARIAS
def euler(funcion,t0,y0,h,n):
  t=t0
  y=y0
  print(f't = {t}, y = {y}')
  for i in range (1, n+1):
        y = y + h * funcion(t, y)
        t = t0 + i * h
        print(f't = {t}, y = {y}')
#EJEMPLO DE FUNCION PARA LA FUNCION EDO
def funcion_euler(t, y):
  return y

