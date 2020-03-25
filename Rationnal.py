class rationnal:
    def __init__(self,numerateur,denominateur):
        self.__numerateur=numerateur
        self.__denominateur=denominateur

    def __str__(self):
        return str(self.__numerateur)+"/"+str(self.__denominateur)


    def __add__(self, other):
        if isinstance(other,rationnal):
            result= rationnal(self.__numerateur*other.__denominateur+other.__numerateur*self.__denominateur,self.__denominateur*other.__denominateur)
            return result.simplifier()
    def __sub__(self, other):
        if isinstance(other,rationnal):
            result=rationnal(self.__numerateur*other.__denominateur-other.__numerateur*self.__denominateur,self.__denominateur*other.__denominateur)
            return result.simplifier()

    def __mul__(self, other):
        if isinstance(other,rationnal):
            result=rationnal(self.__numerateur*other.__numerateur,self.__denominateur*other.__denominateur)
            return result.simplifier()



    def simplifier(self):
        num=self.__numerateur
        deno=self.__denominateur
        reste=num%deno
        if reste ==0:
            PGCD=self.__denominateur
        else:
            while reste!=0:
                num=deno
                deno=reste
                reste=num%deno
                PGCD=deno
        return rationnal(self.__numerateur/PGCD,self.__denominateur/PGCD)


if __name__== '__main__':
    f1=rationnal(6,4)
    f2=rationnal(12,8)
    f3=f1+f2
    f4=f1*f2
    print(f3)
    print(f4)

