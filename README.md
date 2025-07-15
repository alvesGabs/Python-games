# Python-games

Este repositório reúne todos os jogos que desenvolvi usando Python no primeiro semestre da faculdade. Cada projeto foi criado para aprendizado, experimentação e diversão com desenvolvimento de jogos. Alguns jogos utilizam bibliotecas como o `pygame`.

## Jogos Disponíveis

### Frogger (Capivara's Crossing Roads)

Um clone do clássico jogo Frogger, desenvolvido em Python com `pygame`. O objetivo é atravessar a estrada sem ser atingido pelos carros, mas ao invés de um sapo, você controla uma capivara!

#### Como jogar

- Use as teclas **WASD** para mover a capivara.
- Atravesse a estrada até alcançar o outro lado.
- Evite os carros para não ser atropelado.
- Ouça sons de atropelamento e vitória para aumentar a imersão.

#### Requisitos

- Python 3.x
- Biblioteca `pygame` instalada (`pip install pygame`)


### Jogo da Velha

Um clássico jogo da velha implementado em Python que utiliza o algoritmo **Minimax** para a inteligência artificial. O computador joga de forma estratégica para desafiar o jogador.

#### Como jogar

- O computador utiliza o algoritmo Minimax para fazer jogadas ótimas.
- O objetivo é alinhar três símbolos (X ou O) em linha, coluna ou diagonal antes do adversário.

#### Requisitos

- Python 3.x (sem dependências externas)


### WordZapper

WordZapper é um jogo arcade de tiro e vocabulário em que o jogador controla uma nave no espaço e deve atirar nas letras corretas para formar palavras.

####  Como jogar

- Mova a nave com as teclas **WASD**.
- Pressione **Barra de Espaço (Space)** para disparar.
- Acerte as letras da palavra exibida na parte superior da tela.
- Evite colidir com os obstáculos espaciais!

####  Objetivo

- Formar corretamente a palavra sorteada disparando nas letras corretas.
- O jogo termina quando o tempo se esgota ou você completa todas as palavras.

####  Requisitos

- Python 3.x
- Biblioteca `pygame` instalada (`pip install pygame`)


### Forca

Uma versão clássica do jogo da forca desenvolvida em Python. Ideal para treinar lógica de programação e manipulação de strings.

####  Como jogar

- O jogador deve adivinhar letras de uma palavra secreta.
- Cada letra errada desenha uma parte da forca.
- O jogo termina quando o jogador adivinha a palavra ou você perde.

####  Objetivo

- Descobrir a palavra antes de cometer erros demais.
- O jogo utiliza palavras de um arquivo externo (`palavras.txt`), tornando-o facilmente personalizável.

####  Requisitos

- Python 3.x
- Biblioteca `easygui` instaldada (`pip install easygui`)
