from GRAFO import Grafo
from random import randint

grafo_star_wars = Grafo()

grafo_star_wars.insert_vertice('Luke Skywalker')
grafo_star_wars.insert_vertice('Darth Vader')
grafo_star_wars.insert_vertice('Kylo Ren')
grafo_star_wars.insert_vertice('Leia')
grafo_star_wars.insert_vertice('Boba Fett')
grafo_star_wars.insert_vertice('C-3PO')
grafo_star_wars.insert_vertice('Rey')
grafo_star_wars.insert_vertice('Chewbacca')
grafo_star_wars.insert_vertice('Han Solo')
grafo_star_wars.insert_vertice('R2-D2')
grafo_star_wars.insert_vertice('BB-8')
grafo_star_wars.insert_vertice('Yoda')

grafo_star_wars.insert_arist('Luke Skywalker', 'Darth Vader', randint(1, 7))
grafo_star_wars.insert_arist('Luke Skywalker', 'Kylo Ren', randint(1, 7))
grafo_star_wars.insert_arist('Luke Skywalker', 'Leia', randint(1, 7))

arbol_expansion_minimo = grafo_star_wars.kruskal()
print('Árbol de Expansión Mínimo:')
for arista in arbol_expansion_minimo:
    print(arista)

contiene_yoda = False
for arista in arbol_expansion_minimo:
    if 'Yoda' in arista or 'Yoda' in arista[::-1]:
        contiene_yoda = True
        break

if contiene_yoda:
    print('El árbol de expansión mínimo contiene a Yoda.')
else:
    print('El árbol de expansión mínimo no contiene a Yoda.')

max_peso, personajes_max_episodios = grafo_star_wars.max_episodios_compartidos()

if max_peso > 0:
    print(f'El número máximo de episodios compartidos es {max_peso}, y los personajes son:')
    for i in range(0, len(personajes_max_episodios), 2):
        personaje1 = personajes_max_episodios[i]
        personaje2 = personajes_max_episodios[i + 1]
        print(f'{personaje1} y {personaje2}')
else:
    print('No se encontraron personajes que compartan episodios.')

primero = 'Yoda'
ultimo = 'Rey'
principio = grafo_star_wars.search_vertice(primero)
final = grafo_star_wars.search_vertice(ultimo)
camino_mas_corto = None
if principio is not None and final is not None:
    if grafo_star_wars.has_path(primero, ultimo):
        camino_mas_corto = grafo_star_wars.dijkstra(primero, ultimo)
        fin = ultimo
        while len(camino_mas_corto) > 0:
            value = camino_mas_corto.pop(0)
            if fin == value[0]:
                print(value[0], value[1])
                fin = value[2]
