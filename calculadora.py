ct = 0
print("1 - somar")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")
print("5 - Encerrar")

while True:

    try:

        operacao = input("Digite o número da operação desejada (1/2/3/4/5): ")

    except ValueError:
        print("Digite um número inteirto, letras não são permitidas")
        continue

    if operacao == "5":
         print("Encerrando a calculadora.")
         break

            
    if operacao not in ["1", "2", "3", "4", "5"]:
        print("Operação inválida. Por favor, digite uma operação válida.")
        continue

 
    if ct == 0:
        valor1 = float(input("Digite o primeiro valor: "))

    else:
        valor1 = ct
        print(f"Usando o último resultado: {valor1}")


    valor2 = float(input("Digite o segundo valor: "))

    if operacao == "1":
        resultado = valor1 + valor2
        ct = resultado

    elif operacao == "2":
        resultado = valor1 - valor2
        ct = resultado

    elif operacao == "3":
        resultado = valor1 * valor2
        ct = resultado

    elif operacao == "4":
        if valor2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            continue
        elif valor2 != 0:
            resultado = valor1 / valor2
            ct = resultado
            print(f"O resultado da operação é: {resultado} Deseja saber o resto da divisão ? (S/N)")
            escolha_resto = input("Digite sua escolha (S/N): ")
            if escolha_resto == "S":
                resto = valor1 % valor2
                print(f"O resto da divisão é: {resto}")
            else:
                print("Você optou por não saber o resto da divisão.")
                continue
        

    print(f"O resultado da operação é: {resultado}")

    print("N - Você deseja realizar uma operação nova ?")
    print("C - Realizar uma operção com o ultimo valor ?")
    print("E - Encerrar")

    escolha = input("Digite sua escolha (N/C/E): ")

    if escolha == "N":
        ct = 0
        continue

    if escolha == "C":
        print("Escolha a operação que deseja realizar novamente")
        continue


    elif escolha == "E":
        print("Encerrando a calculadora.")
        break

    
