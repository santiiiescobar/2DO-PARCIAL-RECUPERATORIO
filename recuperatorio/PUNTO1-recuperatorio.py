from ArbolBinario import BinaryTree

pokemon_data = [
    {'name': 'Pikachu', 'number': 25, 'type': ['Electric']},
    {'name': 'Bulbasaur', 'number': 1, 'type': ['Grass', 'Poison']},
    {'name': 'Charizard', 'number': 6, 'type': ['Fire', 'Flier']},
    {'name': 'Jolteon', 'number': 135, 'type': ['Electric']},
    {'name': 'Lycanroc', 'number': 745, 'type': ['Stone']},
    {'name': 'Tyrantrum', 'number': 697, 'type': ['Stone', 'Dragon']},
    {'name': 'Steelix', 'number': 208, 'type': ['steel']}
]

name_tree = BinaryTree()
number_tree = BinaryTree()
type_tree = BinaryTree()

for pokemon in pokemon_data:
    name_tree.insert_node(pokemon['name'], {'number': pokemon['number'],'type': pokemon['type']})
    number_tree.insert_node(pokemon['name'], {'number': pokemon['number'],'type': pokemon['type']})
    type_tree.insert_node(pokemon['name'], {'number': pokemon['number'],'type': pokemon['type']})

number = 25
number_tree.inorden(number)
name = 'Bul'
name_tree.search_by_coincidence(name)
type = 'Electric'
type_tree.inorden(type)

def listar_nombres_por_tipo(self, root, tipo):
    if root is not None:
        if tipo in root.value['type']:
            print(root.value['name'])
        self.listar_nombres_por_tipo(root.left, tipo)
        self.listar_nombres_por_tipo(root.right, tipo)

tipos_a_buscar = ["water","Fire", "plant","Electric"]
print("Nombres de Pokémon de tipo agua:")
type_tree.listar_nombres_por_tipo(type_tree.root, tipos_a_buscar)

print("Listado de Pokémon en orden ascendente por numero:")
number_tree.inorden()
print("\nListado de Pokémon en orden ascendente por nombre:")
name_tree.inorden()
print("Listado de Pokémon por nivel nombre")
name_tree.by_level()

print("Datos de Pokémon Jolteon:")
name_tree.search_pokemon_by_name('Jolteon')
print("\nDatos de Pokémon Lycanroc:")
name_tree.search_pokemon_by_name('Lycanroc')
print("\nDatos de Pokémon Tyrantrum:")
name_tree.search_pokemon_by_name('Tyrantrum')

print(f"Total de Pokémon de tipo 'Eléctrico': {type_tree.contar('Eléctrico')}")
print(f"Total de Pokémon de tipo 'Acero': {type_tree.contar('Acero')}")