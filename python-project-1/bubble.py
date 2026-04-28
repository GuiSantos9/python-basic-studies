arr = [2,43,546,67,34,232,65,10,9]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Array ordenado:", arr)

#Eu comparo o primeiro elemento com o segundo, se o primeiro for maior que o segundo eles trocam de lugar 
#Você repete isso para o segundo e o terceiro, depois para o terceiro e o quarto... até chegar ao fim da fila.
#Ao final dessa primeira rodada, você tem a certeza absoluta de que a pessoa mais alta de todas está na 
#última posição.

#Agora você repete o processo para o restante da fila (ignorando o último, que já está no lugar certo). 
#Você faz isso sucessivas vezes até que ninguém mais precise trocar de lugar.
