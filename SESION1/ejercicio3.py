'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: Programador GABRIELA LAZO PRIEGO
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
horas_extras= float(input("Introduce tus horas extras de trabajo: "))
coste1 = float(input("Introduce lo que cobras por hora extra: "))
paga = horas * coste
paga1 =coste1*horas_extras
total=paga+paga1
print("Tu paga es", total)