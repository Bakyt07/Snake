import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
backgroundimage=pygame.image.load('back.png')
foodimage=pygame.image.load('lemon.png')
endImage=pygame.image.load('end.jpg')

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 15
        self.dx = 5 
        self.dy = 0
        self.is_add = False
        self.score=0
        self.color=(209, 61, 42)

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (self.color), element, self.radius)

    def move(self):
        if self.is_add:
            self.size += 1
            self.elements.append([0, 0])
            self.is_add = False

        for i in range(len(self.elements) - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
    
class Lemon:
    def __init__(self):
        self.x=random.randint(20,765)
        self.y=random.randint(320,555)
    def draw(self):
        screen.blit(foodimage, (self.x, self.y))    
def Impact():
     if (food.y<snake.elements[0][1] +18 and food.y >= snake.elements[0][1] -18) and (food.x>= snake.elements[0][0]-18 and food.x<snake.elements[0][0]+18):
        snake.is_add = True  
        if snake.is_add == True:
            snake.score +=2
            food.x = random.randint(12, 760)
            food.y = random.randint(12, 560)


def Line():
        if snake.elements[0][0]>=790 or snake.elements[0][0]<=10 or snake.elements[0][1]<=10 or snake.elements[0][1]>=590:
            return True
        return False    
def Scores():
    font = pygame.font.SysFont("Your", 35)
    score = font.render("Your score:" + str(snake.score), True, (28, 30, 133))
    screen.blit(score, (630, 17))


def Clash():
    for block in snake.elements[1:]:
        if snake.elements[0][0] == block[0] and snake.elements[0][1] == block[1]:
            return True
    return False
def End():
    snake.dx=0
    snake.dy=0
    snake.radius=0
snake = Snake()
food=Lemon()


running = True
score=0
d = 4

FPS = 30

clock = pygame.time.Clock()

while running:
        mill = clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    running = False 
                if event.key == pygame.K_RIGHT: 
                    snake.dx = d 
                    snake.dy = 0 
                if event.key == pygame.K_LEFT: 
                    snake.dx = -d 
                    snake.dy = 0 
                if event.key == pygame.K_UP: 
                    snake.dx = 0 
                    snake.dy = -d 
                if event.key == pygame.K_DOWN: 
                    snake.dx = 0 
                    snake.dy = d 
        if Line() or Clash():
            End()
            backgroundimage=endImage
        screen.blit(backgroundimage, (0, 0))  

        snake.move()
        Impact()
        food.draw()
        snake.draw()
        Scores()
        
        pygame.display.flip()