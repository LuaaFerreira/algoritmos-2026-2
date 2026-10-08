#Cenário: no balcão, o sistema pergunta o ano de nascimento do cliente para liberar o combo "maior de idade" (café+energertico)

ano_nascimento = int(input("Ano nascimento "))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(idade)

maior_de_idade= idade >= 18
if maior_de_idade:
    print ("Recebe o combo café+energetico")
else:
    print ("A pessoa é menor de idade")
