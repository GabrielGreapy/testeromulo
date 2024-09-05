pessoas = {
    "Leonardo": 30,
    "Mariana": 15,
    "Gustavo": 29,
    "Bianca": 32,
    "Vinícius": 18,
    "Amanda": 26,
    "Henrique": 11,
    "Camila": 27,
    "Felipe": 33,
    "Juliana": 30,
}
nova_lista = []
def maiores18(dicionario):
    lista = []
    for k,v in dicionario.items:
        if v >= 18:
            lista.append(k)
    lista.sort()
    return(lista)

print(maiores18(dicionario=pessoas))