'''Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore''' 
class Atleta () :
    def __init__(self, altezza, sport, peso, squadra, visitaMedica):
        self.altezza = altezza
        self.sport = sport
        self.peso = peso
        self.squadra = squadra
        self.visitaMedica = visitaMedica    
    def dati_giocatore (self) :
        while True :
            lista_dati = [self.altezza, self.sport, self.peso, self.squadra, self.visitaMedica]
            risp = int (input ("cliccare 1 per sapere i dati dell'atleta"))
            if risp == 1 :
                print (lista_dati)
            else :
                print ("fa niente")
    dati_giocatore ()
