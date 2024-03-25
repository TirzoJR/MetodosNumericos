import tkinter as tk

#METODO DE INTERPOLACION DE HERMITE
#FALTA AQUI ------------------------------



#-------------------------------------------------------------------------


#METODO DE JACOBI PARA RESOLVER SISTEMAS DE ECUACIONES LINEALES
def jacobi (A,b, vectorSolucion,iteracciones):
  iteraccion = 0
  vectorAux = [0] * len(vectorSolucion)
  while iteraccion < iteracciones:
    for i in range (len(A)):
      x = b[i]
      for j in range (len(A)):
        if i != j:
          x-=A[i][j]* vectorSolucion[j]
          x/= A[i][i]
          vectorAux[i] = x
          print('X da etapa: ', iteraccion, ' Aproximacion: ', vectorSolucion)
          iteraccion += 1
          for p in range (len(vectorAux)):
            vectorSolucion[p]= vectorAux[p]
   print('X da etapa: ', iteraccion, ' Aproximacion: ', vectorSolucion)

#-------------------------------------------------------------------------


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


#-------------------------------------------------------------------------


#ALGORITMO DE LA REGLA DE SIMPSON COMPUESTA
def simpson_compuesta(funcion, a, b, n):
  h = (b - a) / n
  suma = funcion(a) + funcion(b)
  for i in range (1 , n):
    if i % 2 == 0:
      suma += 2 * funcion(a + i * h)
    else:
      suma += 4 * funcion(a + i * h)
      return(h/3) * suma


#-------------------------------------------------------------------------
      
# Función para llamar al método de Jacobi cuando se hace clic en el botón
def llamar_jacobi():
    jacobi([[2, 1], [3, 4]], [1, -1], [0, 0], 3)
    jacobi([[10, 2, 1], [1, 5, 1], [2, 3, 10]], [7, -8, 6], [0, 0, 0], 38)

# Función para llamar al método de Euler cuando se hace clic en el botón
def llamar_euler():
    euler(funcion_euler, 0, 1, 0.1, 10)

#FUNCION PARA LLAMAR AL ALGORITMO DE LA REGLA DE SIMPSON COMPUESTA CUANDO SE HACE CLIC EN EL BOTON
def llamar_simpson_compuesta():
    funcion = lambda x: x**2  # Ejemplo de función f(x) = x^2
    a = 0
    b = 1
    n = 10  # Número de subintervalos
    resultado = simpson_compuesta(funcion, a, b, n)
    print("Resultado de la regla de Simpson compuesta:", resultado)

#-------------------------------------------------------------------------

#CREAMOS LA VENTANA PRINCIPAL
root = tk.Tk()
root.title("EJECUTAR LOS PROGRAMAS DE METODOS NUMERICOS SIS ")
root.geometry("400x400")

#-------------------------------------------------------------------------

#CREAMOS UN LABEL PARA MOSTRAR EL TITULO DE LA VENTANA PRINCIPAL
titulo = tk.Label (root,text="¿QUE PROGRAMA DESEAS EJECUTAR?")
titulo.pack(pady=10)

#VAMOS A CREAR LOS BOTONES PARA LOS METODOS DE JACOBI,EULER,SIMPSON COMPUESTA, INTERPOLACION DE HERMITE
boton_jacobi = tk.Button(root,text="RESOLVER CON JACOBI", command=llamar_jacobi)
boton_jacobi.pack(pady=5)

boton_euler = tk.Button(root,text="RESOLVER CON EULER", command=llamar_euler)
boton_euler.pack(pady=5)

boton_simpson_compuesta = tk.Button(root,text="RESOLVER CON JACOBI", command=llamar_simpson_compuesta)
boton_simpson_compuesta.pack(pady=5)

"EJECUTAR EL BUCLE DE CADA UNO DE LOS EVENTOS
root.mainloop()









