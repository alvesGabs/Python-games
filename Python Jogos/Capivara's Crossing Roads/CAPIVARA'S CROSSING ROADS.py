#Nome do projeto: CAPIVARA'S CROSSING ROADS

import os
import pygame
import random
from pygame import mixer

#Caminho atual dos arquivos
CaminhoAtual = os.path.abspath(os.path.dirname(__file__))

#Todos os caminhos relativos!
CaminhoRelativoFundo = os.path.join(CaminhoAtual, "rua.png")
CaminhoRelativoObst = os.path.join(CaminhoAtual, "carro.png")
CaminhoRelativoCapivara = os.path.join(CaminhoAtual, "capivara.png")
CaminhoRelativoMenu = os.path.join(CaminhoAtual, "menu.jfif")
CaminhoRelativoMusica = os.path.join(CaminhoAtual, "musica.mp3")
CaminhoRelativoBatida = os.path.join(CaminhoAtual, "manga.mp3")
CaminhoRelativoVitoria = os.path.join(CaminhoAtual, "flamengo.mp3")

#Imagens utilizadas
carrinho = pygame.image.load(CaminhoRelativoObst)
fundo = pygame.image.load(CaminhoRelativoFundo)
persona = pygame.image.load(CaminhoRelativoCapivara)
menu = pygame.image.load(CaminhoRelativoMenu)

def exibir_menu():
    logo_imagem = pygame.image.load(CaminhoRelativoMenu) 
    tela.blit(logo_imagem, (0, 0))

    # Configuração das fontes
    titulo_fonte = pygame.font.SysFont("Times", 48, bold=True)
    texto_fonte = pygame.font.SysFont("Times", 24)

    # Renderização do título e texto do menu com fundo preto
    titulo_renderizado = titulo_fonte.render("CAPIVARA'S CROSSING ROADS", True, (255, 0, 0))
    texto1_renderizado = texto_fonte.render("Use as teclas WASD para mover a capivara! ", True, (255, 0, 0))
    texto2_renderizado = texto_fonte.render("Este jogo é brutal! Não nos responsabilizamos por possíveis traumas ", True, (200, 0, 0))
    texto3_renderizado = texto_fonte.render("Aperte qualquer tecla para iniciar o game!", True, (200, 0, 0))

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
    
#Criamos duas classes: uma dos carros e outra do jogador para arrumar nossas 'defs'(Funções) e deixar mais limpo o código
class Carro:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y 
        self.velocidade = velocidade
        self.imagem = pygame.image.load(CaminhoRelativoObst)
        self.comprimento = 40 #Aqui damos a proporção do carro quando objeto em nosso jogo
        self.altura = 50 #Mesma coisa dita anteriormente

#Função para ocorrer a movimentação dos carros
    def mover(self):
        self.x -= self.velocidade
        if self.x < -self.comprimento:
            self.x = 950
            self.velocidade = random.choice([5,7,9,11,13,17])

#Para o carro aparecer na tela, utilizamos uma das funções ofertadas pelo pygame, que basicamente trocará o objeto, no caso retângulo, para a imagem proposta
    def desenhar(self, tela):
        carrin = pygame.transform.scale(carrinho, (120, 125))
        tela.blit(carrin, (self.x, self.y))

#Isto daqui é para justamente, apesar da troca do retângulo pela imagem, assistir na hora de efetuarmos a colisão entre o player e o objeto
    def retangular(self):
        return pygame.Rect(self.x, self.y, self.comprimento, self.altura)

class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_inicial = x  # Coordenada x inicial
        self.y_inicial = y  # Coordenada y inicial
        self.imagem = pygame.image.load(CaminhoRelativoCapivara)
        self.comprimento = 40
        self.altura = 20
        self.vel = 6

    def desenhar(self, tela):
        person = pygame.transform.scale(persona, (65, 65))
        tela.blit(person, (self.x, self.y))

#Aqui desenvolvemos um sistema de movimentação bem simples
    def mover(self, direcao):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.vel
        elif direcao == "direita" and self.x < 1000 - self.comprimento:
            self.x += self.vel
        elif direcao == "cima" and self.y > 0:
            self.y -= self.vel
        elif direcao == "baixo" and self.y < 1000 - self.altura:
            self.y += self.vel

#Mesma coisa já dita anteriormente
    def retangular(self):
        return pygame.Rect(self.x, self.y, self.comprimento, self.altura)
    
#Como já diz o nome, esta função servirá justamente para realocar o player quando ele for atingido
    def resetar(self):
        self.x = self.x_inicial
        self.y = self.y_inicial
        atropelado = mixer.Sound(CaminhoRelativoBatida) #Isso daqui é um segredinho
        atropelado.play()

#Iniciar o jogo
pygame.init()

#Dimensões da tela e título
tela = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("CAPIVARA'S CROSSING ROADS")

# Exibir o menu
exibir_menu()

#Musica de fundo
mixer.music.load(CaminhoRelativoMusica)
mixer.music.play(100000000)

#Esta parte é crucial, tanto para o posicionamento dos veículos quanto para as almejadas velocidades operantes em cada objeto
carros = [
    Carro(950, 150, random.choice([5, 7, 9, 11, 13, 17])),
    Carro(950, 150 + 65, random.choice([5, 7, 9, 11, 13, 17])),
    Carro(950, 150 + 68*2, random.choice([5, 7, 9, 11, 13, 17])),
    Carro(950, 150 + 65*3, random.choice([5, 7, 9, 11, 13, 17])),
    Carro(950, 175 + 57*5, random.choice([5, 7, 9, 11, 13, 17])),
    Carro(950, 175 + 56*6, random.choice([5, 7, 9, 11, 13, 17])),
    Carro(950, 175 + 58*7, random.choice([5, 7, 9, 11, 13, 17])),
    Carro(950, 175 + 58*8, random.choice([5, 7, 9, 11, 13, 17])),
]
#Coordenadas em que o player iniciará
jogador = Jogador(500, 775)

#Indica que o jogo esta operando
funcionando = True
#Dá início ao loop do game
while funcionando:
    pygame.time.delay(9)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            funcionando = False

#Nada mais belo do que um background bem lindo para o nosso jogo
    fundo = pygame.transform.scale(fundo, (1000, 1000))
    tela.blit(fundo, (0, 0))

#Com isso, a parte visual e funcional dos carros esta praticamente pronta
    for carro in carros:
        carro.mover()
        carro.desenhar(tela)

#A colisão entre o player e o carro faz com que o jogador "resete" para a posição inicial que iniciou o game
        if carro.retangular().colliderect(jogador.retangular()):
            jogador.resetar()
            
        if jogador.y <= 100:
            jogador.x = 300 
            jogador.y = 775

            ganhou = mixer.Sound(CaminhoRelativoVitoria) #Isso daqui é um segredinho
            ganhou.play()


#Visualização do player
    jogador.desenhar(tela)

#Atribuição dos botões para o player conseguir andar
    botoes = pygame.key.get_pressed()
    if botoes[pygame.K_a]:
        jogador.mover("esquerda")
    elif botoes[pygame.K_d]:
        jogador.mover("direita")
    elif botoes[pygame.K_w]:
        jogador.mover("cima")
    elif botoes[pygame.K_s]:
        jogador.mover("baixo")

#Atualiza a tela
    pygame.display.update()

#Fecha o loop e portanto acaba com todo este processo
pygame.quit()