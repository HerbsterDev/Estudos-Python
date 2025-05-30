def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            return True
    
    for col in range(3):
        if all(tabuleiro[row][col] == jogador for row in range(3)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    
    return False

def verificar_empate(tabuleiro):
    return all(c != " " for linha in tabuleiro for c in linha)

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    
    while True:
        exibir_tabuleiro(tabuleiro)
        
        try:
            linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0-2): "))
            coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0-2): "))
        except ValueError:
            print("Entrada inválida! Use apenas números entre 0 e 2.")
            continue
        
        if linha not in range(3) or coluna not in range(3) or tabuleiro[linha][coluna] != " ":
            print("Movimento inválido! Tente novamente.")
            continue
        
        tabuleiro[linha][coluna] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador_atual} venceu!")
            break
        
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break
        
        jogador_atual = "O" if jogador_atual == "X" else "X"
        
if __name__ == "__main__":
    jogo_da_velha()
