###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom = input("Quin és el nom del encaminador?")
ubicacio = input("Quina és la seva ubicació?")
nombre_ports = int(input("Quin és el número de ports?"))
està_encès = bool(input("Està encès? (True/False)"))


# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_inclosos = float(input("Quants GB estan inclosos en el pla?"))
gb_consumits = float(input("Quants GB has consumit?"))
gb_queden = gb_inclosos - gb_consumits
print(f"Et queden {gb_queden} GB.")

gb_consumits_nou = float(input("Quants GB has consumit ara?"))
gb_queden = gb_inclosos - gb_consumits_nou
print(f"Et queden {gb_queden} GB.")