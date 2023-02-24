base = float(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

contador = expoente
resultado = base

while contador > 1:
    resultado = resultado * base
    contador = contador - 1

print("O valor de "+str(base)+" elevador a "+str(expoente)+" é: "+str(resultado))
