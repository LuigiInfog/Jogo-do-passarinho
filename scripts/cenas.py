import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador
from scripts.interfaces import Texto, TextoPontuacao, Botao

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, tela.get_height() // 2)
        self.cano = Cano(tela)
        self.estado = 'partida'

        self.pontosValor = 0
        self.pontosTexto = Texto(tela, f"Pontos: {self.pontosValor}", 10, 10, (255, 255, 255), 30)

    def atualizar(self):
        self.estado = 'partida'
        
        # Atualizar jogador e cano
        self.jogador.atualizar()
        self.cano.atualizar()
        
        # Verificar se o jogador passou pelo cano
        if self.cano.passouPeloCano(self.jogador.getPosicaoX()):
            self.pontosValor += 1
            self.pontosTexto.atualizarTexto(f"Pontos: {self.pontosValor}")
        
        # Verificar colisão
        if self.cano.detectarColisao(self.jogador.getRect()):
            self.estado = "menu"
            pontuacao_final = self.pontosValor
            self.resetar()
            return self.estado, pontuacao_final
        
       
        self.jogador.desenhar()
        self.cano.desenhar()
        self.pontosTexto.desenhar()

        return self.estado, 0
    
    def resetar(self):
        self.jogador.posicao = [100, self.tela.get_height() // 2]
        self.jogador.velocidadeAtual = 0
        self.cano.x = self.tela.get_width()
        self.pontosValor = 0
        self.pontosTexto.atualizarTexto(f"Pontos: {self.pontosValor}")

class Menu: 
    def __init__(self, tela, pontuacao_maxima=0):
        self.tela = tela
        self.titulo = Texto(tela, "FlappyBird", 100, 20, (255, 255, 255), 50)
        self.estado = "menu"
        self.botao__jogar = Botao(tela, "JOGAR", 120, 150, 40, (200, 0, 0), (255, 255, 255))
        
       
        self.pontuacao_maxima = pontuacao_maxima
        self.texto_pontuacao = TextoPontuacao(
            tela, 
            f"Pontuação Máxima: {self.pontuacao_maxima}", 
            50, 220, 
            (255, 215, 0),  
            28
        )
        
        # Créditos - Feito por Luigi Info
        self.creditos = TextoPontuacao(
            tela,
            "Feito por Luigi Info",
            80, 260,
            (100, 200, 255),  # Cor azul clara
            22
        )

    def atualizar(self, nova_pontuacao=0):
        self.estado = "menu"
        
        # Atualizar pontuação máxima se necessário
        if nova_pontuacao > self.pontuacao_maxima:
            self.pontuacao_maxima = nova_pontuacao
            self.texto_pontuacao.atualizarTexto(f"Pontuação Máxima: {self.pontuacao_maxima}")
        
        # Desenhar elementos
        self.titulo.desenhar()
        self.botao__jogar.desenhar()
        self.texto_pontuacao.desenhar()
        self.creditos.desenhar()

        if self.botao__jogar.get_click():
            self.estado = "partida"

        return self.estado