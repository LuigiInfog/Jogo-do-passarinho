import pygame
import random

class Cano:
    def __init__(self, tela):
        self.imagem = pygame.image.load('assets/cano.png')
        self.tela = tela 
        self.altura_base = random.randint(100, 300)
        self.x = tela.get_width()
        self.distancia = 50
        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
        self.cano_baixo = self.altura_base + self.distancia
        self.velocidade = 2
        self.passou = False  # Novo: para saber se o pássaro já passou por este cano

    def atualizar(self):
        self.x -= self.velocidade
        if self.x < -self.imagem.get_width():
            self.x = self.tela.get_width()
            self.altura_base = random.randint(100, 300)
            self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
            self.cano_baixo = self.altura_base + self.distancia
            self.passou = False  # Resetar quando o cano reaparece
    
    def desenhar(self):
        imagem_invertida = pygame.transform.flip(self.imagem, False, True)
        self.tela.blit(imagem_invertida, (self.x, self.cano_cima))
        self.tela.blit(self.imagem, (self.x, self.cano_baixo))

    def detectarColisao(self, rectJogador):
        rectCanoCima = pygame.Rect((self.x, self.cano_cima), self.imagem.get_size())
        rectCanoBaixo = pygame.Rect((self.x, self.cano_baixo), self.imagem.get_size())

        if rectJogador.colliderect(rectCanoCima) or rectJogador.colliderect(rectCanoBaixo):
            return True
        return False
    
    def passouPeloCano(self, jogador_x):
        # Verifica se o jogador passou pelo cano
        if not self.passou and jogador_x > self.x + self.imagem.get_width():
            self.passou = True
            return True
        return False