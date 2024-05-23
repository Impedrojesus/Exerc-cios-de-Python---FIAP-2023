print("Soma de notas e calculo de médias")

## variaveis para soma, média e mensagem utilizada no progama
notasPares = 0
notasImpares = 0
mediaGeral = 0.0
mensagem = ""

## feito o laço para soma das notas impares e totalizar a média no final
for linha in range(1, 51, 2):
    notasImpares += float(input("""
Você está digitando as notas dos alunos ÍMPARES          
POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO - {}: """.format(linha)))

## feito o laço para soma das notas pares e totalizar a média no final
for linha in range(2, 51, 2):
    notasPares += float(input("""
Você está digitando as notas dos alunos PARES          
POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO - {}: """.format(linha)))

## verificação de qual foi a maior soma de notas e montagem da mensagem de finalizar o programa
if notasPares > notasImpares:
    mediaGeral = notasPares / 25
    mensagem = """
A média da turma PAR foi {} portanto maior que a impar""".format(mediaGeral)
elif notasImpares > notasPares:
    mediaGeral = notasImpares / 25
    mensagem = """
A média da turma IMPAR foi {} portanto maior que a par""".format(mediaGeral)
else:
    mediaGeral = (notasImpares + notasPares) / 50
    mensagem = """
A média das duas turmas foram iguais - Média {}""".format(mediaGeral)

## imprime na tela a turma com maior média e sua média (caso tenha empate também é falado na mensagem)
print(mensagem)