
Q = [0] * 20

for i in range(20):
    while True:
        numero = float(input(f"Digite o valor positivo da posição {i + 1}: "))
        if numero > 0:
            Q[i] = numero
            break
        else:
            print("Por favor, digite um número positivo.")

maior_elemento = Q[0]
menor_elemento = Q[0]
posicao_maior = 0
posicao_menor = 0

for i in range(1, 20):
    if Q[i] > maior_elemento:
        maior_elemento = Q[i]
        posicao_maior = i
    elif Q[i] < menor_elemento:
        menor_elemento = Q[i]
        posicao_menor = i

print(f"O maior elemento de Q é {maior_elemento}, e ele está na posição {posicao_maior + 1}.")
print(f"O menor elemento de Q é {menor_elemento}, e ele está na posição {posicao_menor + 1}.")
