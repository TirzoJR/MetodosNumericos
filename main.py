import tkinter as tk
import numpy as np
import sympy as sympy
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#-------------------------------------------------------------------------
#Metodo de Hermite

def clear_screen():
    import os
    if os.name == 'posi x ':
        _ = os.system('clear')
    else:
        _ = os.system ('cls')

def calcular_polinomio_interpolador_hermite(z,fz,difs):
    polinomio = ""
    n = len(z)
    for k in range (n):
        if k==0:
            polinomio += str(round(fz[k],6))
        else:
            polinomio += " + "
            for i in range(k):
                polinomio += f"(x - {round(z[i],6})*"
            polinomio += f"({round(difs[k-1][0],6)})"
    return polinomio
def simplificar_polinomio(polinomio):
    x = sympy.symbols('x')
    polinomio_simplificado = sympy.symplify(polinomio):
    polinomio_simplificado_rounded = polinomio_simplificado.evalf(n=6)

return polinomio_simplificado_rounded

def main ():
    n= int (input("ingresa  la cantidad de datos :"))
    x=[]
    fx=[]
    dfx=[]
    
    for i in range (n):
        x.append(float(input(f"Ingresa el valor de x{i}:")))
        fx.append(float(input(f"Ingresa el valor de f(x{i}):")))
        dfx.append(float(input(f"Ingrese el valor de f'(x{i}): ")))
    z=[]
    fz=[]
    dfz=[]
    
    for i in range (n):
        z.append(x[i])
        z.append(x[i])
        fz.append(fx[i])
        fz.append(fx[i])
        dfz.append(dfx[i])
        dfz.append(dfx[i])
  dif =[]
  m=2*n
  difs =[]
    for i in range(m-1):
        dif = []
        difs.append(dif)
    for i in range(m-1):
        for j in range(m-1-i):
            if i == 0:
                if fz[j+1]-fz[j] == 0:
                    difs[i].append(dfz[j])
                else:
                    difs[i].append((fz[j+1]-fz[j])/(z[j+1]-z[j]))
            else:
                difs[i].append((difs[i-1][j+1]-difs[i-1][j])/(z[j+i+1]-z[j]))
    max_legth = max (len(z),len(fz))
    for i in range(m - 1):
        difs[i].extend(["-"] * (max_length - len(difs[i])))

    # Crear la tabla con valores redondeados a 6 decimales
    header = ["z", "fz"]
    for i in range(m - 1):
        header.append(f"dif{i+1}")

    table = [header]
    for row in zip(z, fz, *difs):
        rounded_row = [round(cell, 6) if isinstance(cell, float) else cell for cell in row]
        table.append(rounded_row)

    # Imprimir la tabla con columnas alineadas
    column_lengths = [max(len(str(cell)) for cell in column) for column in zip(*table)]
    for row in table:
        formatted_row = [str(cell).ljust(column_length) for cell, column_length in zip(row, column_lengths)]
        print("  ".join(formatted_row))

    # Obtener el polinomio interpolador de Hermite
    polinomio = calcular_polinomio_interpolador_hermite(z, fz, difs)

    # Imprimir el polinomio interpolador
    print("Polinomio interpolador de Hermite:")
    print(polinomio)

    # Simplificar el polinomio interpolador
    polinomio_simplificado = simplificar_polinomio(polinomio)
    print("Polinomio interpolador de Hermite (simplificado a mínima expresión con 6 decimales):")
    print(polinomio_simplificado)

   
            
    
    
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

#HERMITE INTERPOLACION
def llamar_hermite_interpolation():
    x = np.array([0, 1, 2])
    y = np.array([1, 2, 3])
    y_prime = np.array([2, 3, 4])

    x_interp = np.linspace(0, 2, 100)
    y_interp = hermite_interpolation(x, y, y_prime, x_interp)

    plt.plot(x, y, 'ro', label='Known points')
    plt.plot(x_interp, y_interp, label='Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Hermite Interpolation')
    plt.legend()
    plt.show()

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
boton_hermite_interpolation = tk.Button(root, text="Interpolación de Hermite", main)
boton_hermite_interpolation.pack(pady=5)

boton_jacobi = tk.Button(root,text="RESOLVER CON JACOBI", command=llamar_jacobi)
boton_jacobi.pack(pady=5)

boton_euler = tk.Button(root,text="RESOLVER CON EULER", command=llamar_euler)
boton_euler.pack(pady=5)

boton_simpson_compuesta = tk.Button(root,text="RESOLVER CON JACOBI", command=llamar_simpson_compuesta)
boton_simpson_compuesta.pack(pady=5)

#EJECUTAR EL BUCLE DE CADA UNO DE LOS EVENTOS
root.mainloop()









