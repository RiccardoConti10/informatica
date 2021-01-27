''''Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista
(nazione e relativa capitale si trovano nella medesima posizione delle rispettive liste),
visualizza la capitale di una nazione della quale viene fornito da tastiera il nome,
segnalando con un messaggio di errore il caso in cui la nazione rihiesta non sia compresa nell'elenco
'''
Nazioni = ["Portogallo", "Francia", "Spagna", "Germania", "Italia", "Olanda", "Belgio", "Svizzera", "Danimarca", "Svezia"]
Capitali = ["Lisbona", "Parigi", "Madrid", "Berlino", "Roma", "Amsterdam", "Bruxelles", "Berna", "Copenaghen", "Stoccolma"]
print (Nazioni)
while True:
    scelta_nazione = input("Digita il nome di una nazione per sapere la sua capitale: ")
    scelta_nazione = scelta_nazione.capitalize()
    if scelta_nazione in Nazioni:
        i = Nazioni.index(scelta_nazione)
        print(Capitali[i])
    elif scelta_nazione not in Nazioni :
        print ("ERRORE: la nazione scelta non è presente nell'elenco, scrivi una nazione presente nella lista")
    print ("se desideri finire di controllare capitali, clicca 0, se vuoi continuare clicca 1")
    risposta = input()
    if risposta == 0 :
        print ("ok alla prossima")
        break
    elif risposta == 1:
            print ("ok continuiamo")
        continue
