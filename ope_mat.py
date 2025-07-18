# Vamos solicitar como entrada dois numeros e depois vamos realizar uma operação simpples entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(abs(num1 - num2))
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print("O resultado é:", num1 / num2)
else:
    print("Operação inválida")