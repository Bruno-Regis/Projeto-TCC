
import geopandas as gpd
import pandas as pd
import numpy as np
import math
from scipy.spatial import KDTree                               # BIBLIOTECAS IMPORTADAS
import matplotlib.pyplot as plt
from osgeo import gdal
from shapely.geometry import Point, Polygon
import tempfile

# DEFININDO FUNÇÕES

def path_shapefile(path: str) -> gpd.geodataframe:
    """Obtém um geodataframe a partir de uma """
    return gpd.read_file(path)

def obtem_coordenadas(pontos: gpd.GeoDataFrame, coluna_interp: str = "") ->list:
    if type(pontos["geometry"][0]) == Point:
        coordenadas_x = pontos['geometry'].x
        coordenadas_x = list(coordenadas_x)
        coordenadas_y = pontos['geometry'].y
        coordenadas_y = list(coordenadas_y)
        if coluna_interp != "":
            valores_z = pontos[coluna_interp]
        else:
            valores_z = pontos['geometry'].z
        valores_z = list(valores_z)
    else:    
        gdf_exploded = pontos.explode(index_parts=False)
        gdf_exploded.reset_index(drop=True, inplace=True)
        coordenadas_x = gdf_exploded['geometry'].x
        coordenadas_x = list(coordenadas_x)
        coordenadas_y = gdf_exploded['geometry'].y
        coordenadas_y = list(coordenadas_y)
        if coluna_interp != "":
            valores_z = gdf_exploded[coluna_interp]
        else:
            valores_z = pontos['geometry'].z
        valores_z = list(valores_z)
    return coordenadas_x, coordenadas_y, valores_z

def obtem_geolimites(pontos: gpd.GeoDataFrame)-> np.float64:
    pontos_cotados = pontos.total_bounds
    minx, miny, maxx, maxy = pontos_cotados
    return minx, miny, maxx, maxy

def cria_grid(minx:np.float64, miny:np.float64, maxx:np.float64, maxy:np.float64, res: float) -> np.ndarray:
    grid_de_x = np.arange(minx - res,maxx + res, res, dtype='float64')
    grid_de_y = np.arange(miny - res, maxy + res, res, dtype='float64')
    xi, yi = np.meshgrid(grid_de_x, grid_de_y)
    return xi, yi

def obtem_lat_long(xi:np.ndarray, yi:np.ndarray)-> list:
    lista_de_tuplas = []
    for x, y in np.nditer([xi,yi]):
        lista_de_tuplas.append((x,y))
    Latitude = []
    Longitude = []
    for i in lista_de_tuplas:
        Latitude.append(float(i[0]))
        Longitude.append(float(i[1]))
    return Latitude, Longitude

def lista_pontos_saida(xi:np.ndarray, yi:np.ndarray)-> list:
    lista_de_tuplas = []
    for x, y in np.nditer([xi,yi]):
        lista_de_tuplas.append((x,y))

    Latitude = []
    Longitude = []
    for i in lista_de_tuplas:
        Latitude.append(float(i[0]))
        Longitude.append(float(i[1]))
    saida = list(zip(Latitude,Longitude))
    return saida

def lista_pontos_entrada(coordenadas_x:list, coordenadas_y:list, valores_z:list)->list:
    entrada = list(zip(coordenadas_x, coordenadas_y, valores_z))
    return entrada

def distancia_euclidiana(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def distancia_eliptica(x1: float, y1: float, x2: float, y2: float, a: float, b: float) -> float:
    return math.sqrt(((x2 - x1) / a) ** 2 + ((y2 - y1) / b) ** 2)

def remodelando_interp(lista_interpolada: list, shape: tuple) -> np.ndarray:
    interpolado = np.array(lista_interpolada)
    shape = shape
    interpolado = interpolado.reshape(shape[0],shape[1])
    return interpolado

def viz_mais_prox(pontos_entrada:list, pontos_saida:list) -> list:
    lista_z = []
    
    for ponto1 in pontos_saida:
        x1, y1 = ponto1
        menor_distancia = float('inf')
        z_mais_proximo = None
        for ponto2 in pontos_entrada:
            x2, y2, z = ponto2
            distancia = distancia_euclidiana(x1, y1, x2, y2)
            if distancia < menor_distancia:
                menor_distancia = distancia
                z_mais_proximo = z
        lista_z.append(z_mais_proximo)
    return lista_z
    # pontos_entrada_xy = [(x, y) for x, y, z in pontos_entrada]
    # kd_tree = KDTree(pontos_entrada_xy)
    

def lista_pontos_entrada_kd_tree(coordenadas_x:list, coordenadas_y:list, valores_z:list)->list:
    entrada = list(zip(coordenadas_x, coordenadas_y))
    valores_z = list(valores_z)
    return entrada, valores_z
def viz_mais_prox2(pontos_entrada:list, pontos_saida:list, valores_z) -> list:
    lista_z = []
    kd_tree = KDTree(pontos_entrada)
    for ponto in pontos_saida:
        distancia, indice = kd_tree.query(ponto)
        lista_z.append(valores_z[indice])
    return lista_z

def media_dos_pontos(pontos_entrada:list, pontos_saida:list, raioa:float, raiob:float) -> list:
    medias_z = []
    for ponto1 in pontos_saida:
        x1, y1 = ponto1
        valores_z = []
        for ponto2 in pontos_entrada:
            x2, y2, z = ponto2
            d = distancia_eliptica(x1, y1, x2, y2, raioa, raiob)
            if d <= 1:
                valores_z.append(z)
        media_z = np.mean(valores_z) if valores_z else 0
        medias_z.append(media_z)
    return medias_z

def idw(pontos_entrada: list, pontos_saida: list, potencia: float, raioa:float, raiob: float) ->  np.ndarray:
    idw_z = []
    for ponto1 in pontos_saida:
        valoresz = []
        dists = []
        x1, y1 = ponto1
        for ponto2 in pontos_entrada:
            x2, y2, z = ponto2
            d = distancia_eliptica(x1, y1, x2, y2, raioa, raiob)
            if d <= 1:  # Verifica se está dentro da elipse
                distancia_entre_os_pontos = distancia_euclidiana(x1, y1, x2, y2)
                valoresz.append(z)
                dists.append(distancia_entre_os_pontos)
        valoresz = np.array(valoresz)
        dists = np.array(dists)
        calculo = np.sum(valoresz / dists**potencia) / np.sum(1 / dists**potencia)
        if np.isnan(calculo):
            calculo = 0  # Se todos os valores z forem iguais, retorna 0 para evitar divisão por zero
        idw_z.append(calculo)
    return idw_z

def plotagem_matplot(grid_de_valores_interpolados: np.ndarray, minx:np.float64,maxx:np.float64,miny:np.float64,maxy:np.float64, tipo_interp:str):
    fig,ax = plt.subplots(figsize = (8,10))
    cax = ax.imshow(grid_de_valores_interpolados, extent=(minx-5, maxx+5, miny-5, maxy+5), origin="lower", cmap="YlOrRd")
    #pontos.plot(color="blue", ax=ax, marker="+", label="Amostras")
    cbar=plt.colorbar(cax, fraction = 0.08)
    #ax.legend()
    if tipo_interp == "vizinhos mais proximos":
        plt.title("Interpolação Vizinho Mais Próximo")
    elif tipo_interp == "media":
        plt.title("Interpolação Média dos Valores Próximos")
    elif tipo_interp == "idw":
        plt.title("Interpolação IDW")
    plt.show()

def transforma_TIFF(dfn, name, xres, yres):
    temp_xyz_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xyz")
    print(temp_xyz_file.name)
    dfn.to_csv(temp_xyz_file.name, index = False, header = None, sep = " ")
    gdal.Translate(name+".tif", temp_xyz_file.name, outputSRS = "EPSG:31983", 
                          xRes = xres, yRes = yres)

# INICIANDO SCRIPT
#***** Abrindo dados e atribuindo a variável pontos *****#
print("iniciando script...")
path = 'C:/Users/User/Desktop/TCC/TCC/random_points.shp'
pontos = path_shapefile(path)

#***** Obtendo uma series com os valores das coordenadas x, y e valores z dos pontos *****#
coordenada_x, coordenada_y, valores_z = obtem_coordenadas(pontos, "Elevation")

#***** Obtendo limites geográficos do shapefile *****#
minx, miny, maxx, maxy = obtem_geolimites(pontos)
print(f"mínima coordenada de x: {minx}\nmáxima coordenada de x: {maxx}\nmínima coordenada de y: {miny}\nmáxima coordenada de y: {maxy}")

#***** Criando grid de coordenadas *****#
xi, yi = cria_grid(minx, miny, maxx, maxy, 100)

#***** Criando lista de tuplas de coordenadas de entrada *****#
entrada = lista_pontos_entrada(coordenada_x, coordenada_y, valores_z)

#***** Criando lista de tuplas de coordenadas de saída *****#
saida = lista_pontos_saida(xi, yi)

#***** Interoplando valores *****#
print("Calculando...")
#interpolacao = viz_mais_prox(entrada, saida)
#interpolacao = media_dos_pontos(entrada, saida, 1500, 1000)
interpolacao = idw(entrada, saida,2, 1500, 1000)
print("terminei..")

#***** Obtendo array dos valores interpolados com formato de grid *****#
grid_de_valores_interpolados = remodelando_interp(interpolacao, xi.shape) 

#***** Plotagem utilizando matplotlib *****#
plotagem_matplot(grid_de_valores_interpolados, minx=minx, maxx=maxx, miny=miny, maxy=maxy, tipo_interp= "idw")

#***** Salvando dados em formato de tiff *****#
print("estou fazendo o dfn")
Latitude, Longitude = obtem_lat_long(xi, yi)

# dfn = { 'X': Latitude,
#        'Y': Longitude, 
#        'Z': interpolacao
#       }

# dfn = pd.DataFrame(dfn)
# transforma_TIFF(dfn, "C:/Users/User/Desktop/UNIFAL/idw2_5m", 100, 100)
# print("Fim.")
#amanhã testar gdal.grid..
# dem = gdal.Grid("idw.tif", "pontos_aleatorios.shp", zfield= "Elevation", algorithm="invdistpower", outputBounds=[minx, miny, maxx, maxy], width= 25, height=25)
#classe: arquivo de saida, arquivo de entrada, field, tipo de interpolador, resolucao, se for utilizar a elipse setar a elipse)
