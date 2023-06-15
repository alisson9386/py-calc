def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

print("Calculadora Simples")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("0 - Sair")

while True:
    opcao = input("Digite a opção desejada: ")

    if opcao == '0':
        print("Encerrando o programa...")
        break

    if opcao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = soma(num1, num2)
            print("Resultado: ", resultado)
        elif opcao == '2':
            resultado = subtracao(num1, num2)
            print("Resultado: ", resultado)
        elif opcao == '3':
            resultado = multiplicacao(num1, num2)
            print("Resultado: ", resultado)
        elif opcao == '4':
            resultado = divisao(num1, num2)
            print("Resultado: ", resultado)
    else:
        print("Opção inválida!")
