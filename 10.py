while True:
    operacao = input("Digite uma operação (+, -, *, /, **) ou 'S' para sair: ")

    if operacao.upper() == 'S':
        print("Finalizado.")
        break

    elif operacao in ['+', '-', '*', '/', '**']:
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))

        if operacao == '+':
            resultado = n1 + n2
        elif operacao == '-':
            resultado = n1 - n2
        elif operacao == '*':
            resultado = n1 * n2
        elif operacao == '**':
            resultado = n1 ** n2
        elif operacao == '/':
            if n2 != 0:
                resultado = n1 / n2
            else:
                print("Erro: divisão por zero.")

        print(f"= {resultado:.2f}")

    else:
        print("Operação inválida.")