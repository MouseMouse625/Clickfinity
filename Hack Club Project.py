import pygame as py
from tkinter import messagebox as ms
py.init()
py.mixer.init()
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
prestigeValue = 0
prestigeCount = append(prestigeValue , "Prestige" , "Prestiges" , True)
stageValue = 1
stageCount = append("Stage" , stageValue , stageValue , False)
upgradeRequirement = (((10 ** (clickUpgradeValue + 2)) * stageValue) + 1) - dotValue
upgradeRequirementCount = append(upgradeRequirement , "More Dot Needed For The Next Upgrade" , "More Dots Needed For The Next Upgrade" , True)
prestigeRequirement = ((15000 * ((prestigeValue + 1) ** prestigeValue)) + 1) - dotValue
prestigeRequirementCount = append(prestigeRequirement , "More Dot Needed For The Next Prestige" , "More Dots Needed For The Next Prestige" , True)
stagePrestigeRequirement = [(9 ** stageValue + 1) - prestigeValue , int((((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75) + 1) - dotValue)]
stagePrestigeRequirementCount = str(append(stagePrestigeRequirement[0] , "More Prestige and " , "More Prestiges and " , True)) + str(append(stagePrestigeRequirement[1] , "More Dot Needed For The Next Stage Prestige" , "More Dots Needed For The Next Stage Prestige" , True))
sfxBool = True
welcomeMessage = False
settingsMessage = False
themesMessage = False
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
py.time.set_timer(IDLEDOTGAIN , 50)
py.time.set_timer(IDLEDPCGAIN , 500)
py.time.set_timer(IDLEUPGRADE , 10)
py.time.set_timer(IDLEPRESTIGE , 10)
classicDotButton = Button(30 , 30 , 250 , 190 , (0 , 200 , 255))
classicClickUpgradeButton = Button(30 , 30 , 250 , 230 , (200 , 255 , 0))
classicPrestigeButton = Button(30 , 30 , 250 , 270 , (255 , 0 , 0))
classicStagePrestigeButton = Button(30 , 30 , 250 , 310 , (0 , 255 , 20))
classicStartButton = Button(110 , 60 , 250 , 220 , (0 , 200 , 255))
classicThemesButton = Button(105 , 30 , 250 , 233 , (0 , 200 , 255))
classicInvertedButton = Button(138 , 38 , 250 , 130 , (0 , 200 , 255))
classicInvertedishButton = Button(170 , 38 , 250 , 170 , (0 , 200 , 255))
classicYangYinButton = Button(138 , 38 , 250 , 210 , (0 , 200 , 255))
classicClassicButton = Button(110 , 38 , 250 , 250 , (0 , 200 , 255))
classicYinYangButton = Button(138 , 38 , 250 , 290 , (0 , 200 , 255))
classicClassicishButton = Button(160 , 38 , 250 , 330 , (0 , 200 , 255))
classicAbyssButton = Button(160 , 38 , 250 , 370 , (0 , 200 , 255))
classicBackButton = Button(78 , 33  , 55 , 35 , (0 , 200 , 255))
classicSettingsButton = Button(110 , 30 , 250 , 270 , (0 , 200 , 255))
classicFactoryResetButton = Button(180 , 30 , 250 , 267 , (0 , 200 , 255))
classicInvertedButtonText = Text("Inverted" , 250 , 130 , (255 , 255 , 255) , 30)
classicInvertedishButtonText = Text("Invertedish" , 250 , 170 , (255 , 255 , 255) , 30)
classicYangYinButtonText = Text("Yang Yin" , 250 , 210 , (255 , 255 , 255) , 30)
classicClassicButtonText = Text("Classic" , 250 , 250 , (255 , 255 , 255) , 30)
classicYinYangButtonText = Text("Yin Yang" , 250 , 290 , (255 , 255 , 255) , 30)
classicClassicishButtonText = Text("Classicish" , 250 , 330 , (255 , 255 , 255) , 30)
classicAbyssButtonText = Text("Abyss" , 250 , 370 , (255 , 255 , 255) , 30)
classicBackButtonText = Text("Back" , 55 , 35 , (255 , 255 , 255) , 30)
classicStartButtonText = Text("Play" , 250 , 218 , (255 , 255 , 255) , 50)
classicThemesButtonText = Text("Themes" , 250 , 233 , (255 , 255 , 255) , 25)
classicSettingsButtonText = Text("Settings" , 250 , 270 , (255 , 255 , 255) , 25)
classicFactoryResetButtonText = Text("Factory Reset" , 250 , 267 , (255 , 255 , 255) , 25)
classicDotCounter = Text(dotCount , 410 , 35 , (255 , 255 , 255) , 25)
classicMenuObjects = py.sprite.Group()
classicSettingsObjects = py.sprite.Group()
classicThemesObjects = py.sprite.Group()
classicGameObjects = py.sprite.Group()
classicMenuObjects.add(classicStartButton , classicSettingsButton , classicStartButtonText , classicSettingsButtonText)
classicSettingsObjects.add(classicThemesButton , classicThemesButtonText , classicBackButton , classicBackButtonText , classicFactoryResetButton , classicFactoryResetButtonText)
classicThemesObjects.add(classicClassicButton , classicYinYangButton , classicYangYinButton , classicClassicButtonText , classicYinYangButtonText , classicYangYinButtonText , classicInvertedButton , classicInvertedButtonText , classicInvertedishButton , classicInvertedishButtonText , classicClassicishButton , classicClassicishButtonText , classicAbyssButton , classicAbyssButtonText , classicBackButton , classicBackButtonText)
classicGameObjects.add(classicDotButton , classicDotCounter , classicBackButton , classicBackButtonText)
yinYangDotButton = yinYang(classicDotButton , False)
yinYangClickUpgradeButton = yinYang(classicClickUpgradeButton , False)
yinYangPrestigeButton = yinYang(classicPrestigeButton , False)
yinYangStagePrestigeButton = yinYang(classicStagePrestigeButton , False)
yinYangStartButton = yinYang(classicStartButton , False)
yinYangThemesButton = yinYang(classicThemesButton , False)
yinYangSettingsButton = yinYang(classicSettingsButton , False)
yinYangInvertedButton = yinYang(classicInvertedButton , False)
yinYangInvertedishButton = yinYang(classicInvertedishButton , False)
yinYangYangYinButton = yinYang(classicYangYinButton , False)
yinYangClassicButton = yinYang(classicClassicButton , False)
yinYangYinYangButton = yinYang(classicYinYangButton , False)
yinYangClassicishButton = yinYang(classicClassicishButton , False)
yinYangFactoryResetButton = yinYang(classicFactoryResetButton , False)
yinYangAbyssButton = yinYang(classicAbyssButton , False)
yinYangBackButton = yinYang(classicBackButton , False)
yinYangInvertedButtonText = yinYang(classicInvertedButtonText , True)
yinYangInvertedishButtonText = yinYang(classicInvertedishButtonText , True)
yinYangYangYinButtonText = yinYang(classicYangYinButtonText , True)
yinYangClassicButtonText = yinYang(classicClassicButtonText , True)
yinYangYinYangButtonText = yinYang(classicYinYangButtonText , True)
yinYangClassicishButtonText = yinYang(classicClassicishButtonText , True)
yinYangFactoryResetButtonText = yinYang(classicFactoryResetButtonText , True)
yinYangAbyssButtonText = yinYang(classicAbyssButtonText , True)
yinYangBackButtonText = yinYang(classicBackButtonText , True)
yinYangThemesButtonText = yinYang(classicThemesButtonText , True)
yinYangStartButtonText = yinYang(classicStartButtonText , True)
yinYangSettingsButtonText = yinYang(classicSettingsButtonText , True)
yinYangMenuObjects = py.sprite.Group()
yinYangSettingsObjects = py.sprite.Group()
yinYangThemesObjects = py.sprite.Group()
yinYangGameObjects = py.sprite.Group()
yinYangMenuObjects.add(yinYangStartButton , yinYangSettingsButton , yinYangSettingsButtonText , yinYangStartButtonText)
yinYangSettingsObjects.add(yinYangThemesButton , yinYangThemesButtonText , yinYangBackButton , yinYangBackButtonText , yinYangFactoryResetButton , yinYangFactoryResetButtonText)
yinYangThemesObjects.add(yinYangClassicButton , yinYangClassicButtonText , yinYangYangYinButton , yinYangYangYinButtonText , yinYangYinYangButton , yinYangYinYangButtonText , yinYangBackButton , yinYangBackButtonText , yinYangInvertedButton , yinYangInvertedButtonText , yinYangInvertedishButton , yinYangInvertedishButtonText , yinYangClassicishButton , yinYangClassicishButtonText , yinYangAbyssButton , yinYangAbyssButtonText)
yinYangGameObjects.add(yinYangDotButton , classicDotCounter , yinYangBackButton , yinYangBackButtonText)
yangYinDotButton = yinYang(classicDotButton , True)
yangYinClickUpgradeButton = yinYang(classicClickUpgradeButton , True)
yangYinPrestigeButton = yinYang(classicPrestigeButton , True)
yangYinStagePrestigeButton = yinYang(classicStagePrestigeButton , True)
yangYinStartButton = yinYang(classicStartButton , True)
yangYinThemesButton = yinYang(classicThemesButton , True)
yangYinInvertedButton = yinYang(classicInvertedButton , True)
yangYinInvertedishButton = yinYang(classicInvertedishButton , True)
yangYinYangYinButton = yinYang(classicYangYinButton , True)
yangYinClassicButton = yinYang(classicClassicButton , True)
yangYinYinYangButton = yinYang(classicYinYangButton , True)
yangYinClassicishButton = yinYang(classicClassicishButton , True)
yangYinFactoryResetButton = yinYang(classicFactoryResetButton , True)
yangYinAbyssButton = yinYang(classicAbyssButton , True)
yangYinBackButton = yinYang(classicBackButton , True)
yangYinSettingsButton = yinYang(classicSettingsButton , True)
yangYinDotCounter = yinYang(classicDotCounter , True)
yangYinMenuObjects = py.sprite.Group()
yangYinSettingsObjects = py.sprite.Group()
yangYinThemesObjects = py.sprite.Group()
yangYinGameObjects = py.sprite.Group()
yangYinMenuObjects.add(yangYinStartButton , yangYinSettingsButton , classicSettingsButtonText , classicStartButtonText)
yangYinSettingsObjects.add(yangYinThemesButton , classicThemesButtonText , yangYinBackButton , classicBackButtonText , yangYinFactoryResetButton , classicFactoryResetButtonText)
yangYinThemesObjects.add(yangYinClassicButton , classicClassicButtonText , yangYinYinYangButton , classicYinYangButtonText , yangYinYangYinButton , classicYangYinButtonText , yangYinBackButton , classicBackButtonText , yangYinInvertedButton , classicInvertedButtonText , yangYinInvertedishButton , classicInvertedishButtonText , yangYinClassicishButton , classicClassicishButtonText , yangYinAbyssButton , classicAbyssButtonText)
yangYinGameObjects.add(yangYinDotButton , yangYinDotCounter , yangYinBackButton , classicBackButtonText)
classicishMenuObjects = py.sprite.Group()
classicishSettingsObjects = py.sprite.Group()
classicishThemesObjects = py.sprite.Group()
classicishGameObjects = py.sprite.Group()
classicishMenuObjects.add(classicStartButton , classicSettingsButton , yinYangStartButtonText , yinYangSettingsButtonText)
classicishSettingsObjects.add(classicThemesButton , yinYangThemesButtonText , classicBackButton , yinYangBackButtonText , classicFactoryResetButton , yinYangFactoryResetButtonText)
classicishThemesObjects.add(classicClassicButton , classicYinYangButton , classicYangYinButton , yinYangClassicButtonText , yinYangYinYangButtonText , yinYangYangYinButtonText , classicBackButton , yinYangBackButtonText , classicInvertedButton , yinYangInvertedButtonText , classicInvertedishButton , yinYangInvertedishButtonText , classicClassicishButton , yinYangClassicishButtonText , classicAbyssButton , yinYangAbyssButtonText)
classicishGameObjects.add(classicDotButton , yangYinDotCounter , classicBackButton , yinYangBackButtonText)
invertedishDotButton = Button(30 , 30 , 250 , 190 , (255 , 55 , 0))
invertedishClickUpgradeButton = Button(30 , 30 , 250 , 230 , (55 , 0 , 255))
invertedishPrestigeButton = Button(30 , 30 , 250 , 270 , (0 , 255 , 255))
invertedishStagePrestigeButton = Button(30 , 30 , 250 , 310 , (255 , 0 , 235))
invertedishStartButton = Button(110 , 60 , 250 , 220 , (255 , 55 , 0))
invertedishThemesButton = Button(105 , 30 , 250 , 233 , (255 , 55 , 0))
invertedishInvertedButton = Button(138 , 38 , 250 , 130 , (255 , 55 , 0))
invertedishInvertedishButton = Button(170 , 38 , 250 , 170 , (255 , 55 , 0))
invertedishFactoryResetButton = Button(180 , 30 , 250 , 267 , (255 , 55 , 0))
invertedishYangYinButton = Button(138 , 38 , 250 , 210 , (255 , 55 , 0))
invertedishClassicButton = Button(110 , 38 , 250 , 250 , (255 , 55 , 0))
invertedishYinYangButton = Button(138 , 38 , 250 , 290 , (255 , 55 , 0))
invertedishClassicishButton = Button(160 , 38 , 250 , 330 , (255 , 55 , 0))
invertedishAbyssButton = Button(160 , 38 , 250 , 370 , (255 , 55 , 0))
invertedishBackButton = Button(78 , 33  , 55 , 35 , (255 , 55 , 0))
invertedishSettingsButton = Button(110 , 30 , 250 , 270 , (255 , 55 , 0))
invertedishMenuObjects = py.sprite.Group()
invertedishSettingsObjects = py.sprite.Group()
invertedishThemesObjects = py.sprite.Group()
invertedishGameObjects = py.sprite.Group()
invertedishMenuObjects.add(invertedishStartButton , invertedishSettingsButton , classicStartButtonText , classicSettingsButtonText)
invertedishSettingsObjects.add(invertedishThemesButton , classicThemesButtonText , invertedishBackButton , classicBackButtonText , invertedishFactoryResetButton , classicFactoryResetButtonText)
invertedishThemesObjects.add(invertedishClassicButton , invertedishYinYangButton , invertedishYangYinButton , classicClassicButtonText , classicYinYangButtonText , classicYangYinButtonText , invertedishInvertedButton , classicInvertedButtonText , invertedishInvertedishButton , classicInvertedishButtonText , invertedishClassicishButton , classicClassicishButtonText , invertedishAbyssButton , classicAbyssButtonText , invertedishBackButton , classicBackButtonText)
invertedishGameObjects.add(invertedishDotButton , classicDotCounter , invertedishBackButton , classicBackButtonText)
invertedMenuObjects = py.sprite.Group()
invertedSettingsObjects = py.sprite.Group()
invertedThemesObjects = py.sprite.Group()
invertedGameObjects = py.sprite.Group()
invertedMenuObjects.add(invertedishStartButton , invertedishSettingsButton , yinYangStartButtonText , yinYangSettingsButtonText)
invertedSettingsObjects.add(invertedishThemesButton , yinYangThemesButtonText , invertedishBackButton , yinYangBackButtonText , invertedishFactoryResetButton , yinYangFactoryResetButtonText)
invertedThemesObjects.add(invertedishClassicButton , invertedishYinYangButton , invertedishYangYinButton , yinYangClassicButtonText , yinYangYinYangButtonText , yinYangYangYinButtonText , invertedishInvertedButton , yinYangInvertedButtonText , invertedishInvertedishButton , yinYangInvertedishButtonText , invertedishClassicishButton , yinYangClassicishButtonText , invertedishAbyssButton , yinYangAbyssButtonText , invertedishBackButton , yinYangBackButtonText)
invertedGameObjects.add(invertedishDotButton , yangYinDotCounter , invertedishBackButton , yinYangBackButtonText)
abyssMenuObjects = py.sprite.Group()
abyssSettingsObjects = py.sprite.Group()
abyssThemesObjects = py.sprite.Group()
abyssGameObjects = py.sprite.Group()
abyssMenuObjects.add(yangYinStartButton , yangYinSettingsButton , yinYangStartButtonText , yinYangSettingsButtonText)
abyssSettingsObjects.add(yangYinThemesButton , yinYangThemesButtonText , yangYinBackButton , yinYangBackButtonText , yangYinFactoryResetButton , yinYangFactoryResetButtonText)
abyssThemesObjects.add(yangYinClassicButton , yangYinYinYangButton , yangYinYangYinButton , yinYangClassicButtonText , yinYangYinYangButtonText , yinYangYangYinButtonText , yangYinInvertedButton , yinYangInvertedButtonText , yangYinInvertedishButton , yinYangInvertedishButtonText , yangYinClassicishButton , yinYangClassicishButtonText , yangYinAbyssButton , yinYangAbyssButtonText , yangYinBackButton , yinYangBackButtonText)
abyssGameObjects.add(yangYinDotButton , yangYinDotCounter , yangYinBackButton , yinYangBackButtonText)
programRunning = True
while programRunning:
    mouseX , mouseY = py.mouse.get_pos()
    if level == "Menu":
        if welcomeMessage == False:
            welcomeMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Welcome" , "Hello! This is the Menu. You can select your theme first, or go straight into the gameplay. See you there!")
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Sound Effects" , "There are a lot of sound effects in the game, so just a quick heads up that you can press the Escape key to toggle the sound effects on and off.")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicStartButton.rect.left and mouseX < classicStartButton.rect.right and mouseY > classicStartButton.rect.top and mouseY < classicStartButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Game"
            if mouseX > classicSettingsButton.rect.left and mouseX < classicSettingsButton.rect.right and mouseY > classicSettingsButton.rect.top and mouseY < classicSettingsButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Settings"
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                    elif sfxBool == False:
                        sfxBool = True
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicMenuObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangMenuObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            for object in yangYinMenuObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            for object in classicishMenuObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            for object in invertedishMenuObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            for object in invertedMenuObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            for object in abyssMenuObjects:
                screen.blit(object.surface , object.rect)
        py.display.flip()
    elif level == "Settings":
        if settingsMessage == False:
            settingsMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Settings" , "Hello! This is Settings. You can select your theme first, and go into the gameplay. See you there!")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicThemesButton.rect.left and mouseX < classicThemesButton.rect.right and mouseY > classicThemesButton.rect.top and mouseY < classicThemesButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Themes"
            if mouseX > classicFactoryResetButton.rect.left and mouseX < classicFactoryResetButton.rect.right and mouseY > classicFactoryResetButton.rect.top and mouseY < classicFactoryResetButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    choice = ms.askquestion("Factory Reset" , "Are you sure you want to initiate a factory reset? This resets every stat in game, thus making it like you just started playing.")
                    if choice == "yes":
                        if sfxBool == True:
                            py.mixer.music.load("Message.wav")
                            py.mixer.music.set_volume(0.4)
                            py.mixer.music.play()
                        secondChoice = ms.askquestion("Factory Reset" , "You have chosen wrongly. I'll give you a second chance. Do you want to cancel?")
                        if secondChoice == "no":
                            if sfxBool == True:
                                py.mixer.music.load("Message.wav")
                                py.mixer.music.set_volume(0.4)
                                py.mixer.music.play()
                            ms.showinfo("Factory Reset" , "Sadly, you will now start all over again. This is why I didn't mention the second option in the Settings.")
                            dotValue = 0
                            clickValue = 1
                            clickUpgradeValue = 0
                            prestigeValue = 0
                            stageValue = 1
                        else:
                            if sfxBool == True:
                                py.mixer.music.load("Message.wav")
                                py.mixer.music.set_volume(0.4)
                                py.mixer.music.play()
                            ms.showinfo("Cancellation" , "That was a good choice you made at the last second.")
                    else:
                        if sfxBool == True:
                            py.mixer.music.load("Message.wav")
                            py.mixer.music.set_volume(0.4)
                            py.mixer.music.play()
                        ms.showinfo("Cancellation" , "Good choice.")
            if mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Menu"
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                    elif sfxBool == False:
                        sfxBool = True
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicSettingsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangSettingsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            for object in yangYinSettingsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            for object in classicishSettingsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            for object in invertedishSettingsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            for object in invertedSettingsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            for object in abyssSettingsObjects:
                screen.blit(object.surface , object.rect)
        py.display.flip()
    elif level == "Themes":
        if themesMessage == False:
            themesMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Themes" , "Here you can find a few themes. The current theme, which is the default theme is Classic. Once you have chosen, you can go into the gameplay.")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicClassicButton.rect.left and mouseX < classicClassicButton.rect.right and mouseY > classicClassicButton.rect.top and mouseY < classicClassicButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Classic"
            if mouseX > classicYinYangButton.rect.left and mouseX < classicYinYangButton.rect.right and mouseY > classicYinYangButton.rect.top and mouseY < classicYinYangButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Yin Yang"
            if mouseX > classicYangYinButton.rect.left and mouseX < classicYangYinButton.rect.right and mouseY > classicYangYinButton.rect.top and mouseY < classicYangYinButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Yang Yin"
            if mouseX > classicClassicishButton.rect.left and mouseX < classicClassicishButton.rect.right and mouseY > classicClassicishButton.rect.top and mouseY < classicClassicishButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Classicish"
            if mouseX > classicInvertedishButton.rect.left and mouseX < classicInvertedishButton.rect.right and mouseY > classicInvertedishButton.rect.top and mouseY < classicInvertedishButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Invertedish"
            if mouseX > classicInvertedButton.rect.left and mouseX < classicInvertedButton.rect.right and mouseY > classicInvertedButton.rect.top and mouseY < classicInvertedButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Inverted"
            if mouseX > classicAbyssButton.rect.left and mouseX < classicAbyssButton.rect.right and mouseY > classicAbyssButton.rect.top and mouseY < classicAbyssButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Abyss"
            if mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Settings"
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                    elif sfxBool == False:
                        sfxBool = True
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicThemesObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangThemesObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            for object in yangYinThemesObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            for object in classicishThemesObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            for object in invertedishThemesObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            for object in invertedThemesObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            for object in abyssThemesObjects:
                screen.blit(object.surface , object.rect)
        py.display.flip()
    elif level == "Game":
        if tutorialMessage == False:
            tutorialMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Tutorial" , "Hello! This is a minimalistic cookie clicker made for the Hack Club Arcade.")
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Tutorial" , "For now, you have to collect as many dots as possible.")
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Tutorial" , "That blue button you'll see shortly increments the amount of dots you have by 1 every time you press it.")
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Info" , "You can navigate to the Themes area again to change your theme once more.")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicDotButton.rect.left and mouseX < classicDotButton.rect.right and mouseY > classicDotButton.rect.top and mouseY < classicDotButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    dotValue = dotValue + clickValue
            if mouseX > classicClickUpgradeButton.rect.left and mouseX < classicClickUpgradeButton.rect.right and mouseY > classicClickUpgradeButton.rect.top and mouseY < classicClickUpgradeButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                        clickValue = (clickValue + 1) * (prestigeValue + 1)
                        clickUpgradeValue = clickUpgradeValue + 1
            if mouseX > classicPrestigeButton.rect.left and mouseX < classicPrestigeButton.rect.right and mouseY > classicPrestigeButton.rect.top and mouseY < classicPrestigeButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                        prestigeValue = prestigeValue + 1
                        dotValue = 0
                        clickValue = 1
                        clickUpgradeValue = 0
            if mouseX > classicStagePrestigeButton.rect.left and mouseX < classicStagePrestigeButton.rect.right and mouseY > classicStagePrestigeButton.rect.top and mouseY < classicStagePrestigeButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                        stageValue = stageValue + 1
                        prestigeValue = 0
                        dotValue = 0
                        clickValue = 1
                        clickUpgradeValue = 0
            if mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_system_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Menu"
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                    elif sfxBool == False:
                        sfxBool = True
                if event.key == py.K_SPACE:
                    if sfxBool == True:
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
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
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Starting Off" , "You've gained your first dot. You can earn more, and once you have a substantial amount, you'll get another message like this one.")
        if dotValue > 100 and firstUpgradeMessage == False:
            firstUpgradeMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Upgrades" , "You've reached your first upgrade. When you press that yellow button that you will see shortly, your Dots Per Click (DPC) value will increment by one. This changes how many dots you earn per click.")
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Statistics" , "To see some statistics, you can press the Space key on your keyboard.")
        if dotValue > 11250 and firstPrestigeMessage == False:
            firstPrestigeMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Prestiges" , "You have reached the point where you can undergo your first prestige. When you press the red button that you will see shortly, you will prestige. This means that all of your statistics, including your dots and DPC will be reset to 0 and 1 respectively. Things like how many times you have prestiged will be incremented by one of course, and your stage (you'll learn about that later) will stay the same. Although this seems purely negative, the rate at which your DPC increments will be vastly different (positively), and you will reach more and more dot counts.")
        if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75) and firstStagePrestigeMessage == False:
            firstStagePrestigeMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Stage Prestiges" , "After a long time, you have reached your first stage prestige. Stage prestiges reset everything that prestiges do, as well as your prestige count. On the other hand, your stage increments by one. A stage prestige always automates some part of the game that hasn't been automated before, eventualy allowing full idle gameplay. You can stage prestige by pressing the green button that you will se shortly. There is a suprise in Stage 2.")
        if stageValue > 1 and stageTwoMessage == False:
            stageTwoMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Stage 2" , "This is the second Stage. As promised, once you progress after reading this message, a part of the game will be automated. Good luck.")
        if stageValue > 2 and stageThreeMessage == False:
            stageThreeMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Stage 3" , "You should have gotten the gist by now. Last time, Idle Dot Gain was implemented. Now, something else will be automated. See you in Stage 4.")
        if stageValue > 3 and stageFourMessage == False:
            stageFourMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Stage 4" , "You have progressed pretty far into the game by now. In Stage 3, Idle DPC Gain was added. As promised previously, something else will be automated. If you make it to Stage 5, see you there.")
        if stageValue > 4 and stageFiveMessage == False:
            stageFiveMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Stage 5" , "By now, you must have guessed what will be automated next. The next time I see you, there will be something different...")
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            classicGameObjects.remove(classicDotCounter)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            yinYangGameObjects.remove(classicDotCounter)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            yangYinGameObjects.remove(yangYinDotCounter)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            classicishGameObjects.remove(yangYinDotCounter)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            invertedishGameObjects.remove(classicDotCounter)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            invertedGameObjects.remove(yangYinDotCounter)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            abyssGameObjects.remove(yangYinDotCounter)
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
        classicDotCounter = Text(dotCount , 410 , 35 , (255 , 255 , 255) , 25)
        yangYinDotCounter = yinYang(classicDotCounter , True)
        statistics = dotCount + "\n" + clickCount + "\n" + clickUpgradeCount + "\n" + stageCount + "\n" + upgradeRequirementCount + "\n" + prestigeRequirementCount + "\n" + stagePrestigeRequirementCount
        if theme == "Classic":
            classicGameObjects.add(classicDotCounter)
            for object in classicGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(classicClickUpgradeButton.surface , classicClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(classicPrestigeButton.surface , classicPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(classicStagePrestigeButton.surface , classicStagePrestigeButton.rect)
        elif theme == "Yin Yang":
            yinYangGameObjects.add(classicDotCounter)
            for object in yinYangGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(yinYangClickUpgradeButton.surface , yinYangClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(yinYangPrestigeButton.surface , yinYangPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(yinYangStagePrestigeButton.surface , yinYangStagePrestigeButton.rect)
        elif theme == "Yang Yin":
            yangYinGameObjects.add(yangYinDotCounter)
            for object in yangYinGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(yangYinClickUpgradeButton.surface , yangYinClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(yangYinPrestigeButton.surface , yangYinPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(yangYinStagePrestigeButton.surface , yangYinStagePrestigeButton.rect)
        elif theme == "Classicish":
            classicishGameObjects.add(yangYinDotCounter)
            for object in classicishGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(classicClickUpgradeButton.surface , classicClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(classicPrestigeButton.surface , classicPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(classicStagePrestigeButton.surface , classicStagePrestigeButton.rect)
        elif theme == "Invertedish":
            invertedishGameObjects.add(classicDotCounter)
            for object in invertedishGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(invertedishClickUpgradeButton.surface , invertedishClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(invertedishPrestigeButton.surface , invertedishPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(invertedishStagePrestigeButton.surface , invertedishStagePrestigeButton.rect)
        elif theme == "Inverted":
            invertedGameObjects.add(yangYinDotCounter)
            for object in invertedGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(invertedishClickUpgradeButton.surface , invertedishClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(invertedishPrestigeButton.surface , invertedishPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(invertedishStagePrestigeButton.surface , invertedishStagePrestigeButton.rect)
        elif theme == "Abyss":
            abyssGameObjects.add(yangYinDotCounter)
            for object in abyssGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(yangYinClickUpgradeButton.surface , yangYinClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(yangYinPrestigeButton.surface , yangYinPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(yangYinStagePrestigeButton.surface , yangYinStagePrestigeButton.rect)
        py.display.flip()
py.quit()
