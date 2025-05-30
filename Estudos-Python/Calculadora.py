def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")
    
    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif escolha == '4':
            if num2 == 0:
                print("Erro! Divisão por zero.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()
