nombres=["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

def hacer_grandioso(magos):
    magos2=[]
    for i in magos[0]:
        magos2.append(f"El gran {i}")
    magos[0].clear
    magos[0]= magos2
    return magos

def imprimir_nombres(names):
    for i in names:
        print(i) 
    return 

def clasificacion(a,b):
    print(" ---- Lista sin modificar ----")
    print(a)
    print("---- Clasificacion ----")
    clasif=["Magos", "Cientificos", "Otros"]
    for i,nombre in enumerate(b):
        print(f"---- {clasif[i]} ------")
        for j in nombre:
            print(j)



ngrupos=3
grupos=[[] for _ in range(ngrupos)]

for i in nombres:
    if ("Harry" in i) or ("David" in i) or ("Teller" in i): grupos[0].append(i)
    elif ("Newton" in i) or ("Hawking" in i) or ("Einstein" in i): grupos[1].append(i)
    else: grupos[2].append(i)


original= grupos[:]

hacer_grandioso(grupos)
imprimir_nombres(nombres)
clasificacion(original, grupos)




""" 

# Ejemplo de lista original
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cantidad de grupos que se desean crear
n_grupos = 3

# Crear una lista de listas vacía, donde se almacenarán los grupos
grupos = [[] for _ in range(n_grupos)]

# Separar los elementos en grupos
for i, elemento in enumerate(lista):
    grupos[i % n_grupos].append(elemento)

# Imprimir los grupos resultantes
print(grupos)
"""