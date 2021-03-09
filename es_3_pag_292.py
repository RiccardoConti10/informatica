''' Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo visitaMedica uguale a True'''
class Atleta () :
    def __init__(self, altezza, sport, peso, squadra, visitaMedica):
        self.altezza = altezza
        self.sport = sport
        self.peso = peso
        self.squadra = squadra
        self.visitaMedica = visitaMedica
    def effettua_visita (self) :
        while True :
            risp = int(input ("L'Atleta ha effettuato la visita medica? Cliccare 1 per dire di sì, cliccare qualsiasi altro tasto per dire di no"))
            if self.visitaMedica == 1 :
                print ("L'Atleta  ha effettuato la visita medica, può giocare")
            else :
                print ("L'Atleta non ha effetuato la visita medica, quindi non può giocare")
                break
    effettua_visita() 
