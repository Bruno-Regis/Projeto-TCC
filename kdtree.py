from scipy.spatial import KDTree

# Lista de tuplas contendo coordenadas de pontos
pontos = [(2.0, 3.0), (5.0, 4.0), (9.0, 6.0), (4.0, 7.0), (8.0, 1.0), (7.0, 2.0)]

# Lista de pontos de consulta para encontrar o ponto mais próximo
pontos_consulta = [(3.0, 4.0), (7.0, 5.0), (8.0, 7.0)]

# Criar o KDTree a partir da lista de pontos
kd_tree = KDTree(pontos)

# Encontrar o ponto mais próximo para cada ponto de consulta
for ponto in pontos_consulta:
    distancia, indice = kd_tree.query(ponto)
    ponto_mais_proximo = pontos[indice]
    print(f"Ponto de consulta: {ponto}")
    print(f"Ponto mais próximo: {ponto_mais_proximo}")
    print(f"Distância: {distancia}\n")
    print(f"Distância: {indice}\n")
