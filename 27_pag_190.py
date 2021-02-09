'''Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici.
Fornito poi il nome della persona, il programma visualizza il suo numero di telefono oppure un 
messaggio nel caso la persona non sia presente nella rubrica (GC)
'''
lista_numeri = []
lista_nomi = []

d_nomi_num = {}

while True:
    nome = input("Inserisci il nome della persona: ")
    print("inserisci il numero telefonico della persona scelta :")
    numero = input()
    
    lista_nomi.append(nome)
    lista_numeri.append(numero)

    print("Premi 1 per continuare ad inserire persone con il loro numero. Premi 0 per terminare e visualizzare la rubrica. ")
    stop = int(input())
    if stop == 0:
        break

for z in range(len(lista_nomi)):
    d_nomi_num[lista_nomi[z]] = lista_numeri[z]

print(d_nomi_num)

while True:
    print("Digita il nome di una persona per cercare il suo numero nella rubrica: ")
    ricerca = input()
    if ricerca in d_nomi_num.keys():
        print(d_nomi_num.get(ricerca))
    else:
        print(ricerca, " il nome scelto non è nella rubrica")
    print("Premi 1 per continuare la ricerca dei contatti nella rubrica. Premi 0 per terminare. ")
    stop2 = int(input())
    if stop2 == 0:
        break
