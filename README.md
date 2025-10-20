# Jogo-de-Velha-Vers-o-visual

 Jogo da Velha — Python (Tkinter)
 Projeto completo com interface gráfica desenvolvida em Python com Tkinter.
 Descrição

Este é um Jogo da Velha completo criado em Python, utilizando a biblioteca Tkinter para a interface gráfica.
O projeto foi desenvolvido passo a passo do Exercício 01 ao 09, implementando desde a criação do tabuleiro até o placar e botões extras.

 Recursos implementados:

Tabuleiro 3x3 totalmente funcional.

Alternância automática entre os jogadores X e O.

Verificação de vitória e empate.

Placar atualizado a cada partida.

Botões extras: Reiniciar Partida, Zerar Placar, Créditos.

Testes automáticos integrados.

  Estrutura do Código

O arquivo principal é:

jogo_da_velha_tkinter.py

  Organização em Funções (def)

Cada funcionalidade foi isolada conforme os exercícios:

Exercício	Função	Descrição
01	criar_tabuleiro() / criar_interface()	Montagem do tabuleiro 3x3
02	mudar_jogador()	Alternância de turnos
03	clicar()	Jogada do usuário (função central)
04	check_vencedor_board()	Verifica vitória nas linhas, colunas e diagonais
05	check_empate_board()	Verifica empate
06	atualizar_placar()	Atualiza o placar de X e O
07	reiniciar_partida()	Reinicia o tabuleiro mantendo o placar
08	zerar_placar()	Reseta o placar
09	mostrar_creditos()	Mostra informações do projeto

Além disso, há a função run_tests() que realiza testes automáticos das funções principais de verificação.

 Requisitos

Python 3.8+

Tkinter instalado no sistema

Tkinter já vem incluído no Python (Windows e macOS).

No Linux, instale com:

sudo apt-get install python3-tk

 Como Executar
 Rodar o jogo

Certifique-se de ter o Python e o Tkinter instalados.

Abra o terminal ou prompt de comando na pasta do projeto.

Execute:

python jogo_da_velha_tkinter.py

 Testes Automáticos

O código inclui uma função run_tests() que valida:

Verificação de vitória (linhas, colunas, diagonais);

Verificação de empate;

Consistência da lógica principal.

Executada automaticamente ao iniciar o programa:

run_tests()

 Interface do Jogo

Tela principal:

Mostra o placar (X e O).

Tabuleiro interativo 3x3.

Botões: Reiniciar, Zerar Placar e Créditos.

Fluxo de jogo:

O jogador X começa.

Os turnos se alternam automaticamente.

Uma mensagem aparece ao vencer ou empatar.

O placar é atualizado automaticamente.

 Tecnologias Utilizadas

Python 3

Tkinter (Interface gráfica)

Paradigma funcional/modular

Testes automatizados

 Possíveis Melhorias Futuras

Adicionar modo 1 jogador (vs. computador) com lógica de IA simples.

Personalização de cores e temas visuais.

Histórico de partidas e estatísticas.

 Créditos

Projeto desenvolvido como atividade prática do curso Técnico em Desenvolvimento de Sistemas.
Autor(a): [Seu Nome Aqui]
Instituição: CEM03
Professor(a): [Nome do(a) Professor(a)]

Estrutura de Pastas (sugerida)
 jogo_da_velha/
├── jogo_da_velha_tkinter.py
├── README.md
└── tests/
    └── test_logic.py   # (opcional para testes unitários separados)

Licença

Este projeto é de uso educacional e livre.
Sinta-se à vontade para modificar, estudar e distribuir, desde que cite a autoria original.
