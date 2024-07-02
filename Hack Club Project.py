import pygame as py
py.init()
class Button(py.sprite.Sprite):
    def __init__(self , width , height , xPosition , yPosition , colour):
        super().__init__()
        self.width = width
        self.height = height
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.colour = colour
        self.surface = py.Surface((self.width , self.height))
        self.surface.fill(colour)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.xPosition , self.yPosition)
class Text(py.sprite.Sprite):
    def __init__(self , text , xPosition , yPosition , colour , size):
        super().__init__()
        self.text = text
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.colour = colour
        self.size = size
        self.surface = comfortaa(self.size).render(str(self.text) , True , self.colour)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.xPosition , self.yPosition)
def comfortaa(size):
    return py.font.Font("Comfortaa-Light.ttf" , (size))
def append(prefix , suffix):
    if prefix == 1:
        return str(prefix) + str(suffix)
    else:
        return str(prefix) + " " + str(suffix) + "s"
screenWidth = 500
screenHeight = 500
dotValue = 0
dotCount = append(dotValue , "Dot")
print(dotCount)
screen = py.display.set_mode((screenWidth , screenHeight))
py.display.set_icon(py.image.load("Window Icon.png"))
py.display.set_caption("Hack Club Project")
dotButton = Button(30 , 30 , 20 , 20 , (0 , 200 , 255))
dotCounter = Text(dotCount , 455 , 20 , (255 , 255 , 255) , 25)
buttons = py.sprite.Group()
text = py.sprite.Group()
buttons.add(dotButton)
text.add(dotCounter)
programRunning = True
while programRunning:
    for event in py.event.get():
        if event.type == py.QUIT:
            programRunning = False
    screen.fill((255 , 0 , 255))
    for button in buttons:
        screen.blit(button.surface , button.rect)
    for textbox in text:
        screen.blit(textbox.surface , textbox.rect)
    py.display.flip()
py.quit()
