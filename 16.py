
'''Risolvi il problema precedente partendo da due liste che generano un dizionario
con la nazione come chiave e la capitale come valore. Successivamente interroga il dizionario
per visualizzare la capitale di una nazione
'''
def crea_dict(Nazioni, Capitali, dizionario={}):
    for i in range(len(Nazioni)):
        dizionario[Nazioni[i]] = Capitali[i]
    return dizionario

def main():
    Nazioni = ["Spagna", "Portogallo", "Francia", "Germania", "Italia", "Olanda", "Belgio", "Svizzera", "Danimarca", "Austria"]
    Capitali = ["Madrid", "Lisbona", "Parigi", "Berlino", "Roma", "Amsterdam", "Bruxelles", "Berna", "Copenaghen", "Vienna"]
    d =crea_dict(Nazioni, Capitali)
    while True:
        print("Inserire il nome di una nazione per ricevere il nome della sua capitale: ")
        nazione = input()
        nazione = naz.capitalize()
        if naz not in d:
            print("Nazione non trovata. Premere 0 per chiudere o premere qualsiasi altro tasto per reinserire la nazione: ")
            scelta = input()
            if scelta == "0":
                break
        else:
            cap = d.get(naz)
            print("La capitale è:", capitale, "Premere 0 per chiudere o premere qualsiasi altro tasto per reinserire la nazione:")
            scelta2 = input()
            if scelta2 == "0":
                break

main()
