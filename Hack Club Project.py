import pygame as py
from tkinter import messagebox as ms
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
clickUpgradeCount = append(clickUpgradeValue , "Click Upgrade" , "Click Upgrades")
prestigeValue = 0
prestigeCount = append(prestigeValue , "Prestige" , "Prestiges")
stageValue = 1
stageCount = append("Stage" , stageValue , stageValue)
upgradeRequirement = (((10 ** (clickUpgradeValue + 2)) * stageValue) + 1) - dotValue
upgradeRequirementCount = append(upgradeRequirement , "More Dot Needed For The Next Upgrade" , "More Dots Needed For The Next Upgrade")
prestigeRequirement = ((15000 * ((prestigeValue + 1) ** prestigeValue)) + 1) - dotValue
prestigeRequirementCount = append(prestigeRequirement , "More Dot Needed For The Next Prestige" , "More Dots Needed For The Next Prestige")
stagePrestigeRequirement = [10 - prestigeValue , int((((15000 * ((prestigeValue + 1) ** prestigeValue)) * 0.75) + 1) - dotValue)]
stagePrestigeRequirementCount = append(stagePrestigeRequirement[0] , "More Prestige and " , "More Prestiges and ") + append(stagePrestigeRequirement[1] , "More Dot Needed For The Next Stage Prestige" , "More Dots Needed For The Next Stage Prestige") 
firstDotMessage = False
firstUpgradeMessage = False
statistics = dotCount + "\n" + clickCount + "\n" + clickUpgradeCount + "\n" + stageCount + "\n" + upgradeRequirementCount + "\n" + stagePrestigeRequirementCount
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
text = py.sprite.Group()
text.add(dotCounter)
programRunning = True
ms.showinfo("Tutorial" , "Hello! This is a minimalistic cookie clicker made for the Hack Club Arcade.")
ms.showinfo("Tutorial" , "For now, you have to collect as many dots as possible.")
ms.showinfo("Tutorial" , "That blue button you'll see shortly increments the amount of dots you have by 1 every time you press it.")
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
                if prestigeValue > 9 and dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * 0.75):
                    stageValue = stageValue + 1
                    prestigeValue = 0
                    dotValue = 0
                    clickValue = 1
                    clickUpgradeValue = 0
        elif event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                ms.showinfo("Statistics" , statistics)
        elif event.type == IDLEDOTGAIN:
            if stageValue > 1:
                dotValue = dotValue + clickValue
        elif event.type == IDLEDPCGAIN:
            if stageValue > 2:
                clickValue = round(clickValue * 1.5)
    if dotValue == 1 and firstDotMessage == False:
        ms.showinfo("Starting Off" , "You've gained your first dot. You can earn more, and once you have a substantial amount, you'll get another message like this one.")
        firstDotMessage = True
    if dotValue == 101 and firstUpgradeMessage == False:
        ms.showinfo("Upgrades" , "You've reached your first upgrade. When you press that yellow button that you will see shortly, your Dots Per Click (DPC) value will increment by one. This changes how many dots you earn per click.")
        firstUpgradeMessage = True
        ms.showinfo("Statistics" , "To see some statistics, you can press the Space key on your keyboard.")
    screen.fill((255 , 0 , 255))
    mouseX , mouseY = py.mouse.get_pos()
    text.empty()
    dotCount = append(dotValue , "Dot" , "Dots")
    dotCounter = Text(dotCount , 440 , 20 , (255 , 255 , 255) , 25)
    text.add(dotCounter)
    screen.blit(dotButton.surface , dotButton.rect)
    if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
        screen.blit(clickUpgradeButton.surface , clickUpgradeButton.rect)
    if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
        screen.blit(prestigeButton.surface , prestigeButton.rect)
    if prestigeValue > 9 and dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * 0.75):
        screen.blit(stagePrestigeButton.surface , stagePrestigeButton.rect)
    for textbox in text:
        screen.blit(textbox.surface , textbox.rect)
    py.display.flip()
py.quit()
