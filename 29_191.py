limiti = {
    15000: 0.23,
    28000: 0.27,
    55000: 0.38,
    75000: 0.41,
    1000000000000: 0.43,}

imposta = 0
while True:
    stipendio = int(float(input("A quanto ammonta il tuo stipendio mensile?\n")))
    if stipendio <= 1000000000000:
        for i in range(len(limiti)):
            fascia_redditi = list(limiti)

            if stipendio > fascia_redditi[i] - fascia_redditi[i-1]:
                if i == 0:
                    imposta += fascia_redditi[i] * limiti.get(fascia_redditi[i])
                    stipendio -= fascia_redditi[i]

                else:
                    imposta += (fascia_redditi[i] - fascia_redditi[i-1]) * limiti.get(fascia_redditi[i])
                    stipendio -= fascia_redditi[i] - fascia_redditi[i-1]

            else:
                imposta += stipendio * limiti.get(fascia_redditi[i])
                stipendio = 0
                
        print(imposta)
    else:
        print("Impossibile definire un'imposta per questo reddito.")
        
    stop = input("Premere 0 per uscire oppure  premere qualsiasi altro tasto per continuare.\n ")
    if stop == "0":
        break
