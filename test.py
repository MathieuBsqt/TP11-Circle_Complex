class Duree:
    def __init__(self,heure,minute,seconde):
        self.__heure=heure
        self.__minute=minute
        self.__seconde=seconde

    def __str__(self):
        if self.__minute>59:
            nb=self.__minute//60
            self.__heure+=nb
            self.__minute-=nb*60
        if self.__seconde>59:
            nb=self.__seconde//60
            self.__minute+=nb
            self.__seconde-=nb*60
        return str(self.__heure)+"h"+str(self.__minute)+"m"+str(self.__seconde)+'s'

    def __add__(self, other):
        return Duree(self.__heure+other.__heure,self.__minute+other.__minute,self.__seconde+other.__seconde)

if __name__== '__main__':
    D1=Duree(5,20,6)
    D2=Duree(6,50,66)
    D3=D1+D2
    print(D1)
    print(D3)
