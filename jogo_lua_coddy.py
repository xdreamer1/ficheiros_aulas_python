import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
ecra = pygame.display.set_caption("Night Sky")
clock = pygame.time.Clock()

# Configure as coisas aqui, antes do loop do jogo.
comet_x = 0
print("Este é o jogo da lua. Diverte-te!")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Altere as coisas aqui, uma vez por quadro.
    comet_x = comet_x + 3
    if comet_x > 700:
        comet_x = -60

    screen.fill((20, 24, 48))
    # Desenhe aqui, depois do preenchimento.
    pygame.draw.circle(screen, (240, 230, 160), (500, 110), 80)
    pygame.draw.circle(screen, (255, 255, 255), (comet_x, 300), 6)

    fonte = pygame.font.Font(None, 36)
    mensagem = fonte.render("Eu criei esta mensagem neste jogo.", True, (255, 255, 255))
    screen.blit(mensagem, (50, 200))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()