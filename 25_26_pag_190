''' 
25.
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario
che ha per chiave la matricola, mentre il valore associato è il voto. Elenca i risultati in ordine crescente di voto
e successivamente visualizza quali voti diversi tra loro sono stati assegnati, riducendo a uno i voti uguali. (GC)
26.
Con riferimento al dizionario del problema precedente, elenca i numeri di matricola degli studenti che hanno ottenuto
una votazione superiore alla media di tutte le votazioni
'''
import statistics
numero_di_matricola = 0

lista_matricole = []
lista_voti = []
lista_voti_diversi = []
matricole_sopra_la_media = []

dizionario_finale = {}

for i in range(30):
    numero_di_matricola += 1
    print("Inserire voto del numero di matricola", numero_di_matricola, "in registro: ")
    voto = int(input())

    lista_matricole.append(matricola)
    lista_voti.append(voto)

for d in range(len(lista_matricole)):
    dizionario_finale[lista_matricole[e]] = lista_voti[d]

for h in range(len(lista_matricole)):
    controllo = True
    if lista_voti[h] in lista_voti_diversi:
        controllo = False
    if controllo:
        lista_voti_diversi.append(lista_voti[h])

def controllo_media(contatore_mat = 0):
    media_voti = statistics.mean(lista_voti)
    for i in range(len(lista_matricole)):
        contatore_mat += 1
        if lista_voti[i] > media_voti:
            mat_sopra_la_media.append(lista_matricole[contatore_mat-1])
    print("La media dei voti è: ", media_voti)
    return mat_sopra_la_media

lista_voti_diversi.sort(reverse=True)
lista_voti.sort()
print(" La Lista dei voti in ordine crescente è : ", lista_voti)
print(" Il Dizionario in ordine di matricola è : ", dizionario_finale)
print(" I Diversi voti usciti in verifica sono: ", lista_voti_diversi)
print("Le matricole sopra la media sono: ", controllo_media())
