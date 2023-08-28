# Gerenciamento de Pedidos de Comida Online

# Você foi contratado para desenvolver um sistema que armazena informações dos pedidos de comida online realizados por um cliente. O sistema deve permitir ao cliente inserir novos pedidos, escolher um cupom de desconto (10% ou 20%) e exibir o valor total de todos os pedidos realizados até o momento, com o desconto aplicado.

def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
    cupom = input()
 
    if cupom == '10%':
        valorTotal = total - total * 0.10
    elif cupom == '20%':
        valorTotal = total - total * 0.20
    else:
        valorTotal = total
    
    print(f"Valor total: {valorTotal:.2f}")
 
 
if __name__ == "__main__":
    main()