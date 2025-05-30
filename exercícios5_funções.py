def eh_primo(i : int):
    if i <= 1:
        return False
    if i == 2:
        return True
    if i % 2 == 0:
        return False
    for n in range(3, int(i ** 0.5) + 1, 2):
        if i % n == 0:
            return False
    return True


N = int(input("Digite um número: "))
if eh_primo(N) == True:
    print("Seu número é primo")
else:
    print("Não é primo")

# soma = 0