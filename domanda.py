import random
from operator import truediv


class Domanda:
    def __init__(self,difficoltà:int,testo_domanda:str,domanda_corretta,domande:list):
        self.difficoltà=difficoltà
        self.testo_domanda=testo_domanda
        self.domande=domande
        self.domanda_corretta=domanda_corretta

    def prop_domanda(self):
        print(self.testo_domanda)
        lista_temp=random.sample(self.domande,len(self.domande))
        risp=int(input("1)"+lista_temp[0]+"\n"
              "2)"+lista_temp[1]+"\n"
              "3)"+lista_temp[2]+"\n"
              "4)"+lista_temp[3]+"\n" 
              "inserire la risposta corretta"))
        if lista_temp[risp-1]==self.domanda_corretta:
            return True
        else:
            return False
