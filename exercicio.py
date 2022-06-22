# Questão 1)
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
    
print(SOMA)

# Questão 2)
n = int(input("Que número deseja encontrar: "))
ultimo=1
penultimo=0
count=0
array=[0, 1]

while ultimo < n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    array.append(termo)
    count += 1

for i in range(len(array)):
    if (n==array[i]):
        print("Estou aqui!")
    else:
        print("Aqui não")

# Questão 3)
a) 1, 3, 5, 7, 9, 11, 13, 15
b) 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
c) 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
d) 4, 16, 36, 64, 100, 144, 196, 252
e) 1, 1, 2, 3, 5, 8, 13, 21, 34
f) 2,10, 12, 16, 17, 18, 19, 200, 201, 202, 203


# Questão 4) Se eles estão se cruzando então a distancia deles para a cidade de Ribeirão Preto é a mesma, logo, nenhum estará mais proximo da cidade do que o outro. 

# Questão 5)
texto = ['arroz']
textoReverso = []

for palavra in texto:
    linha = []
    for letra in palavra:
        linha.insert(0, letra)
    textoReverso.append(linha)

print(textoReverso)
