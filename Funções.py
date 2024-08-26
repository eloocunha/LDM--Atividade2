def olaMundo():
  print("Luxemburguês: Salut, pronunciado Sa-lú") 
  print("Francês: Salut")
  print("Alemão: Hallo") 
  print("Italiano: Ciao") 
  print("Tcheco: Ahoj") 
  print("Grego: YAH sahs") 
  print("Croata: Bog") 
  print("Chinês: 你好 (nǐhǎo) para falar com uma pessoa só, 你们好 (nǐmenhǎo) para falar com mais pessoas") 
  print("Hindi: हैलो (hello) ou नमस्ते (namastē)")
olaMundo()

def OlaMundoeVoce(name):
  print(f"Salut, {name}!")
  print(f"Salut, {name}!")
  print(f"Hallo, {name}!")
  print(f"Ciao, {name}!")
  print(f"Aloj, {name}!")
  print(f"Yah shas, {name}!")
  print(f"Bog, {name}!")
  print(f"nǐhǎo, {name}!")
  print(f"nǐmenhǎo, {name}!")
  print(f"namastē, {name}!")
OlaMundoeVoce("Eloisa")

def sum(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def mult(num1, num2):
  return num1 * num2

def div(num1, num2):
  if num2 == 0:
    return "Erro: Divisão por Zero"
  return num1 / num2



num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

operacao = int(input("Digite o número da operação: "))

if operacao == 1:
  print(num1, "+", num2, "=", sum(num1, num2))
elif operacao == 2:
  print(num1, "-", num2, "=", sub(num1, num2))
elif operacao == 3:
  print(num1, "*", num2, "=", mult(num1, num2))
elif operacao == 4:
  print(num1, "/", num2, "=", div(num1, num2))
else:
  print("Operação inválida")