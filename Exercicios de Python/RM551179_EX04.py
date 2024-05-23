print("Programa para calcular a senha de desbloqueio v0.1")

## solicitar o minuto atual da maquina
minutos = int(input("Digite o número de minutos atuais: "))

## valor inicial para calculo da fatoração
nFatorial = 1
## utilizado para saber qual numero do fator atual e somar mais um para o calculo
x = 1

## função para gerar o calculo fatorial
while x <= minutos:
    nFatorial = nFatorial * x
    x += 1

## Exibindo a senha para desbloqueio na tela
print("""Senha para desbloqueio é: LIBERDADE{} """.format(nFatorial))