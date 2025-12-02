import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.tamanho = [32, 32]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        self.contador = 0
        self.imagemAtual = 0
        self.listaImagens = []

        for i in range(3):
            imagem = pygame.image.load(f'assets/passaro-{i}.png')
            imagem = pygame.transform.scale(imagem, self.tamanho)
            self.listaImagens.append(imagem)

        # AJUSTE AQUI: Valores mais baixos para movimento mais lento
        self.velocidadeAtual = 0
        self.gravidade = 0.15  # REDUZIDO de 0.5 para 0.15
        self.velocidadeMaxima = 5  # REDUZIDO de 8 para 5
        self.forcaPulo = -4  # REDUZIDO de -10 para -4

    def desenhar(self):
        self.contador += 1
        if self.contador > 5:
            self.contador = 0
            self.imagemAtual = (self.imagemAtual + 1) % 3
        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    def atualizar(self):
        # Aplicar gravidade (mais suave agora)
        self.velocidadeAtual += self.gravidade
        
        # Limitar velocidade máxima
        if self.velocidadeAtual > self.velocidadeMaxima:
            self.velocidadeAtual = self.velocidadeMaxima
        
        # Atualizar posição vertical
        self.posicao[1] += self.velocidadeAtual
        
        # Atualizar o retângulo de colisão
        self.rect = pygame.Rect(self.posicao, self.tamanho)

    def pular(self):
        # Pulo mais controlado
        self.velocidadeAtual = self.forcaPulo

    def getRect(self):
        return self.rect
    
    def getPosicaoX(self):
        return self.posicao[0]