import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 450
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🐢 Corrida das Tartarugas 🏁")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
ROXO = (200, 0, 200)
VERMELHO = (255, 0, 0)
VERDE = (0, 200, 0)

# Fonte para texto
fonte = pygame.font.SysFont(None, 48)

# Configurações da corrida
distancia = LARGURA - 100
velocidade_max = 10

# Tartarugas: (cor, nome, y inicial)
tartarugas = [
    (AZUL, "Leonardo", 50),
    (AMARELO, "Michelangelo", 150),
    (ROXO, "Donatello", 260),
    (VERMELHO, "Rafael", 360)
]

# Posições iniciais
posicoes = [50] * len(tartarugas)
vencedor = None
correndo = True

# Loop principal
clock = pygame.time.Clock()
while correndo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(BRANCO)

    # Desenhar linha de chegada
    pygame.draw.line(tela, PRETO, (distancia, 0), (distancia, ALTURA), 5)

    # Atualizar posição das tartarugas
    for i, (cor, nome, y) in enumerate(tartarugas):
        if vencedor is None:
            passos = random.randint(1, velocidade_max)
            posicoes[i] += passos
            if posicoes[i] >= distancia:
                posicoes[i] = distancia
                vencedor = nome

        # Desenhar tartaruga (um círculo colorido simples)
        pygame.draw.circle(tela, cor, (posicoes[i], y), 30)

        # Nome abaixo da tartaruga
        texto = fonte.render(nome, True, PRETO)
        tela.blit(texto, (posicoes[i] - 30, y + 40))

    # Se houver vencedor, mostrar mensagem
    if vencedor:
        texto_final = fonte.render(f"🎉 Vencedor: {vencedor}! 🎉", True, VERDE)
        tela.blit(texto_final, (200, ALTURA - 60))

    pygame.display.flip()
    clock.tick(10)  # controla a velocidade da animação

