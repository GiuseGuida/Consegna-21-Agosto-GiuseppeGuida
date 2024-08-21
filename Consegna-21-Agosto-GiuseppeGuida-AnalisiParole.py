import re

def analisi(frase):
    frase = frase.lower()
    frase = re.sub(r'[^\w\s]', '', frase)
    parole = frase.split()
    diz = {}
    for parola in parole:
        if parola in diz:
            diz[parola] +- 1
        else:
            diz[parola] = 1
            
    return diz

frase = "Ciao! Tutto BENE? COme stai!?"

output = analisi(frase)

print(output)


    
