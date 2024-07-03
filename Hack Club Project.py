import pygame as py
import tkinter as tk
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
def append(prefix , singularSuffix , pluralSuffix):
    if prefix == 1:
        return str(prefix) + " " + str(singularSuffix)
    else:
        return str(prefix) + " " + str(pluralSuffix)
screenWidth = 500
screenHeight = 500
dotValue = 0
dotCount = append(dotValue , "Dot" , "Dots")
clickValue = 1
clickCount = append(clickValue , "DPC" , "DPC")
clickUpgradeValue = 0
prestigeValue = 0
prestigeCount = append(prestigeValue , "Prestige" , "Prestiges")
stageValue = 3
screen = py.display.set_mode((screenWidth , screenHeight))
py.display.set_icon(py.image.load("Window Icon.png"))
py.display.set_caption("Hack Club Project")
IDLEDOTGAIN = py.USEREVENT + 1
IDLEDPCGAIN = py.USEREVENT + 2
py.time.set_timer(IDLEDOTGAIN , 50)
py.time.set_timer(IDLEDPCGAIN , 500)
dotButton = Button(30 , 30 , 20 , 20 , (0 , 200 , 255))
clickUpgradeButton = Button(30 , 30 , 20 , 60 , (200 , 255 , 0))
prestigeButton = Button(30 , 30 , 20 , 100 , (255 , 0 , 0))
stagePrestigeButton = Button(30 , 30 , 20 , 140 , (0 , 255 , 20))
dotCounter = Text(dotCount , 440 , 20 , (255 , 255 , 255) , 25)
clickCounter = Text(clickCount , 440 , 60 , (255 , 255 , 255) , 25)
prestigeCounter = Text(prestigeCount , 70 , 480 , (255 , 255 , 255) , 25)
text = py.sprite.Group()
text.add(dotCounter , clickCounter , prestigeCounter)
programRunning = True
while programRunning:
    for event in py.event.get():
        if event.type == py.QUIT:
            programRunning = False
        elif event.type == py.MOUSEBUTTONDOWN:
            if mouseX > dotButton.rect.left and mouseX < dotButton.rect.right and mouseY > dotButton.rect.top and mouseY < dotButton.rect.bottom:
                dotValue = dotValue + clickValue
            if mouseX > clickUpgradeButton.rect.left and mouseX < clickUpgradeButton.rect.right and mouseY > clickUpgradeButton.rect.top and mouseY < clickUpgradeButton.rect.bottom:
                if dotValue > 10 ** (clickUpgradeValue + 2):
                    clickValue = (clickValue + 1) * (prestigeValue + 1)
                    clickUpgradeValue = clickUpgradeValue + 1
            if mouseX > prestigeButton.rect.left and mouseX < prestigeButton.rect.right and mouseY > prestigeButton.rect.top and mouseY < prestigeButton.rect.bottom:
                if dotValue > (15000 * ((prestigeValue + 1) ** prestigeValue)):
                    prestigeValue = prestigeValue + 1
                    dotValue = 0
                    clickValue = 1
                    clickUpgradeValue = 0
            if mouseX > stagePrestigeButton.rect.left and mouseX < stagePrestigeButton.rect.right and mouseY > stagePrestigeButton.rect.top and mouseY < stagePrestigeButton.rect.bottom:
                if prestigeValue > 9 and dotValue > ((15000 * ((prestigeValue + 1) ** 1.8)) * 0.75):
                    stageValue = stageValue + 1
                    prestigeValue = 0
                    dotValue = 0
                    clickValue = 1
                    clickUpgradeValue = 0
        elif event.type == IDLEDOTGAIN:
            if stageValue > 1:
                dotValue = dotValue + clickValue
        elif event.type == IDLEDPCGAIN:
            if stageValue > 2:
                clickValue = round(clickValue * 1.5)
    screen.fill((255 , 0 , 255))
    mouseX , mouseY = py.mouse.get_pos()
    text.empty()
    dotCount = append(dotValue , "Dot" , "Dots")
    dotCounter = Text(dotCount , 440 , 20 , (255 , 255 , 255) , 25)
    clickCount = append(clickValue , "DPC" , "DPC")
    clickCounter = Text(clickCount , 440 , 60 , (255 , 255 , 255) , 25)
    prestigeCount = append(prestigeValue , "Prestige" , "Prestiges")
    prestigeCounter = Text(prestigeCount , 70 , 480 , (255 , 255 , 255) , 25)
    text.add(dotCounter , clickCounter , prestigeCounter)
    screen.blit(dotButton.surface , dotButton.rect)
    if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
        screen.blit(clickUpgradeButton.surface , clickUpgradeButton.rect)
    if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
        screen.blit(prestigeButton.surface , prestigeButton.rect)
    if (prestigeValue > 9 ** stageValue) and dotValue > round(((15000 * ((prestigeValue + 1) ** 1.8)) * 0.75)):
        screen.blit(stagePrestigeButton.surface , stagePrestigeButton.rect)
    for textbox in text:
        screen.blit(textbox.surface , textbox.rect)
    py.display.flip()
py.quit()
