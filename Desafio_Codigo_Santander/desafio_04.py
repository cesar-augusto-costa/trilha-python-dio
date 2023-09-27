# Juros Compostos
''' 
Entrada:  
A função deve receber os seguintes parâmetros:

valor_inicial: um número inteiro ou decimal representando o valor inicial do investimento.

taxa_juros: um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de 5%, o valor passado será 0.05.

periodo: um número inteiro representando a quantidade de anos do investimento.

Saída:
A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. O valor final deve ser arredondado para duas casas decimais.
'''

valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

for _ in range(periodo):
    valor_final += valor_final * taxa_juros


print(f"Valor final do investimento: R$ {valor_final:.2f}")
