'''In un laboratorio di analisi i pazienti sono sottoposti a un esame specialistico
secondo l'ordine di arrivo, scrivi il programma che consenta di registrare i nomi
dei pazienti man mano che arrivano. Visualizza poi il nome del paziente che deve
essere sottoposto all'esame perchè è il primo della coda in attesa.
(Utilizzare una struttura di coda)'''

def registra_coda(coda = [], stop = False):
    while stop == False:
        paziente = input("Registrazione  dei nomi dei pazienti che devono essere visitati. Scrivi stop per finire la registrazione: ")
        paziente = paziente.capitalize()
        if paziente == "Stop":
            stop = True
        else:
            coda.append(r)
    return coda

def uscita_dalla_coda(stop2 = False):
    global lunghezza_coda
    print("Il primo paziente della lista è, ", l_coda[0], ", si può sottoporre all'esame. Venga.")
    while stop2 == False:        
        print("Il paziente", lunghezza_coda[0], ", ha finito!")
        lumghezza_coda.pop(0)
        if len(lunghezza_coda) == 0:
            print("...")
            print("Questo era l'ultimo, la lista è finita.")
            stop2 = True
        else:
            print("Ora tocca a...", lunghezza_coda[0], ". Entri pure.")

lunghezza_coda = registra_coda()
print("La lista è formata da:", lunghezza_coda)
uscita_dalla_coda()
