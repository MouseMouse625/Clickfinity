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
prestigeValue = 10
prestigeCount = append(prestigeValue , "Prestige" , "Prestiges")
stageValue = 1
stageCount = append("Stage" , stageValue , stageValue)
upgradeRequirement = (((10 ** (clickUpgradeValue + 2)) * stageValue) + 1) - dotValue
upgradeRequirementCount = append(upgradeRequirement , "More Dot Needed For The Next Upgrade" , "More Dots Needed For The Next Upgrade")
prestigeRequirement = ((15000 * ((prestigeValue + 1) ** prestigeValue)) + 1) - dotValue
prestigeRequirementCount = append(prestigeRequirement , "More Dot Needed For The Next Prestige" , "More Dots Needed For The Next Prestige")
stagePrestigeRequirement = [(9 ** stageValue + 1) - prestigeValue , int((((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75) + 1) - dotValue)]
stagePrestigeRequirementCount = append(stagePrestigeRequirement[0] , "More Prestige and " , "More Prestiges and ") + append(stagePrestigeRequirement[1] , "More Dot Needed For The Next Stage Prestige" , "More Dots Needed For The Next Stage Prestige") 
firstDotMessage = False
firstUpgradeMessage = False
firstPrestigeMessage = False
firstStagePrestigeMessage = False
stageTwoMessage = False
stageThreeMessage = False
statistics = dotCount + "\n" + clickCount + "\n" + clickUpgradeCount + "\n" + stageCount + "\n" + upgradeRequirementCount + "\n" + prestigeRequirementCount + "\n" + stagePrestigeRequirementCount
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
                if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
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
    if dotValue > 0 and firstDotMessage == False:
        firstDotMessage = True
        ms.showinfo("Starting Off" , "You've gained your first dot. You can earn more, and once you have a substantial amount, you'll get another message like this one.")
    if dotValue > 100 and firstUpgradeMessage == False:
        firstUpgradeMessage = True
        ms.showinfo("Upgrades" , "You've reached your first upgrade. When you press that yellow button that you will see shortly, your Dots Per Click (DPC) value will increment by one. This changes how many dots you earn per click.")
        ms.showinfo("Statistics" , "To see some statistics, you can press the Space key on your keyboard.")
    if dotValue > 11250 and firstPrestigeMessage == False:
        firstPrestigeMessage = True
        ms.showinfo("Prestiges" , "You have reached the point where you can undergo your first prestige. When you press the red button that you will see shortly, you will prestige. This means that all of your statistics, including your dots and DPC will be reset to 0 and 1 respectively. Things like how many times you have prestiged will be incremented by one of course, and your stage (you'll learn about that later) will stay the same. Although this seems purely negative, the rate at which your DPC increments will be vastly different (positively), and you will reach more and more dot counts.")
    if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75) and firstStagePrestigeMessage == False:
        firstStagePrestigeMessage = True
        ms.showinfo("Stage Prestiges" , "After a long time, you have reached your first stage prestige. Stage prestiges reset everything that prestiges do, as well as your prestige count. On the other hand, your stage increments by one. A stage prestige always automates some part of the game that hasn't been automated before, eventualy allowing full idle gameplay. You can stage prestige by pressing the green button that you will se shortly. There is a suprise in Stage 2.")
    if stageValue > 1 and stageTwoMessage == False:
        stageTwoMessage = True
        ms.showinfo("Stage 2" , "This is the second Stage. As promised, once you progress after reading this message, a part of the game will be automated. Good luck.")
    if stageValue > 2 and stageThreeMessage == False:
        stageThreeMessage = True
        ms.showinfo("Stage 3" , "You should have gotten the gist by now. Last time, idle dot gain was implemented. Now, something else will be automated. See you in Stage 4.")
    screen.fill((255 , 0 , 255))
    mouseX , mouseY = py.mouse.get_pos()
    text.empty()
    upgradeRequirement = (((10 ** (clickUpgradeValue + 2)) * stageValue) + 1) - dotValue
    prestigeRequirement = ((15000 * ((prestigeValue + 1) ** prestigeValue)) + 1) - dotValue
    stagePrestigeRequirement = [(9 ** stageValue + 1) - prestigeValue , int((((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75) + 1) - dotValue)]
    dotCount = append(dotValue , "Dot" , "Dots")
    clickCount = append(clickValue , "DPC" , "DPC")
    clickUpgradeCount = append(clickUpgradeValue , "Click Upgrade" , "Click Upgrades")
    prestigeCount = append(prestigeValue , "Prestige" , "Prestiges")
    upgradeRequirementCount = append(upgradeRequirement , "More Dot Needed For The Next Upgrade" , "More Dots Needed For The Next Upgrade")
    prestigeRequirementCount = append(prestigeRequirement , "More Dot Needed For The Next Prestige" , "More Dots Needed For The Next Prestige")
    stagePrestigeRequirementCount = append(stagePrestigeRequirement[0] , "More Prestige and " , "More Prestiges and ") + append(stagePrestigeRequirement[1] , "More Dot Needed For The Next Stage Prestige" , "More Dots Needed For The Next Stage Prestige") 
    dotCounter = Text(dotCount , 440 , 20 , (255 , 255 , 255) , 25)
    text.add(dotCounter)
    statistics = dotCount + "\n" + clickCount + "\n" + clickUpgradeCount + "\n" + stageCount + "\n" + upgradeRequirementCount + "\n" + prestigeRequirementCount + "\n" + stagePrestigeRequirementCount
    screen.blit(dotButton.surface , dotButton.rect)
    if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
        screen.blit(clickUpgradeButton.surface , clickUpgradeButton.rect)
    if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
        screen.blit(prestigeButton.surface , prestigeButton.rect)
    if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
        screen.blit(stagePrestigeButton.surface , stagePrestigeButton.rect)
    for textbox in text:
        screen.blit(textbox.surface , textbox.rect)
    py.display.flip()
py.quit()
