import domanda


class Gioco:
    def __init__(self,listaDomande,listaPlayers,livelloMassimoDomande):
        self.listaDomande = listaDomande
        self.listaPlayers = listaPlayers
        self.livelloMassimoDomande = livelloMassimoDomande


    ##qua cerco i file con domande e giocatori ecc...
    def inizializzazioneGioco(self):
        with open("domande.txt","r",encoding="utf-8") as file:
            lista_righe=file.readlines()
            temp_counter=0
            for righe in lista_righe:
                temp_counter++