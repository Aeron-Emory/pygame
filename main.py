# Example file showing a basic pygame "game loop"
import pygame
import pawn

# pygame setup
pygame.init()
font = pygame.font.SysFont(None, 48)
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
running = True
click_released = True

background = pygame.image.load("assests\\menu\\bg.png")
board = pygame.image.load("assests\\game\\sorry_Board.jpg")
board = pygame.transform.scale(board, (900, 900))
button_image = pygame.image.load("assests\\menu\\start.png").convert_alpha()
circle_image = pygame.image.load("assests\\game\\circle.png").convert_alpha()
circle_image = pygame.transform.scale(circle_image, (50, 50))
button_rect = button_image.get_rect(topleft=(100, 100))
p1 = pawn.pawn()
arrayY = []
arrayX = []
def initializeBoard():
    num = 0
    for i in range(17):
        arrayY.append(num)
        arrayX.append(num)
        num += 56.25
initializeBoard()

class button:
    def __init__(self, x, y, width, height, text):
        self.button_rect = pygame.Rect(x, y, width, height)
        self.button_color = (200, 200, 200)
        self.button_text = font.render(text, True, (0, 0, 0))

    def draw(self, screen):
        pygame.draw.rect(screen, self.button_color, self.button_rect)
        text_rect = self.button_text.get_rect(center=self.button_rect.center)
        screen.blit(self.button_text, text_rect)

class menubutton:
    def __init__(self, text, x, y):
        self.button_image = pygame.image.load("assests\\menu\\buttonT1small.png").convert_alpha()
        self.button_image = pygame.transform.scale(self.button_image, (200, 100))
        self.button_rect = self.button_image.get_rect(topleft=(x, y))
        self.text = font.render(text, True, (100, 0, 0))
        self.text_rect = self.text.get_rect(center=self.button_rect.center, y=self.button_rect.y + 38)

    def draw(self, screen, mouse_pos):
        is_hovering = self.button_rect.collidepoint(mouse_pos)
        if is_hovering:
            self.button_image = pygame.transform.scale(self.button_image, (210, 110))
            self.button_rect = self.button_image.get_rect(topleft=(self.button_rect.x - 5, self.button_rect.y - 5))
            screen.blit(self.button_image, self.button_rect)
        else:
            screen.blit(self.button_image, self.button_rect)
        screen.blit(self.text, self.text_rect)
        if pygame.mouse.get_pressed()[0] and is_hovering:
            self.button_image = pygame.image.load("assests\\menu\\buttonT1smallClicked.png").convert_alpha()
            self.button_image = pygame.transform.scale(self.button_image, (210, 110))
            self.button_rect = self.button_image.get_rect(topleft=(self.button_rect.x, self.button_rect.y))
            screen.blit(self.button_image, self.button_rect)
            screen.blit(self.text, self.text_rect)
            return True
        
def drawPlayer(screen, pawn):
    xpos = int()
    ypos = int()
    for index in range(0, pawn.pos):
        xpos = arrayX[index]
        ypos = arrayY[index]
        xpos += 1
        print("length: ",len(arrayX), len(arrayY))
        if xpos >= len(arrayX):
            xpos = 0
            ypos += 1
        if ypos >= len(arrayY):
            ypos = 0
            xpos = 0
    print("X Position: ", xpos, arrayX[xpos], arrayY[ypos])
    print("Y Position: ", ypos, arrayX[xpos], arrayY[ypos])
    screen.blit(circle_image, circle_image.get_rect(topleft=(arrayX[xpos], arrayY[ypos])))

def cardDraw():
    return 5

def placePLayer(pawn):
    if pawn.pos >= 0 and pawn.pos <= 17:
        pawn

while running:
    mouse_pos = pygame.mouse.get_pos()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_released = True

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background, (0, 0))
    #button(128, 512, 256, 256, "Options").draw(screen)
    #screen.blit(button_image, button_rect)
    quit = menubutton("Quit", 100, 100).draw(screen, mouse_pos)
    start = menubutton("Start", 200, 200).draw(screen, mouse_pos)
    menubutton("2", 200, 300).draw(screen, mouse_pos)
    menubutton("3", 200, 400).draw(screen, mouse_pos)
    pygame.display.flip()
    # RENDER YOUR GAME HERE
    while start:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(board, (0, 0))
        back = menubutton("Back", 100, 100).draw(screen, mouse_pos)
        down = menubutton("down", 100, 200).draw(screen, mouse_pos)
        up = menubutton("up", 100, 300).draw(screen, mouse_pos)
        backward = menubutton("backward", 100, 400).draw(screen, mouse_pos)
        forward = menubutton("forward", 100, 500).draw(screen, mouse_pos)
        drawPlayer(screen, p1)
        if back and click_released:
            click_released = False
            start = False

        if forward:
            if p1.pos <= 61:
                p1.pos += 1
            else:
                p1.pos = 0
        if backward:
            if p1.pos >= 0:
                p1.pos -= 1
            else:
                p1.pos = 61
        pygame.display.flip()
        print("length: ",len(arrayX), len(arrayY))
        clock.tick(60)
        # Here you would typically transition to the main game loop or another screen
    # flip() the display to put your work on screen

    clock.tick(60)  # limits FPS to 60
    if quit and click_released:
        click_released = False
        running = False
    print("length: ",len(arrayX), len(arrayY))

pygame.quit()