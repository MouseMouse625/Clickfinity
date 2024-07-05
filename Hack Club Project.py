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
def append(prefix , singularSuffix , pluralSuffix , sciNotationBool):
    if sciNotationBool == True:
        if prefix == 1:
            return str(prefix) + " " + str(singularSuffix)
        else:
            if int(prefix) > 999999:
                prefix = "{:.2e}".format(prefix)
            return str(prefix) + " " + str(pluralSuffix)
    else:
        if prefix == 1:
            return str(prefix) + " " + str(singularSuffix)
        else:
            return str(prefix) + " " + str(pluralSuffix)
def yinYang(object , blackBool):
    objectClass = object.__class__
    objectName = objectClass.__name__
    if blackBool == False:
        if objectName == "Text":
            return Text(object.text , object.xPosition , object.yPosition , (255 , 255 , 255) , object.size)
        elif objectName == "Button":
            return Button(object.width , object.height , object.xPosition , object.yPosition , (255 , 255 , 255))
    else:
        if objectName == "Text":
            return Text(object.text , object.xPosition , object.yPosition , (0 , 0 , 0) , object.size)
        elif objectName == "Button":
            return Button(object.width , object.height , object.xPosition , object.yPosition , (0 , 0 , 0))
screenWidth = 500
screenHeight = 500
level = "Menu"
theme = "Classic"
dotValue = 0
dotCount = append(dotValue , "Dot" , "Dots" , True)
clickValue = 1
clickCount = append(clickValue , "DPC" , "DPC" , True)
clickUpgradeValue = 0
clickUpgradeCount = append(clickUpgradeValue , "Click Upgrade" , "Click Upgrades" , True)
prestigeValue = 10
prestigeCount = append(prestigeValue , "Prestige" , "Prestiges" , True)
stageValue = 1
stageCount = append("Stage" , stageValue , stageValue , False)
upgradeRequirement = (((10 ** (clickUpgradeValue + 2)) * stageValue) + 1) - dotValue
upgradeRequirementCount = append(upgradeRequirement , "More Dot Needed For The Next Upgrade" , "More Dots Needed For The Next Upgrade" , True)
prestigeRequirement = ((15000 * ((prestigeValue + 1) ** prestigeValue)) + 1) - dotValue
prestigeRequirementCount = append(prestigeRequirement , "More Dot Needed For The Next Prestige" , "More Dots Needed For The Next Prestige" , True)
stagePrestigeRequirement = [(9 ** stageValue + 1) - prestigeValue , int((((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75) + 1) - dotValue)]
stagePrestigeRequirementCount = str(append(stagePrestigeRequirement[0] , "More Prestige and " , "More Prestiges and " , True)) + str(append(stagePrestigeRequirement[1] , "More Dot Needed For The Next Stage Prestige" , "More Dots Needed For The Next Stage Prestige" , True))
tutorialMessage = False
firstDotMessage = False
firstUpgradeMessage = False
firstPrestigeMessage = False
firstStagePrestigeMessage = False
stageTwoMessage = False
stageThreeMessage = False
stageFourMessage = False
stageFiveMessage = False
statistics = dotCount + "\n" + clickCount + "\n" + clickUpgradeCount + "\n" + stageCount + "\n" + upgradeRequirementCount + "\n" + prestigeRequirementCount + "\n" + stagePrestigeRequirementCount
screen = py.display.set_mode((screenWidth , screenHeight))
py.display.set_icon(py.image.load("Window Icon.png"))
py.display.set_caption("Hack Club Project")
IDLEDOTGAIN = py.USEREVENT + 1
IDLEDPCGAIN = py.USEREVENT + 2
IDLEUPGRADE = py.USEREVENT + 3
IDLEPRESTIGE = py.USEREVENT + 4
START = py.USEREVENT + 5
py.time.set_timer(IDLEDOTGAIN , 50)
py.time.set_timer(IDLEDPCGAIN , 500)
py.time.set_timer(IDLEUPGRADE , 10)
py.time.set_timer(IDLEPRESTIGE , 10)
classicDotButton = Button(30 , 30 , 20 , 20 , (0 , 200 , 255))
classicClickUpgradeButton = Button(30 , 30 , 20 , 60 , (200 , 255 , 0))
classicPrestigeButton = Button(30 , 30 , 20 , 100 , (255 , 0 , 0))
classicStagePrestigeButton = Button(30 , 30 , 20 , 140 , (0 , 255 , 20))
classicStartButton = Button(110 , 60 , 250 , 220 , (0 , 200 , 255))
classicThemeButton = Button(90 , 30 , 250 , 270 , (0 , 200 , 255))
classicClassicButton = Button(110 , 38 , 250 , 250 , (0 , 200 , 255))
classicYinYangButton = Button(138 , 38 , 250 , 271 , (0 , 200 , 255))
classicYangYinButton = Button (138 , 38 , 250 , 229 , (0 , 200 , 255))
classicClassicButtonText = Text("Classic" , 250 , 250 , (255 , 255 , 255) , 30)
classicYinYangButtonText = Text("Yin Yang" , 250 , 271 , (255 , 255 , 255) , 30)
classicYangYinButtonText = Text("Yang Yin" , 250 , 229 , (255 , 255 , 255) , 30)
classicStartButtonText = Text("Play" , 250 , 218 , (255 , 255 , 255) , 50)
classicThemeButtonText = Text("Theme" , 250 , 268 , (255 , 255 , 255) , 25)
classicDotCounter = Text(dotCount , 410 , 20 , (255 , 255 , 255) , 25)
classicMenuObjects = py.sprite.Group()
classicThemesObjects = py.sprite.Group()
classicMenuObjects.add(classicStartButton , classicThemeButton , classicStartButtonText , classicThemeButtonText)
classicThemesObjects.add(classicClassicButton , classicYinYangButton , classicYangYinButton , classicClassicButtonText , classicYinYangButtonText , classicYangYinButtonText)
yinYangDotButton = yinYang(classicDotButton , False)
yinYangClickUpgradeButton = yinYang(classicClickUpgradeButton , False)
yinYangPrestigeButton = yinYang(classicPrestigeButton , False)
yinYangStagePrestigeButton = yinYang(classicStagePrestigeButton , False)
yinYangStartButton = yinYang(classicStartButton , False)
yinYangThemeButton = yinYang(classicThemeButton , False)
yinYangClassicButton = yinYang(classicClassicButton , False)
yinYangYinYangButton = yinYang(classicYinYangButton , False)
yinYangYangYinButton = yinYang(classicYangYinButton , False)
yinYangClassicButtonText = yinYang(classicClassicButtonText , True)
yinYangYinYangButtonText = yinYang(classicYinYangButtonText , True)
yinYangYangYinButtonText = yinYang(classicYangYinButtonText , True)
yinYangThemeButtonText = yinYang(classicThemeButtonText , True)
yinYangStartButtonText = yinYang(classicStartButtonText , True)
yinYangDotCounter = yinYang(classicDotCounter , False)
yinYangMenuObjects = py.sprite.Group()
yinYangThemesObjects = py.sprite.Group()
yinYangMenuObjects.add(yinYangStartButton , yinYangThemeButton , yinYangThemeButtonText , yinYangStartButtonText)
yinYangThemesObjects.add(yinYangClassicButton , yinYangClassicButtonText , yinYangYangYinButton , yinYangYangYinButtonText , yinYangYinYangButton , yinYangYinYangButtonText)
yangYinDotButton = yinYang(classicDotButton , True)
yangYinClickUpgradeButton = yinYang(classicClickUpgradeButton , True)
yangYinPrestigeButton = yinYang(classicPrestigeButton , True)
yangYinStagePrestigeButton = yinYang(classicStagePrestigeButton , True)
yangYinStartButton = yinYang(classicStartButton , True)
yangYinThemeButton = yinYang(classicThemeButton , True)
yangYinClassicButton = yinYang(classicClassicButton , True)
yangYinYinYangButton = yinYang(classicYinYangButton , True)
yangYinYangYinButton = yinYang(classicYangYinButton , True)
yangYinClassicButtonText = yinYang(classicClassicButtonText , False)
yangYinYinYangButtonText = yinYang(classicYinYangButtonText , False)
yangYinYangYinButtonText = yinYang(classicYangYinButtonText , False)
yangYinThemeButtonText = yinYang(classicThemeButtonText , False)
yangYinStartButtonText = yinYang(classicStartButtonText , False)
yangYinDotCounter = yinYang(classicDotCounter , True)
yangYinMenuObjects = py.sprite.Group()
yangYinThemesObjects = py.sprite.Group()
yangYinMenuObjects.add(yangYinStartButton , yangYinThemeButton , yangYinThemeButtonText , yangYinStartButtonText)
yangYinThemesObjects.add(yangYinClassicButton , yangYinClassicButtonText , yangYinYinYangButton , yangYinYinYangButtonText , yangYinYangYinButton , yangYinYangYinButtonText)
programRunning = True
while programRunning:
    if level == "Menu":
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if event.type == py.MOUSEBUTTONDOWN:
                if mouseX > classicStartButton.rect.left and mouseX < classicStartButton.rect.right and mouseY > classicStartButton.rect.top and mouseY < classicStartButton.rect.bottom:
                    level = "Game"
                if mouseX > classicThemeButton.rect.left and mouseX < classicThemeButton.rect.right and mouseY > classicThemeButton.rect.top and mouseY < classicThemeButton.rect.bottom:
                    level = "Themes"
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicMenuObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangMenuObjects:
                screen.blit(object.surface , object.rect)
        mouseX , mouseY = py.mouse.get_pos()
        py.display.flip()
    elif level == "Themes":
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if event.type == py.MOUSEBUTTONDOWN:
                if mouseX > classicClassicButton.rect.left and mouseX < classicClassicButton.rect.right and mouseY > classicClassicButton.rect.top and mouseY < classicClassicButton.rect.bottom:
                    theme = "Classic"
                if mouseX > classicYinYangButton.rect.left and mouseX < classicYinYangButton.rect.right and mouseY > classicYinYangButton.rect.top and mouseY < classicYinYangButton.rect.bottom:
                    theme = "Yin Yang"
                if mouseX > classicYinYangButton.rect.left and mouseX < classicYinYangButton.rect.right and mouseY > classicYinYangButton.rect.top and mouseY < classicYinYangButton.rect.bottom:
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicThemesObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangThemesObjects:
                screen.blit(object.surface , object.rect)
        mouseX , mouseY = py.mouse.get_pos()
        py.display.flip()
    elif level == "Game":
        if tutorialMessage == False:
            tutorialMessage = True
            ms.showinfo("Tutorial" , "Hello! This is a minimalistic cookie clicker made for the Hack Club Arcade.")
            ms.showinfo("Tutorial" , "For now, you have to collect as many dots as possible.")
            ms.showinfo("Tutorial" , "That blue button you'll see shortly increments the amount of dots you have by 1 every time you press it.")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if event.type == py.MOUSEBUTTONDOWN:
                if mouseX > classicDotButton.rect.left and mouseX < classicDotButton.rect.right and mouseY > classicDotButton.rect.top and mouseY < classicDotButton.rect.bottom:
                    dotValue = dotValue + clickValue
                if mouseX > classicClickUpgradeButton.rect.left and mouseX < classicClickUpgradeButton.rect.right and mouseY > classicClickUpgradeButton.rect.top and mouseY < classicClickUpgradeButton.rect.bottom:
                    if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                        clickValue = (clickValue + 1) * (prestigeValue + 1)
                        clickUpgradeValue = clickUpgradeValue + 1
                if mouseX > classicPrestigeButton.rect.left and mouseX < classicPrestigeButton.rect.right and mouseY > classicPrestigeButton.rect.top and mouseY < classicPrestigeButton.rect.bottom:
                    if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                        prestigeValue = prestigeValue + 1
                        dotValue = 0
                        clickValue = 1
                        clickUpgradeValue = 0
                if mouseX > classicStagePrestigeButton.rect.left and mouseX < classicStagePrestigeButton.rect.right and mouseY > classicStagePrestigeButton.rect.top and mouseY < classicStagePrestigeButton.rect.bottom:
                    if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                        stageValue = stageValue + 1
                        prestigeValue = 0
                        dotValue = 0
                        clickValue = 1
                        clickUpgradeValue = 0
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    ms.showinfo("Statistics" , statistics)
            if event.type == IDLEDOTGAIN:
                if stageValue > 1:
                    dotValue = dotValue + clickValue
            if event.type == IDLEDPCGAIN:
                if stageValue > 2:
                    clickValue = round(clickValue * 1.5)
            if event.type == IDLEUPGRADE:
                if stageValue > 3:
                    if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                        clickValue = (clickValue + 1) * (prestigeValue + 1)
                        clickUpgradeValue = clickUpgradeValue + 1
            if event.type == IDLEPRESTIGE:
                if stageValue > 4:
                    if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                        prestigeValue = prestigeValue + 1
                        dotValue = 0
                        clickValue = 1
                        clickUpgradeValue = 0
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
            ms.showinfo("Stage 3" , "You should have gotten the gist by now. Last time, Idle Dot Gain was implemented. Now, something else will be automated. See you in Stage 4.")
        if stageValue > 3 and stageFourMessage == False:
            stageFourMessage = True
            ms.showinfo("Stage 4" , "You have progressed pretty far into the game by now. In Stage 3, Idle DPC Gain was added. As promised previously, something else will be automated. If you make it to Stage 5, see you there.")
        if stageValue > 4 and stageFiveMessage == False:
            stageFiveMessage = True
            ms.showinfo("Stage 5" , "By now, you must have guessed what will be automated next. The next time I see you, there will be something different...")
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
        mouseX , mouseY = py.mouse.get_pos()
        upgradeRequirement = (((10 ** (clickUpgradeValue + 2)) * stageValue) + 1) - dotValue
        prestigeRequirement = ((15000 * ((prestigeValue + 1) ** prestigeValue)) + 1) - dotValue
        stagePrestigeRequirement = [(9 ** stageValue + 1) - prestigeValue , int((((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75) + 1) - dotValue)]
        dotCount = append(dotValue , "Dot" , "Dots" , True)
        clickCount = append(clickValue , "DPC" , "DPC" , True)
        stageCount = append("Stage" , stageValue , stageValue , False)
        clickUpgradeCount = append(clickUpgradeValue , "Click Upgrade" , "Click Upgrades" , True)
        prestigeCount = append(prestigeValue , "Prestige" , "Prestiges" , True)
        upgradeRequirementCount = append(upgradeRequirement , "More Dot Needed For The Next Upgrade" , "More Dots Needed For The Next Upgrade" , True)
        prestigeRequirementCount = append(prestigeRequirement , "More Dot Needed For The Next Prestige" , "More Dots Needed For The Next Prestige" , True)
        stagePrestigeRequirementCount = append(stagePrestigeRequirement[0] , "More Prestige and " , "More Prestiges and " , True) + append(stagePrestigeRequirement[1] , "More Dot Needed For The Next Stage Prestige" , "More Dots Needed For The Next Stage Prestige" , True) 
        classicDotCounter = Text(dotCount , 410 , 20 , (255 , 255 , 255) , 25)
        yinYangDotCounter = yinYang(classicDotCounter , False)
        statistics = dotCount + "\n" + clickCount + "\n" + clickUpgradeCount + "\n" + stageCount + "\n" + upgradeRequirementCount + "\n" + prestigeRequirementCount + "\n" + stagePrestigeRequirementCount
        if theme == "Classic":
            screen.blit(classicDotButton.surface , classicDotButton.rect)
        elif theme == "Yin Yang":
            screen.blit(yinYangDotButton.surface , yinYangDotButton.rect)
        if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
            screen.blit(classicClickUpgradeButton.surface , classicClickUpgradeButton.rect)
        if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
            screen.blit(classicPrestigeButton.surface , classicPrestigeButton.rect)
        if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
            screen.blit(classicStagePrestigeButton.surface , classicStagePrestigeButton.rect)
        if theme == "Classic":
            screen.blit(classicDotCounter.surface , classicDotCounter.rect)
        elif theme == "Yin Yang":
            screen.blit(yinYangDotCounter.surface , yinYangDotCounter.rect)
        py.display.flip()
py.quit()
