## utilizado o import para arredondamento das casas decimais
import math

## variaveis utilizadas na verificação do dia mais votado e montagem da mensagem final do programa
diaMaisVotado = 0
diaEscolhido = ""

print("CONTAGEM DE VOTOS PARA O MELHOR DIA DA LIVE")

## variaveis que guardam a quantidade de votos de cada dia
segunda = int(input("Quantidade de votos para a segunda-feira: "))
terca = int(input("Quantidade de votos para a terça-feira: "))
quarta = int(input("Quantidade de votos para a quarta-feira: "))
quinta = int(input("Quantidade de votos para a quinta-feira: "))
sexta = int(input("Quantidade de votos para a sexta-feira: "))

## verifica os dias e salva em uma variavel o maior numero de votos e o dia escolhido
if segunda > diaMaisVotado:
    diaMaisVotado = segunda
    diaEscolhido = "SEGUNDA FEIRA"
if terca > diaMaisVotado:
    diaMaisVotado = terca
    diaEscolhido = "TERÇA FEIRA"
if quarta > diaMaisVotado:
    diaMaisVotado = quarta
    diaEscolhido = "QUINTA FEIRA"
if quinta > diaMaisVotado:
    diaMaisVotado = quinta
    diaEscolhido = "QUINTA FEIRA"
if sexta > diaMaisVotado:
    diaMaisVotado = sexta
    diaEscolhido = "SEXTA FEIRA"

## verifica caso não tenha sido digitado nenhum voto em nenhum dia
if diaEscolhido == "":
    print("Nenhum voto computado!")
else:
    ## soma dos votos para calculo posterior
    percentual = 100 / (segunda + terca + quarta + quinta + sexta) * diaMaisVotado
    print("O dia da semana mais votado foi {} com {} voto(s) - um total de {}% de votos".format(diaEscolhido, diaMaisVotado, math.floor(percentual)))
