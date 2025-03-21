import math
class Operacoes:
    @classmethod
    def distancia_euclidiana(cls, x1, y1, x2, y2):
        cls.x1 = x1
        cls.y1 = y1
        cls.x2 = x2
        cls.y2 = y2
        return math.sqrt((cls.x2 - cls.x1)**2 + (cls.y2 - cls.y1)**2)
    @classmethod
    def distancia_eliptica(cls, x1,y1,x2,y2,a, b):
        cls.x1 = x1
        cls.y1 = y1
        cls.x2 = x2
        cls.y2 = y2
        cls.a = a
        cls.b = b
        return math.sqrt(((cls.x2 - cls.x1) / cls.a) ** 2 + ((cls.y2 - cls.y1) / cls.b) ** 2)