
try:
    import tkinter as tk
    from tkinter import messagebox
    TK_AVAILABLE = True
except Exception:
    TK_AVAILABLE = False

# ------------------------- Aparência / Temas -------------------------------
THEMES = {
    'claro': {
        'root_bg': '#f0f0f0',
        'btn_bg': '#ffffff',
        'btn_fg': '#0f172a',
        'frame_bg': '#f0f0f0',
        'text': '#0f172a'
    },
    'escuro': {
        'root_bg': '#333333',
        'btn_bg': '#555555',
        'btn_fg': '#ffffff',
        'frame_bg': '#333333',
        'text': '#ffffff'
    }
}
current_theme = 'claro'

FONT_BIG = ("Helvetica", 32)
FONT_MED = ("Helvetica", 14)

# ------------------------- Estado do jogo ---------------------------------
root = None
botoes = [[None for _ in range(3)] for _ in range(3)]
board_state = [["" for _ in range(3)] for _ in range(3)]

# placares como exigido no ex 06
placar_x = 0
placar_o = 0
placar = {'X': placar_x, 'O': placar_o}  # manter compatibilidade interna

label_placar_x = None
label_placar_o = None
jogador_atual = 'X'

# ------------------------- Lógica testável (puras) ------------------------

def set_move(r, c, jogador):
    if board_state[r][c] != "":
        return False
    board_state[r][c] = jogador
    return True


def clear_board_state():
    for r in range(3):
        for c in range(3):
            board_state[r][c] = ""


def check_vencedor_board(board):
    # linhas
    for r in range(3):
        if board[r][0] != "" and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    # colunas
    for c in range(3):
        if board[0][c] != "" and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # diagonais
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def check_empate_board(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                return False
    return check_vencedor_board(board) is None

# ------------------------- Funções GUI (se disponível) ---------------------
if TK_AVAILABLE:
    def aplicar_tema():
        """Aplica o tema atual a widgets existentes."""
        theme = THEMES[current_theme]
        root.configure(bg=theme['root_bg'])
        # atualiza botões do tabuleiro
        for r in range(3):
            for c in range(3):
                btn = botoes[r][c]
                if btn is not None:
                    btn.config(bg=theme['btn_bg'], fg=theme['btn_fg'])
        # labels do placar
        if label_placar_x is not None:
            label_placar_x.config(bg=theme['frame_bg'], fg=theme['text'])
        if label_placar_o is not None:
            label_placar_o.config(bg=theme['frame_bg'], fg=theme['text'])

    def toggle_tema():
        global current_theme
        current_theme = 'escuro' if current_theme == 'claro' else 'claro'
        aplicar_tema()

    def criar_interface():
        global root, label_placar_x, label_placar_o
        root = tk.Tk()
        root.title("Jogo da Velha - Tkinter")

        # Placar - linha 0
        placar_frame = tk.Frame(root, bg=THEMES[current_theme]['frame_bg'])
        placar_frame.grid(row=0, column=0, pady=(12, 6), padx=12)

        label_placar_x = tk.Label(placar_frame, text=f"X: {placar['X']}",
                                  font=FONT_MED, width=12, relief='ridge', bd=2,
                                  bg=THEMES[current_theme]['frame_bg'], fg=THEMES[current_theme]['text'])
        label_placar_x.grid(row=0, column=0, padx=6)

        label_placar_o = tk.Label(placar_frame, text=f"O: {placar['O']}",
                                  font=FONT_MED, width=12, relief='ridge', bd=2,
                                  bg=THEMES[current_theme]['frame_bg'], fg=THEMES[current_theme]['text'])
        label_placar_o.grid(row=0, column=1, padx=6)

        # Tabuleiro - linha 1
        board_frame = tk.Frame(root, bg=THEMES[current_theme]['frame_bg'])
        board_frame.grid(row=1, column=0, padx=12, pady=8)

        for r in range(3):
            for c in range(3):
                btn = tk.Button(board_frame, text="", font=FONT_BIG,
                                width=5, height=2,
                                bg=THEMES[current_theme]['btn_bg'], fg=THEMES[current_theme]['btn_fg'],
                                command=lambda r=r, c=c: clicar(r, c))
                btn.grid(row=r, column=c, padx=6, pady=6)
                botoes[r][c] = btn

        # Controles - linha 2
        controles_frame = tk.Frame(root, bg=THEMES[current_theme]['frame_bg'])
        controles_frame.grid(row=2, column=0, pady=(6, 12))

        reiniciar_btn = tk.Button(controles_frame, text="Reiniciar Partida",
                                  font=FONT_MED, width=16,
                                  command=reiniciar_partida)
        reiniciar_btn.grid(row=0, column=0, padx=6)

        zerar_btn = tk.Button(controles_frame, text="Zerar Placar",
                              font=FONT_MED, width=12,
                              command=zerar_placar)
        zerar_btn.grid(row=0, column=1, padx=6)

        creditos_btn = tk.Button(controles_frame, text="Créditos",
                                  font=FONT_MED, width=10,
                                  command=mostrar_creditos)
        creditos_btn.grid(row=0, column=2, padx=6)

        tema_btn = tk.Button(controles_frame, text="Mudar Tema",
                              font=FONT_MED, width=12,
                              command=toggle_tema)
        tema_btn.grid(row=0, column=3, padx=6)

        # aplica tema e inicia jogo
        aplicar_tema()
        iniciar_jogo()

    def iniciar_jogo():
        global jogador_atual
        jogador_atual = 'X'
        clear_board_state()
        for r in range(3):
            for c in range(3):
                if botoes[r][c] is not None:
                    botoes[r][c].config(text="", state='normal')

    def clicar(r, c):
        global jogador_atual, placar_x, placar_o, placar
        btn = botoes[r][c]

        if board_state[r][c] != "":
            return

        # atualiza lógico e visual
        board_state[r][c] = jogador_atual
        btn.config(text=jogador_atual)

        vencedor = check_vencedor_board(board_state)
        if vencedor:
            # atualiza placar (ex 06)
            if vencedor == 'X':
                placar_x += 1
                placar['X'] = placar_x
            else:
                placar_o += 1
                placar['O'] = placar_o
            atualizar_placar()
            messagebox.showinfo("Vencedor", f"Jogador {vencedor} venceu!")
            for i in range(3):
                for j in range(3):
                    botoes[i][j].config(state='disabled')
            return

        if check_empate_board(board_state):
            messagebox.showinfo("Empate", "A partida terminou empatada.")
            return

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

    def atualizar_placar():
        if label_placar_x is not None:
            label_placar_x.config(text=f"X: {placar['X']}")
        if label_placar_o is not None:
            label_placar_o.config(text=f"O: {placar['O']}")

    def reiniciar_partida():
        iniciar_jogo()

    def zerar_placar():
        global placar_x, placar_o, placar
        placar_x = 0
        placar_o = 0
        placar['X'] = 0
        placar['O'] = 0
        atualizar_placar()
        iniciar_jogo()

    def mostrar_creditos():
        creditos_text = (
            "Jogo da Velha - Implementação Tkinter\n"
            "Autores: Giovanna Ohana\n"
            "Turma: Técnico em Desenvolvimento de Sistemas\n"
            "Professor(a): =Alexandre Tolentino)\n"
        )
        messagebox.showinfo("Créditos", creditos_text)

# ------------------------- Versão console (fallback) -----------------------
else:
    def criar_interface():
        print("Tkinter não disponível — iniciando modo console.")

    def iniciar_jogo():
        global jogador_atual
        jogador_atual = 'X'
        clear_board_state()

    def mostrar_creditos():
        print("--- Créditos ---")
        print("Jogo da Velha - Implementação Tkinter")
        print("Autores: Giovanna Ohana")
        print("Turma: Técnico em Desenvolvimento de Sistemas")
        print("Professor(a): Alexandre Tolentino")

    def reiniciar_partida():
        iniciar_jogo()

    def zerar_placar():
        global placar_x, placar_o, placar
        placar_x = 0
        placar_o = 0
        placar['X'] = 0
        placar['O'] = 0
        print("Placar zerado.")
        iniciar_jogo()

    def clicar_console(r, c):
        global jogador_atual, placar_x, placar_o, placar
        if not (0 <= r < 3 and 0 <= c < 3):
            print("Posição inválida")
            return False
        if board_state[r][c] != "":
            print("Casa já ocupada")
            return False
        board_state[r][c] = jogador_atual
        vencedor = check_vencedor_board(board_state)
        if vencedor:
            if vencedor == 'X':
                placar_x += 1
                placar['X'] = placar_x
            else:
                placar_o += 1
                placar['O'] = placar_o
            print(f"Jogador {vencedor} venceu!")
            print(f"Placar: X={placar['X']} O={placar['O']}")
            return True
        if check_empate_board(board_state):
            print("Empate!")
            return True
        # alterna jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        return True

    def mostrar_tabuleiro_console():
        print("\nTabuleiro:")
        for r in range(3):
            print(" | ".join([board_state[r][c] if board_state[r][c] != "" else ' ' for c in range(3)]))
            if r < 2:
                print("---------")

    def console_game_loop():
        global jogador_atual
        iniciar_jogo()
        while True:
            mostrar_tabuleiro_console()
            print(f"Vez do jogador: {jogador_atual}")
            user = input("Digite a jogada como 'row col' (ex: 0 2) ou 'q' para sair: ")
            if user.strip().lower() == 'q':
                print("Saindo...")
                break
            try:
                r, c = map(int, user.split())
            except Exception:
                print("Entrada inválida. Tente novamente.")
                continue
            ok = clicar_console(r, c)
            if not ok:
                continue
            # se terminou rodada (vencedor/empate), pergunta se quer jogar novamente
            vencedor = check_vencedor_board(board_state)
            if vencedor or check_empate_board(board_state):
                if input("Jogar novamente? (s/n): ").strip().lower() == 's':
                    iniciar_jogo()
                    continue
                else:
                    break

# ------------------------- Testes automatizados ----------------------------

def run_tests():
    tests = []
    tests.append(((
        ['X','X','X'],
        ['O','',''],
        ['','','O']
    ), 'X'))
    tests.append(((
        ['X','X','O'],
        ['X','O',''],
        ['O','','']
    ), 'O'))
    tests.append(((
        ['X','O','X'],
        ['X','O','O'],
        ['O','X','X']
    ), None))
    tests.append(((
        ['X','O',' '],
        [' ','X',' '],
        [' ',' ','O']
    ), None))
    # Teste adicional: vitória X na coluna 1
    tests.append(((
        ['O','X',''],
        ['','X','O'],
        ['','X','']
    ), 'X'))

    all_ok = True
    for i, (board_rows, expected) in enumerate(tests, 1):
        board = [[cell if cell != ' ' else "" for cell in row] for row in board_rows]
        winner = check_vencedor_board(board)
        draw = check_empate_board(board)
        if winner != expected:
            print(f"Teste {i} falhou: esperado vencedor={expected}, obteve {winner}")
            all_ok = False
        else:
            print(f"Teste {i} OK: vencedor={winner}")
        if expected is None and all(cell != "" for row in board for cell in row):
            if not draw:
                print(f"Teste {i} falhou: empate esperado, mas draw=False")
                all_ok = False
    if all_ok:
        print("Todos os testes passaram com sucesso.")
    else:
        print("Alguns testes falharam. Verifique as funções de verificação.")

# ------------------------- Entrada principal --------------------------------

def main():
    run_tests()
    if TK_AVAILABLE:
        criar_interface()
        root.mainloop()
    else:
        print("\n--- Modo console ativado (tkinter não disponível) ---\n")
        console_game_loop()

if __name__ == '__main__':
    main()
