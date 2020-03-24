class Cercle:
    def __init__(self, rayon):
        self.__rayon = rayon

    def GetRayon(self):
        return self.__rayon

    def __add__(self, other):
        return Cercle(self.__rayon+other.__rayon)

    def __lt__(self, other):
        return self.__rayon < other.__rayon

    def __gt__(self, other):
        return self.__rayon > other.__rayon

if __name__ == '__main__':
    C1 = Cercle(2)
    C2 = Cercle(3)
    C3 = C1 + C2
    C4 = C1 < C2
    C5 = C2 > C3
    print(C3.GetRayon()) #R_C1 + R_C2
    print(C4) #C1<C2 ?
    print(C5) #C2>C3 ?
    print(isinstance(C1,Cercle)) #C1 appartient à la classe ?
    print(isinstance(C3,Cercle))
