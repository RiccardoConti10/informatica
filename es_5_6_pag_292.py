class Prodotto():
    def _init_(self, quantità, materiale, oggetto):
        self.quantità = quantità
        self.materiale = materiale
        self.oggetto = oggetto
    def assegna_prezzo(self):
        dizionario_prodotti_in_vendita = {
            1: "Assi",
            2: "Tubi",
            3: "Gioielli"}  

        dizionario_matateriali_dei_prodotti = {
            1: "Legno",
            2: "Metallo",
            3: "Pietre preziose"}
        try:
            prodotto_scelto = list(dizionario_prodotti_in_vendita.values())[self.oggetto-1]
            incrementatore_prezzo = 0
            
            if prodotto_scelto in dizionario_prodotti_in_vendita.values():
                if prodotto_scelto == "Assi":
                    incrementatore_prezzo += 3
                elif prodotto_scelto == "Tubi":
                    incrementatore_prezzo += 7
                elif prodotto_scelto == "Pietre preziose" :
                    incrementatore_prezzo += 25
                incrementatore_prezzo *= self.quantità
                materiale_scelto = list(dizionario_matateriali_dei_prodotti.values())[self.materiale-1]

                try:
                    if materiale_scelto in dizionario_matateriali_dei_prodotti.values():
                        if prodotto_scelto == "Legno":
                            incrementatore_prezzo += 3
                        elif prodotto_scelto == "Metallo":
                            incrementatore_prezzo += 7
                        else:
                            incrementatore_prezzo += 25
                except:
                    print("Il prodotto scelto non lo abbiamo... ci dispiace molto.")
            
                return incrementatore_prezzo
        except:
            print("Il prodotto scelto non lo abbiamo... ci dispiace molto")
    
        

def main():
    print("Benvenuto nel negozio, cosa desidera comprare?\
         \nScrivere il numero del prodotto. ")
    print("1: Assi\
        \n2: Lastre\
        \n3: Gioielli")

    prodotto_da_comprare = int(input())
    numero_di_prodotti = int(input("Quanti ne vuoi?"))

    print(" La lista dei materiali disponibili è la seguente:\
        \n1: Legno\
        \n2: Metallo\
        \n3: Pietre preziose")
    
    materiale = int(input("Di che materiale vuoi il prodotto?\
         \nScrivere il numero del materiale desiderato"))

    prodotto1 = Prodotto(numero_di_prodotti, materiale, prodotto_da_comprare)
    totale = prodotto1.assegna_prezzo()

    if totale != None:
        print("Il prezzo totale è di", totale, "Euro")
        
    else:
        print("")

main()
