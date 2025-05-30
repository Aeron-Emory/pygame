# Example file showing a basic pygame "game loop"
import pygame
import pawn

# pygame setup
pygame.init()
font = pygame.font.Font('assests\\font\\Bitrimus-BLAPB.ttf', 38)
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
running = True
click_released = True
pygame.display.set_caption("Dude I'm so Sorry!")

background = pygame.image.load("assests\\menu\\bg.png").convert()
board = pygame.image.load("assests\\game\\sorry_Board.jpg").convert()
board = pygame.transform.scale(board, (900, 900))
button_image = pygame.image.load("assests\\menu\\start.png").convert_alpha()
circle_image = pygame.image.load("assests\\game\\circle.png").convert_alpha()
circle_image = pygame.transform.scale(circle_image, (50, 50))
button_rect = button_image.get_rect(topleft=(100, 100))
p1 = pawn.pawn()
n = 0
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

def MapBoard(x, y):
    """
    Creates a Grid system for the game board.
    :param x: height of the board.
    :param y: length of the board.
    """
    x = (x - x * (1 / 18)) / 16
    y = (y - y * (1 / 18)) / 16
    return x, y

class PlayPawn():
    def __init__(self, pawn):
        self.pawn = pawn
        self.pos = pawn.getBoardPostition()
        self.x = 25
        self.y = 25

    def draw(self, screen, newPos): # now newPos is 3
        IncPos = newPos - self.pos # pos is 4 and newPos is 3, so IncPos = -1
        self.pos = newPos # pos is now updated to 3
        Ix, Iy = MapBoard(900, 900)
        if IncPos > 0:
            self.x = self.x + Ix # right
            screen.blit(circle_image, circle_image.get_rect(topleft=(self.x, self.y)))
        elif IncPos < 0:
            self.x = self.x - Ix # left
            screen.blit(circle_image, circle_image.get_rect(topleft=(self.x, self.y)))
        else:
            screen.blit(circle_image, circle_image.get_rect(topleft=(self.x, self.y)))

p = PlayPawn(p1)

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
            elif event.type == pygame.MOUSEBUTTONUP:
                click_released = True
        screen.fill((0, 0, 0))
        screen.blit(board, (0, 0))
        back = menubutton("Back", 100, 100).draw(screen, mouse_pos)
        down = menubutton("LEFT", 100, 200).draw(screen, mouse_pos)
        up = menubutton("RIGHT", 100, 300).draw(screen, mouse_pos)
        backward = menubutton("UP", 100, 400).draw(screen, mouse_pos)
        forward = menubutton("DOWN", 100, 500).draw(screen, mouse_pos)
        #drawPlayer(screen, p1)
        p.draw(screen, n)
        if back and click_released:
            click_released = False
            start = False

        if up and click_released:
            click_released = False
            n += p1.pos + 1
            p.draw(screen, n)
        if down and click_released:
            click_released = False
            n += p1.pos - 1
            p.draw(screen, n)
        if forward and click_released:
            if p1.pos <= 61:
                n = p1.pos + 1
                p.draw(screen, n)
                click_released = False
            else:
                p.draw(screen, n)
                click_released = False
        if backward and click_released:
            if p1.pos >= 0:
                p1.pos -= 1
                p.draw(screen, n)
                click_released = False
            else:
                p.draw(screen, n)
                click_released = False
        pygame.display.flip()
        clock.tick(60)
        # Here you would typically transition to the main game loop or another screen
    # flip() the display to put your work on screen

    clock.tick(60)  # limits FPS to 60
    if quit and click_released:
        click_released = False
        running = False

pygame.quit()