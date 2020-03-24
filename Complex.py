class Complex:
    def __init__(self,reel,imagine):
        self.__reel=reel
        self.__imagine=imagine

    def Getreel(self):
        return self.__reel

    def Getimagine(self):
        return self.__imagine

    def __str__(self):
        if self.__imagine<0:
            return str(self.__reel)+str(self.__imagine)+"i"
        if self.__imagine>=0:
            return str(self.__reel)+"+"+ str(self.__imagine)+"i"

    def __add__(self, other):
        return Complex(self.__reel+other.__reel,self.__imagine+other.__imagine)

    def __sub__(self, other):
        return Complex(self.__reel-other.__reel,self.__imagine-other.__imagine)

    def __mul__(self, other):
        return Complex(self.__reel*other.__reel-self.__imagine*other.__imagine,self.__reel*other.__imagine+self.__imagine*other.__reel)

    def __truediv__(self, other):
        return Complex(((self.__reel*other.__reel+self.__imagine*other.__imagine)/(((other.__reel)**2)+((other.__imagine)**2))),(-self.__reel*other.__imagine+self.__imagine*other.__reel)/((other.__reel**2)+(other.__imagine**2)))

    def absolu(self):
        return (self.__reel**2+self.__imagine**2)**(1/2)

    def __eq__(self, other): #==
        return self.__reel==other.__reel and self.__imagine==other.__imagine

    def __ne__(self, other):
        return self.__reel!=other.__reel or self.__imagine!=other.__imagine

if __name__== '__main__':
    c1 = Complex(2,4)
    c2 = Complex(3,-7)
    c3 = c1 + c2
    c4 = c1 - c2
    c5 = c1*c2
    c6 = c1 / c2
    #c7 = c2  c3
    c8 = c1 == c2
    c9 = c1 != c2
    print(c3)
    print(c4)
    print(c5)
    print(c6)
    print(c1.absolu())
    print(c8)
    print(c9)

