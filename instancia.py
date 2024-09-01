#### TESTE DE ATRIBUIÇÃO DE OBJETO ####
from interp import Interpolador
interpolar = Interpolador(caminho= "C:/Users/User/Desktop/TCC/TCC/random_points.shp", coluna_z= 'Elevation', algoritmo= "IDW", resolucao_espacial= 100)
dados = interpolar.interpolar()
print(f"{dados}")

interpolar.plotagem_matplotlib(dados = dados, color="PRGn")

