from models.Operacoes import Operacoes
class VizinhosMaisProximos():
    def __init__(self, pontos, pixels):
        self.pontos = pontos
        self.pixels = pixels
    def calcula(self):
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
