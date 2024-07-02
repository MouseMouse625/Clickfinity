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
def append(prefix , suffix , pluralMaker):
    if prefix == 1:
        return str(prefix) + " " + str(suffix)
    else:
        return str(prefix) + " " + str(suffix) + str(pluralMaker)
screenWidth = 500
screenHeight = 500
dotValue = 0
dotCount = append(dotValue , "Dot" , "s")
clickValue = 1
clickUpgradeValue = 0
prestigeValue = 0
screen = py.display.set_mode((screenWidth , screenHeight))
py.display.set_icon(py.image.load("Window Icon.png"))
py.display.set_caption("Hack Club Project")
dotButton = Button(30 , 30 , 20 , 20 , (0 , 200 , 255))
clickUpgradeButton = Button(30 , 30 , 20 , 60 , (200 , 255 , 0))
prestigeButton = Button(30 , 30 , 20 , 100 , (255 , 0 , 0))
dotCounter = Text(dotCount , 440 , 20 , (255 , 255 , 255) , 25)
text = py.sprite.Group()
text.add(dotCounter)
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
                if prestigeValue == 0:
                    if dotValue > 15000:
                        prestigeValue = prestigeValue + 1
                        dotValue = 0
                        clickValue = 1
                        clickUpgradeValue = 0
    screen.fill((255 , 0 , 255))
    mouseX , mouseY = py.mouse.get_pos()
    text.empty()
    dotCount = append(dotValue , "Dot" , "s")
    dotCounter = Text(dotCount , 440 , 20 , (255 , 255 , 255) , 25)
    text.add(dotCounter)
    screen.blit(dotButton.surface , dotButton.rect)
    if dotValue > 10 ** (clickUpgradeValue + 2):
        screen.blit(clickUpgradeButton.surface , clickUpgradeButton.rect)
    if prestigeValue == 0:
        if dotValue > 15000:
            screen.blit(prestigeButton.surface , prestigeButton.rect)
    for textbox in text:
        screen.blit(textbox.surface , textbox.rect)
    py.display.flip()
py.quit()
