import numpy as np

class Grid: 
    @classmethod
    def cria_grid(cls, pontos, resolucao_espacial):
        cls.pontos = pontos
        cls.resolucao_espacial = resolucao_espacial
        minx, miny, maxx, maxy = cls.pontos.obtem_geolimites() 
        grid_de_x = np.arange(minx - cls.resolucao_espacial,maxx + cls.resolucao_espacial, cls.resolucao_espacial, dtype='float64')
        grid_de_y = np.arange(miny - cls.resolucao_espacial, maxy + cls.resolucao_espacial, cls.resolucao_espacial, dtype='float64')
        xi, yi = np.meshgrid(grid_de_x, grid_de_y)
        return xi, yi

class Pixel:
    def __init__(self, pontos, resolucao_espacial):
        self.pontos = pontos
        self.resolucao_espacial = resolucao_espacial
        self.coordenadas_x_pixels = self.obtem_coordenadas_x_pixels()
        self.coordenadas_y_pixels = self.obtem_coordenadas_y_pixels()
        self.entrada_de_dados_pixels = self.obtem_lista_de_pixels()
        
    @property
    def xi_yi(self):
        xi, yi = Grid.cria_grid(self.pontos, self.resolucao_espacial)
        return xi
    
    def obtem_coordenadas_x_pixels(self):
        xi, yi = Grid.cria_grid(self.pontos, self.resolucao_espacial)
        lista_de_tuplas = []
        for x, y in np.nditer([xi,yi]):
            lista_de_tuplas.append((x,y))
            Latitude = []
            for i in lista_de_tuplas:
                Latitude.append(float(i[0]))
        return Latitude
    def obtem_coordenadas_y_pixels(self):
        xi, yi = Grid.cria_grid(self.pontos, self.resolucao_espacial)
        lista_de_tuplas = []
        for x, y in np.nditer([xi,yi]):
            lista_de_tuplas.append((x,y))
            Longitude = []
            for i in lista_de_tuplas:
                Longitude.append(float(i[1]))
        return Longitude

    def obtem_lista_de_pixels(self):
        saida = list(zip(self.coordenadas_x_pixels,self.coordenadas_y_pixels))
        return saida