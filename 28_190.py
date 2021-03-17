diz = {223 : "Reggio Emilia", 453 : "Venezia", 333 : "Bologna"}
dict = {value:key for key, value in diz.items()}
citta = input("dimmi una citta di cui vuoi sapere il CAP").capitalize()


if citta in dict:
    print("il CAP della città", citta, "è:", dict[citta])

else:
    print("la citta non è nell'elenco")
