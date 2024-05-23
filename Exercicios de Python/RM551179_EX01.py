## Variavel utilizada caso a user queira continuar utilizando o programa para outros calculos
continuarUtilizando = True

print("""
PROGRAMA PARA CÁLCULO DE ASSINATURA V1.0
""")

## Caso a pessoa queira fazer mais de um calculo por vez

while continuarUtilizando:
 ## Inicia o programa pedindo informações basicas para processar as informações
    tipoAssinatura = input("""Por favor, insira o Código da assinatura:
Código - Tipo Assinatura
1         Basic
2         Silver
3         Gold
4         Platinum   
5         Sair do Programa    
Código: """)

## Verifica se foi digitado o código correto dentre os itens passado
    while (
            tipoAssinatura != '1' and tipoAssinatura != '2' and tipoAssinatura != '3' and tipoAssinatura != '4' and tipoAssinatura != '5'):
        tipoAssinatura = input("""
Ops, acho que não foi inserido um código válido...
Tente novamente, por favor.
Código - Tipo Assinatura
1         Basic
2         Silver
3         Gold
4         Platinum   
5         Sair do Programa    
Código: """)

    if tipoAssinatura != '5':
        ## Pega o valor do faturamento anual para calculo posterior
        faturamentoAnual = float(input("Digite o faturamento anual: "))

        ## Verifica o tipo de assinatura para calculo do valor a ser pago
        porcentagem = 0.0
        if tipoAssinatura == '1':
            porcentagem = 0.3
        elif tipoAssinatura == '2':
            porcentagem = 0.2
        elif tipoAssinatura == '3':
            porcentagem = 0.1
        else:
            porcentagem = 0.05

        ## Calcula o valor do faturamento anual * percentual
        valorPagar = faturamentoAnual * porcentagem

        ## Imprime na tela o valor para o user
        print("O valor a ser pago é de R$ {}".format(valorPagar))

        ## Caso o user queria fazer mais de um calculo com o sistema
        continuarUtilizando = input("Se deseja fazer outro cálculo digite 1, se deseja sair digite 2: ")
        if continuarUtilizando != '1':
            continuarUtilizando = False
    else:
        continuarUtilizando = False
else:
    continuarUtilizando = False
    print("Obrigado por utilizar o nosso software!")