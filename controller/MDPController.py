from models.Operacoes import Operacoes
import numpy as np
class MediaDosPontos:
    def __init__(self,pontos, pixels,raio_horizontal = 1500, raio_vertical = 1000 ):    
        self.pontos = pontos
        self.pixels = pixels
        self.raio_horizontal = raio_horizontal
        self.raio_vertical = raio_vertical
    def calcula(self):
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