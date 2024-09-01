import numpy as np
from osgeo import gdal
import pandas as pd
import tempfile
import matplotlib.pyplot as plt
from pontos import Pontos
from estrutura import Pixel, Grid
from operacoes import Operacoes
# o qeue vamos ter no interpolador final? path entrada, path saída, coluna a ser interpolada, tipo de interpolador, resolucao...
class Interpolador:
    def __init__(self, caminho, coluna_z, algoritmo, resolucao_espacial, raio_horizontal = 1500, raio_vertical = 1000, potencia = 1):   
        self.caminho = caminho
        self.coluna_z = coluna_z
        self.algoritmo = algoritmo
        self.resolucao_espacial = resolucao_espacial
        self.raio_horizontal = raio_horizontal
        self.raio_vertical = raio_vertical
        self.potencia = potencia
        self.pontos = Pontos(self.caminho,self.coluna_z)
        self.pixels = Pixel(self.pontos, self.resolucao_espacial)
        self.xi = self.pixels.xi_yi
        self.latitude_pixels = self.pixels.obtem_coordenadas_x_pixels()
        self.longitude_pixels = self.pixels.obtem_coordenadas_y_pixels()
        self.valores_interpolados = []

    def interpolar(self):
        print("Iniciando interpolação")
        match self.algoritmo:
            case "Vizinhos":
                dados_pontos = self.pontos.entrada_de_dados_pontos
                dados_pixels = self.pixels.entrada_de_dados_pixels                
                vizinhos = VizinhosMaisProximos(dados_pontos, dados_pixels)
                valores_interpolados = vizinhos.calculo()
 
            case "Media":
                dados_pontos = self.pontos.entrada_de_dados_pontos
                dados_pixels = self.pixels.entrada_de_dados_pixels
                media_dos_pontos = MediaDosPontos(dados_pontos, dados_pixels, self.raio_horizontal, self.raio_vertical)
                valores_interpolados = media_dos_pontos.calculo()

            case "IDW":
                dados_pontos = self.pontos.entrada_de_dados_pontos
                dados_pixels = self.pixels.entrada_de_dados_pixels
                idw = InversoDaDistancia(dados_pontos,dados_pixels, self.raio_horizontal, self.raio_vertical, self.potencia)
                valores_interpolados = idw.calculo()
        self.valores_interpolados = valores_interpolados
        return valores_interpolados
    
    @classmethod
    def remodelando_valores_interpolados(cls, valores_interpolados, xi):
        print("Iniciando remodelação - criando objetos")
        print("obtendo shape..")
        cls.xi = xi
        cls.valores_interpolados = valores_interpolados
        interpolado = np.array(valores_interpolados)
        shape = cls.xi.shape
        print("reshape..")
        grid_de_valores_interpolados = interpolado.reshape(shape[0],shape[1])
        return grid_de_valores_interpolados
    
    def plotagem_matplotlib(self, dados, color):    
        self.color = color
        self.dados = dados   
        grid_de_valores_interpolados = Interpolador.remodelando_valores_interpolados(self.dados,self.xi)
        minx, miny, maxx, maxy = self.pontos.obtem_geolimites()
        print("Iniciando plot")
        fig,ax = plt.subplots(figsize = (8,10))
        cax = ax.imshow(grid_de_valores_interpolados, extent=(minx-5, maxx+5, miny-5, maxy+5), origin="lower", cmap=self.color)
        #pontos.plot(color="blue", ax=ax, marker="+", label="Amostras")
        cbar=plt.colorbar(cax, fraction = 0.08)
        #ax.legend()
        if self.algoritmo== "Vizinhos":
            plt.title("Interpolação Vizinho Mais Próximo")
        elif self.algoritmo == "Media":
            plt.title("Interpolação Média dos Valores Próximos")
        elif self.algoritmo == "IDW":
            plt.title("Interpolação IDW")
        return plt.show()

    def gera_data_frame_de_dados(self):
        
        dfn = { 
            'X': self.latitude_pixels,
            'Y': self.longitude_pixels, 
            'Z': self.valores_interpolados
              }
        dfn = pd.DataFrame(dfn)
        return dfn
    def transforma_TIFF(self,dfn, name):
        dfn = Interpolador.gera_data_frame_de_dados()
        temp_xyz_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xyz")
        dfn.to_csv(temp_xyz_file.name, index = False, header = None, sep = " ")
        gdal.Translate(name+".tif", temp_xyz_file, outputSRS = "EPSG:31983", 
                            xRes = self.resolucao_espacial, yRes = self.resolucao_espacial)
        
class VizinhosMaisProximos():
    def __init__(self, pontos, pixels):
        self.pontos = pontos
        self.pixels = pixels
    def calculo(self):
        lista_z = []
        for ponto1 in self.pixels:
            x1, y1 = ponto1
            menor_distancia = float('inf')
            z_mais_proximo = None
            for ponto2 in self.pontos:
                x2, y2, z = ponto2
                distancia = Operacoes.distancia_euclidiana(x1, y1, x2, y2)
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    z_mais_proximo = z
            lista_z.append(z_mais_proximo)
        return lista_z

class MediaDosPontos:
    def __init__(self,pontos, pixels,raio_horizontal = 1500, raio_vertical = 1000 ):    
        self.pontos = pontos
        self.pixels = pixels
        self.raio_horizontal = raio_horizontal
        self.raio_vertical = raio_vertical
    def calculo(self):
        medias_z = []
        for ponto1 in self.pixels:
            x1, y1 = ponto1
            valores_z = []
            for ponto2 in self.pontos:
                x2, y2, z = ponto2
                d = Operacoes.distancia_eliptica(x1, y1, x2, y2, self.raio_horizontal, self.raio_vertical)
                if d <= 1:
                    valores_z.append(z)
            media_z = np.mean(valores_z) if valores_z else 0
            medias_z.append(media_z)
        return medias_z

class InversoDaDistancia:
    def __init__(self,pontos, pixels, raio_horizontal = 1500, raio_vertical = 1000, potencia = 1):    
        self.pontos = pontos
        self.pixels = pixels
        self.raio_horizontal = raio_horizontal
        self.raio_vertical = raio_vertical
        self.potencia = potencia
    def calculo(self):
        idw_z = []
        for ponto1 in self.pixels:
            valoresz = []
            dists = []
            x1, y1 = ponto1
            for ponto2 in self.pontos:
                x2, y2, z = ponto2
                d = Operacoes.distancia_eliptica(x1, y1, x2, y2, self.raio_horizontal, self.raio_vertical)
                if d <= 1:
                    distancia_entre_os_pontos = Operacoes.distancia_euclidiana(x1, y1, x2, y2)
                    valoresz.append(z)
                    dists.append(distancia_entre_os_pontos)
            valoresz = np.array(valoresz)
            dists = np.array(dists)
            calculo = np.sum(valoresz / dists**self.potencia) / np.sum(1 / dists**self.potencia)
            if np.isnan(calculo):
                calculo = 0
            idw_z.append(calculo)
        return idw_z



    
