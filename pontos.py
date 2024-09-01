import geopandas as gpd
from shapely.geometry import Point, Polygon

class Pontos:
    def __init__(self, caminho, coluna_z = ""):
        self.caminho = caminho
        self.coluna_z = coluna_z
        self.pontos = self.obtem_shapefile()
        self.coordenadas_x = self.obtem_coordenadas_x()
        self.coordenadas_y = self.obtem_coordenadas_y()
        self.valores_z = self.obtem_valores_z()
        self.entrada_de_dados_pontos = self.obtem_lista_de_pontos()
    
    def obtem_shapefile(self):
        return gpd.read_file(self.caminho)

    def obtem_coordenadas_x(self):
        if type(self.pontos["geometry"][0]) == Point:
            coordenadas_x = self.pontos['geometry'].x
            coordenadas_x = list(coordenadas_x)
        else:
            gdf_exploded = self.pontos.explode(index_parts=False)
            gdf_exploded.reset_index(drop=True, inplace=True)
            coordenadas_x = gdf_exploded['geometry'].x
            coordenadas_x = list(coordenadas_x)
        return coordenadas_x
    
    def obtem_coordenadas_y(self):
        if type(self.pontos["geometry"][0]) == Point:
            coordenadas_y = self.pontos['geometry'].y
            coordenadas_y = list(coordenadas_y)
        else:
            gdf_exploded = self.pontos.explode(index_parts=False)
            gdf_exploded.reset_index(drop=True, inplace=True)
            coordenadas_y = gdf_exploded['geometry'].y
            coordenadas_y = list(coordenadas_y)
        return coordenadas_y
    
    def obtem_valores_z(self):
        if type(self.pontos["geometry"][0]) == Point:
            if self.coluna_z != "":
                valores_z = self.pontos[self.coluna_z]
            else:
                valores_z = self.pontos['geometry'].z
            valores_z = list(valores_z)
        else:
            gdf_exploded = self.pontos.explode(index_parts=False)
            gdf_exploded.reset_index(drop=True, inplace=True)
            if self.coluna_z != "":
                valores_z = gdf_exploded[self.coluna_z]
            else:
                valores_z = self.pontos['geometry'].z
            valores_z = list(valores_z)
        return valores_z
    
    def obtem_geolimites(self):
        pontos_cotados = self.pontos.total_bounds
        minx, miny, maxx, maxy = pontos_cotados
        return minx, miny, maxx, maxy
        
    def obtem_lista_de_pontos(self):
        entrada = list(zip(self.coordenadas_x, self.coordenadas_y, self.valores_z))
        return entrada
