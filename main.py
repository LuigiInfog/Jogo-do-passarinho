import pygame
import sys
from scripts.cenas import Partida, Menu

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA = 400
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird - Luigi Info ")

# Cores
COR_FUNDO = (100, 150, 255)

# Relógio para controlar FPS
relogio = pygame.time.Clock()
FPS = 60

# Estado do jogo e pontuação máxima
estado_jogo = "menu"
pontuacao_maxima = 0

# Criar menu inicial
menu = Menu(tela, pontuacao_maxima)
partida = None

# Loop principal do jogo
executando = True
while executando:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False
            # Detectar quando ESPAÇO é pressionado (KEYDOWN, não KEYPRESSED)
            elif evento.key == pygame.K_SPACE and estado_jogo == "partida" and partida:
                partida.jogador.pular()
    
    # Preencher tela com cor de fundo
    tela.fill(COR_FUNDO)
    
    # Lógica de estado do jogo
    if estado_jogo == "menu":
        estado = menu.atualizar()
        estado_jogo = estado
        
        # Se mudou para partida, criar nova partida
        if estado_jogo == "partida":
            partida = Partida(tela)
    
    elif estado_jogo == "partida" and partida:
        # Atualizar partida
        estado, pontuacao_atual = partida.atualizar()
        estado_jogo = estado
        
        # Se voltou para o menu, atualizar pontuação máxima
        if estado_jogo == "menu" and pontuacao_atual > 0:
            if pontuacao_atual > pontuacao_maxima:
                pontuacao_maxima = pontuacao_atual
                menu = Menu(tela, pontuacao_maxima)
    
    # Atualizar tela
    pygame.display.flip()
    
    # Controlar FPS
    relogio.tick(FPS)

# Encerrar Pygame
pygame.quit()
sys.exit()