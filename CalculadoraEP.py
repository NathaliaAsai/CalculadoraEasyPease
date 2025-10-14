#Receber Dados
name = input("Olá! Bem vindo à calculadora EP. Qual o seu nome?")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f""" {name}, escolha a operação matemárica desejada:
  Adição: A ou +
  Subtração: S ou -
  Multiplicação: M ou *
  Divisão: D ou /""")

#loop condicional
while True:
  operation = input("Operação matemática desejada: ")

  if operation.lower() == "a" or operation == "+":
    result = num1 + num2
    simbolo = "+"
  elif operation.lower() == "s" or operation == "-":
    result =  num1 - num2
    simbolo = "-"
  elif operation.lower() == "m" or operation == "*":
    result =  num1 * num2
    simbolo = "*"
  elif operation.lower() == "d" or operation == "/":
    if num2 == 0:
      print("Erro: Divisão por zero não permitida")
      continue
    result =  num1 / num2
    simbolo = "/"
  else:
    print("Operação invalida")
    continue

#resultado
  print(f"O resultado da operação {num1} {simbolo} {num2} é: {result:.2f}")

#continuar calculando
  while True:
      continuar = input(f"{name}, deseja fazer outra operação? (s/n): ").lower()
      if continuar in ("s","n"):
          break
      print("Opção inválida. Digite apenas 's' ou 'n'.")

  if continuar == "n":
      print("Encerrando...")
      break #sai do while principal

#Trocar os números
  while True:
      trocar = input(f"{name}, deseja TROCAR os números? (s/n): ").lower()
      if trocar in ("s","n"):
         break
      print("Opção inválida. Digite apenas 's' ou 'n'.")

  if trocar == "s":
      num1 = float(input("Digitar o novo primeiro número: "))
      num2 = float(input("Digitar o novo segundo número: "))
