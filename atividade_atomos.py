def dn(a):
    if a==0:
        return
    a = a - 1
    if atm[a].isnumeric():
        numeros_extras = qntZr(a)
        if atm[a - 1- numeros_extras].islower():
            lista.append(atm[a-numeros_extras:a+1]+ " moleculas de "+ atm[a-2-numeros_extras:a-numeros_extras])
            dn(a-2-numeros_extras)
        else:
            lista.append(atm[a-numeros_extras:a+1]+ " moleculas de "+ atm[a - 1-numeros_extras:a-numeros_extras])
            dn(a-1-numeros_extras)
    elif atm[a].isupper():
        lista.append("1 molecula de "+ atm[a])
        dn(a)
    else:
        lista.append("1 molecula de "+ atm[a - 1:a + 1])
        dn(a-1)
def qntZr(a):
    qtZr = 0
    while True:
        if atm[a-1].isnumeric():
            qtZr += 1
            a-= 1
        else:
            return qtZr
lista = []
atm = input("Digite uma substância quimica: ")
dn(len(atm))
for i in range(len(lista)):
    print(lista[len(lista) - i - 1])

