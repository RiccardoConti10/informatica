''' Aggiungi alla classe atleta un metodo per assegnare all'atleta il nome 
della squadra in cui gioca'''
class Atleta () :
    def __init__(self, altezza, sport, peso, squadra, visitaMedica):
        self.altezza = altezza
        self.sport = sport
        self.peso = peso
        self.squadra = squadra
        self.visitaMedica = visitaMedica
    def squadra (self) :
        print ("L'Atleta appartiene alla squadra: ",self.squadra)
    squadra ()
