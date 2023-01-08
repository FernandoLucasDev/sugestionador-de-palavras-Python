import re
arquivo = open('alice.txt', 'r')
lista = []
lista_proximas = []
apos = {}
cont = 0

linhas = arquivo.read().split(' ')
for i in range(0, len(linhas)):
    lista.append(linhas[i])

user = input('Please, digite uma palavra... ')

for n in range(0, len(lista)):
    lista[n].replace("-", "")
    if lista[n] == user:
        lista_proximas.append(lista[n + 1])

for n in lista_proximas:
    contadora = lista_proximas.count(n)
    apos[n] = contadora

ordenado = sorted(apos, key=apos.get, reverse=True)

try:
    pal_1 = ordenado.pop()
    pal_2 = ordenado.pop()
    pal_3 = ordenado.pop()
    print(f'Essas são as palavras que mais aparecem após {user}, no texto:')
    print(f'{pal_1}, {pal_2}, {pal_3}')
except IndexError:
    print('')


