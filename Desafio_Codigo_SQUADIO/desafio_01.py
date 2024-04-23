# Desafio
# Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

# Entrada
# Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta. .

# Saída
# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

# Desafio: A Aventura do Explorador

# Entrada
while True:
  quantidade_passos = int(input())
  if quantidade_passos >= 0:
    break

if quantidade_passos == 0:
  print("Nenhum passo dado na floresta.")
else:
  for i in range(quantidade_passos):
    if i == 0:
      print('Explorador:', i+1, "passo")
    else:
      print('Explorador:', i+1, "passos")