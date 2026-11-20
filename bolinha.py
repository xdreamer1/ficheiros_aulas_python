# Game da bolinha
# Importa as bibliotecas utilizadas 
import sys, pygame

# Define algumas cores em RGB
PRETO  = (0, 0, 0)
BRANCO = (255, 255, 255)

# Inicializa a biblioteca
pygame.init()

# Define a largura e altura da janela em pixels 800x600
size = (800, 600)
screen = pygame.display.set_mode(size)

# Armazena a posicao X e Y do circulo que iremos desenhar dentro do Loop
posicaoCirculo = [200, 30]
# Velocidade de movimentacao do circulo nos eixos X e Y respectivamente
velocidadeCirculo = [5, 5]

# Utilizado para controlar a velocidade de quadros (de atualizacoes da tela)
clock = pygame.time.Clock()

# Define um nome para a janela
pygame.display.set_caption("Introducao")

# Loop principal do jogo
while True:

	# Verifica se algum evento aconteceu
	for event in pygame.event.get():
		# Verifica se foi um evento de saida (pygame.QUIT), 
		# em caso afirmativo fecha a aplicacao
		if event.type == pygame.QUIT: sys.exit()

	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_UP]: posicaoCirculo[1] -= velocidadeCirculo[1]
	if pressed[pygame.K_DOWN]: posicaoCirculo[1] += velocidadeCirculo[1]
	if pressed[pygame.K_LEFT]: posicaoCirculo[0] -= velocidadeCirculo[0]
	if pressed[pygame.K_RIGHT]: posicaoCirculo[0] += velocidadeCirculo[0]

	# Preenche a tela com uma cor, neste caso preto (definido logo apos importar as bibliotecas)
	screen.fill(PRETO)
	
	# Desenha um circulo branco na tela
	pygame.draw.circle(screen, BRANCO, posicaoCirculo, 10)
	
	# Atualiza a tela visivel ao usuario
	pygame.display.flip()

	# Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
	clock.tick(60)