vetor = []

def preencherVetor():
    for i in range(101):
        vetor.append(i+1)#append é adicionar

def mostrarVetor():
    preencherVetor()
    for i in range(101):
        print(vetor[i])