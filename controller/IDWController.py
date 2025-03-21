from models.Operacoes import Operacoes
import numpy as np
class InversoDaDistancia:
    def __init__(self,pontos, pixels, raio_horizontal = 1500, raio_vertical = 1000, potencia = 2):    
        self.pontos = pontos
        self.pixels = pixels
        self.raio_horizontal = raio_horizontal
        self.raio_vertical = raio_vertical
        self.potencia = potencia
    def calcula(self):
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