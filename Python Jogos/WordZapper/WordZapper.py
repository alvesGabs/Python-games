#Nome do projeto: WordZapper

#Importamos as seguintes bibliotecas
import pygame
import random
import os

# Caminho atual dos arquivos
CaminhoAtual = os.path.abspath(os.path.dirname(__file__))

#Arquivo das palavras
ArquivoTxtRelativo = os.path.join(CaminhoAtual, 'palavras.txt')

#Abre o arquivo e nele lê cada linha
with open(ArquivoTxtRelativo) as arquivo:
    todasPalavras = arquivo.readlines()

# Todos os caminhos relativos!
CaminhoRelativoFundo = os.path.join(CaminhoAtual, "espaco.jfif")
CaminhoRelativoObst = os.path.join(CaminhoAtual, "obst.png")
CaminhoRelativoNave = os.path.join(CaminhoAtual, "nave.png")
CaminhoRelativoMenu = os.path.join(CaminhoAtual, "menu.jfif")

# Caminhos relativos das imagens e áudios
navezinha = pygame.image.load(CaminhoRelativoNave)
obstaculos = pygame.image.load(CaminhoRelativoObst)
background = pygame.image.load(CaminhoRelativoFundo)

def exibir_menu():
    logo_imagem = pygame.image.load(CaminhoRelativoMenu) 
    tela.blit(logo_imagem, (0, 0))

    # Configuração das fontes
    titulo_fonte = pygame.font.SysFont("Times", 48, bold=True)
    texto_fonte = pygame.font.SysFont("Times", 24)

    # Renderização do título e texto do menu com fundo preto
    titulo_renderizado = titulo_fonte.render("WordZapper", True, (255, 0, 0))
    texto1_renderizado = texto_fonte.render("Use as teclas WASD para mover e 'Space' para disparar ", True, (255, 0, 0))
    texto2_renderizado = texto_fonte.render("O seu objetivo é formar a palavra disparando nas letras! ", True, (200, 0, 0))
    texto3_renderizado = texto_fonte.render("Pressione qualquer tecla para iniciar o jogo!", True, (200, 0, 0))

    # Desenhar retângulos pretos como fundo para o título e os subtítulos
    tela.blit(pygame.Surface((titulo_renderizado.get_width(), titulo_renderizado.get_height())), (150, 200))
    tela.blit(pygame.Surface((texto1_renderizado.get_width(), texto1_renderizado.get_height())), (200, 300))
    tela.blit(pygame.Surface((texto2_renderizado.get_width(), texto2_renderizado.get_height())), (200, 350))
    tela.blit(pygame.Surface((texto3_renderizado.get_width(), texto3_renderizado.get_height())), (200, 400))

    # Posicionamento dos elementos na tela
    tela.blit(titulo_renderizado, (150, 200))
    tela.blit(texto1_renderizado, (200, 300))
    tela.blit(texto2_renderizado, (200, 350))
    tela.blit(texto3_renderizado, (200, 400))

    pygame.display.update()
   
    # Aguarda o jogador pressionar qualquer tecla para iniciar o jogo
    aguardando_tecla = True
    while aguardando_tecla:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN: 
                aguardando_tecla = False
                break
#Início do jogo
pygame.init()

#Dimensões do jogo e nome do jogo
tela = pygame.display.set_mode((800, 700))
relogio = pygame.time.Clock()
pygame.display.set_caption("Word Zapper")

#Exibir o menu
exibir_menu()

#Classes são sempre bem-vindas e, neste caso, não será diferente. O código contém variáveis próximas aos do jogo "Frogger"
class Obstaculos:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade 
        self.imagem = pygame.image.load(CaminhoRelativoObst) #Aqui instruimos a carregar a imagem direto do caminho relativo
        self.comprimento = 50 #Comprimento da hitbox
        self.altura = 50 #Altura da hitbox

    def mover(self):
        self.x -= self.velocidade
        if self.x < -self.comprimento:
            self.x = 950 #As coordenadas até onde vai e depois desaparece da tela
            self.velocidade = random.choice([1, 3, 5]) #Velocidade randomizadas

    def desenhar(self, tela):
        obst = pygame.transform.scale(obstaculos, (100, 100)) #Escala da imagem
        tela.blit(obst, (self.x, self.y)) #Aparecer na tela, caso contrário, ela pode estar operando em outro "layer" do jogo

    def retangular(self): #Função adotada para facilitar a colisão
        return pygame.Rect(self.x, self.y, self.comprimento, self.altura)

#Classe do player
class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_inicial = x
        self.y_inicial = y
        self.imagem = pygame.image.load(CaminhoRelativoNave) #Caminho relativo sempre ajuda!
        self.comprimento = 70 #Hitbox
        self.altura = 70 #Hitbox
        self.vel = 5 #Velocidade do player
        self.disparos = [] #Abrimos uma lista vazia para os disparos. Dessa forma, economizando uma possível classe que teríamos que usar

    def desenhar(self, tela): 
        nave = pygame.transform.scale(navezinha, (100, 100))
        tela.blit(nave, (self.x, self.y)) 

        for disparo in self.disparos: 
            pygame.draw.rect(tela, (0, 255, 0), disparo) #Cor do disparo e sua criação

    def mover(self, direcao):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.vel
        elif direcao == "direita" and self.x < 850 - self.comprimento:
            self.x += self.vel
        elif direcao == "cima" and self.y > 0:
            self.y -= self.vel
        elif direcao == "baixo" and self.y < 550 - self.altura:
            self.y += self.vel

    def disparar(self):
        disparo = pygame.Rect(self.x + self.comprimento // 2 - 2, self.y, 4, 10) #Função para que os disparos tenham sua colisão e apareçam na tela como pequenos retângulos!
        self.disparos.append(disparo) #Sem isso os disparos não são efetuados 

    def retangular(self):
        return pygame.Rect(self.x, self.y, self.comprimento, self.altura) #Colisão do jogador

#Aqui já é novidade! Basicamente, usaremos a função "font" que a biblioteca pygame provê!
class Alfabeto:
    def __init__(self, x, y, letra):
        self.x = x
        self.y = y
        self.letra = letra
        self.velocidade = 1 #Velocidade que as letras vão passar na tela
        self.fonte = pygame.font.SysFont('Times', 60) #Fonte e tamanho da letra
        self.cor = (255, 255, 0) #Cor amarela

    def mover(self):
        self.x -= self.velocidade
        if self.x < 0:
            self.x = 1700 #Aqui seria a distância que o alfabeto vai percorrer antes de aparecer na tela, ou quando entrar no loop!
            self.velocidade = 1 

    def desenhar(self, tela):
        letra_renderizada = self.fonte.render(self.letra, True, self.cor) #Função para que apareça na tela
        tela.blit(letra_renderizada, (self.x, self.y))

    def retangular(self): #Colisão para ser utilizado já, já
        letra_rect = pygame.Rect(self.x, self.y, 40, 20)
        return letra_rect

#Sim, eu reutilizo códigos. Como sabia? 
#Dar aos destroços suas posições e velocidades randomizadas 

destrocos = [
    Obstaculos(950, 150, random.choice([1, 3, 5])),
    Obstaculos(950, 150 + 65, random.choice([1, 3, 5])),
    Obstaculos(950, 150 + 68 * 2, random.choice([1, 3, 5])),
    Obstaculos(950, 150 + 65 * 3, random.choice([1, 3, 5])),
    Obstaculos(950, 175 + 57 * 5, random.choice([1, 3, 5])),
]

#Coordenadas que o jogador iniciará
jogador = Jogador(100, 500)

#Lista vazia que será utilizada para ser colocada no plano, além das coordenadas que as letras sairão no começo do jogo!
alfabeto = []
x = 1200
y = 75

#Cria uma lista de objetos "Alfabeto"  em um plano. O loop "for" itera de 0 a 25, representando as 26 letras do alfabeto
for i in range(26):
    letra = chr(ord('A') + i)
    alfabeto.append(Alfabeto(x, y, letra))
    x += 60

#Lista vazias das palavras do arquivo .txt e letras acertadas para a aplicação na hora de acertar as letras!
palavras_completas = []
palavra_atual = ""
letras_acertadas = []

#Esta parte inteira é responsável por dar sequência ao jogo, e reiniciar o jogo!
#Aqui usamos a querida "global" que permite que as variáveis sejam acessadas e modificadas fora da função
def reiniciar_palavras():
    global palavra_atual, letras_acertadas
    palavra_atual = random.choice(todasPalavras).strip().upper()
    letras_acertadas = []

#Strip vai ler cada linha, contudo, apenas funcionará com o upper que assistirá na famosa "leitura" e "pop"
def trocar_palavra():
    global palavra_atual
    palavra_atual = random.choice(todasPalavras).strip().upper()

def verificar_palavra_completa():
    global palavra_atual, letras_acertadas, palavras_completas
    if set(palavra_atual) == set(letras_acertadas):
        palavras_completas.append(palavra_atual)
        trocar_palavra()
        letras_acertadas = []

reiniciar_palavras()

#Aqui colocamos o nosso timer em ação!
tempo_restante = 7000 # Tempo total de jogo
tempo_fonte = pygame.font.SysFont('Arial', 30)

#Inicio do loop 
funcionando = True
while funcionando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            funcionando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE: #Adiciona-se o botão de disparar
                jogador.disparar()

    tela.blit(background, (0, 0)) 

    tempo_restante -= 1 # Decrementa o tempo a cada interação do loop
    tempo_restante_renderizado = tempo_fonte.render("Tempo: " + str(tempo_restante//100), True, (255, 255, 255)) #aqui, fazemos com que o tempo apareça no canto inferior direito da tela
    tela.blit(tempo_restante_renderizado, (600, 660)) #Onde ele ficará posicionado!

    #Fecha o jogo quando atinge um número negativo no timer
    if tempo_restante <= 0:
        funcionando = False

    #Aparição dos meteoros na tela
    for objeto in destrocos:
        objeto.mover()
        objeto.desenhar(tela)

    #Em caso de colisão com o player, o timer correrá mais rapidamente!
        if objeto.retangular().colliderect(jogador.retangular()):
            tempo_restante -=10

    for letra in alfabeto:
        letra.mover()
        letra.desenhar(tela)

    #Colisão das letras e checagem para cada colisão feita
        if letra.retangular().colliderect(jogador.retangular()):
            if letra.letra not in letras_acertadas:
                letras_acertadas.append(letra.letra)
                verificar_palavra_completa()

    #Velocidade do disparo
    for disparo in jogador.disparos:
        disparo.y -= 8
        pygame.draw.rect(tela, (255, 0, 0), disparo)

        for letra in alfabeto:
            if disparo.colliderect(letra.retangular()):
                if letra.letra not in letras_acertadas:
                    letras_acertadas.append(letra.letra)
                    verificar_palavra_completa()

                jogador.disparos.remove(disparo)

    jogador.desenhar(tela)

    botoes = pygame.key.get_pressed()
    if botoes[pygame.K_a]:
        jogador.mover("esquerda")
    elif botoes[pygame.K_d]:
        jogador.mover("direita")
    elif botoes[pygame.K_w]:
        jogador.mover("cima")
    elif botoes[pygame.K_s]:
        jogador.mover("baixo")

    # Exibição das palavras
    if len(letras_acertadas) == 0:
        palavra_renderizada = palavra_atual
    else:
        palavra_renderizada = ""
    for letra in palavra_atual:
        if letra in letras_acertadas:
            palavra_renderizada += letra + " "
        else:
            palavra_renderizada += "_ "

    #Caso acerte a letra, ela aparecerá desta forma!
    palavra_fonte = pygame.font.SysFont('Arial', 30)
    palavra_texto = palavra_fonte.render(palavra_renderizada, True, (255, 255, 255))
    tela.blit(palavra_texto, (10, 10))

    pygame.display.update()
    relogio.tick(60)

pygame.quit()