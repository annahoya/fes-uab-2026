###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}!")

saludar_a("Anna")  
saludar_a("Alex", "Bon dia")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    return numero % 2 == 0

print(es_parell(6))  
print(es_parell(3))  

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)

print(mitjana([1, 2, 3, 4, 5]))  

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_tot(2,4))
print(sumar_tot(7,2,1,5,6))  
print(sumar_tot(4,6,3,1,2,8,6,5,9,7))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
    for i in range(1, limit + 1):
        print(f"{numero} x {i} = {numero * i}")

taula_multiplicar(5)
taula_multiplicar(3, 5)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def demostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

demostrar_perfil(Nom="Anna", Edat=19, Grau="Enginyeria Telecomunicacions")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
    resultat = 1
    comptador = 1
    while comptador <= n:
        resultat *= comptador
        comptador += 1
    return resultat

def maxim(numeros):
    valor_max = numeros[0]
    for numero in numeros:
        if numero > valor_max:
            valor_max = numero
    return valor_max

print(f"El factorial de 7 és {factorial(7)}")
print(f"El màxim de [3, 7, 2, 9, 5] és {maxim([3, 7, 2, 9, 5])}")

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    vocals = "aeiouAEIOUàèéíòóúÀÈÍÒÚïüÏÜ"
    comptador = 0
    for char in text:
        if char in vocals:
            comptador += 1
    return comptador

print(f"El nombre de vocals en 'Hola, com estàs?' és {comptar_vocals('Hola, com estàs?')}")

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.