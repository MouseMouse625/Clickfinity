import pygame as py
from tkinter import messagebox as ms
import random as rd
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
level = "Disco"
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
flashingBool = False
welcomeMessage = False
settingsMessage = False
themesMessage = False
tutorialMessage = False
firstDotMessage = False
firstUpgradeMessage = False
firstPrestigeMessage = False
firstStagePrestigeMessage = False
creditsMessage = False
stageTwoMessage = False
stageThreeMessage = False
stageFourMessage = False
stageFiveMessage = False
easterEggLevelOneMessage = False
easterEggLevelTwoMessage = False
easterEggLevelThreeMessage = False
easterEggLevelFourMessage = False
discoMessage = False
discoDuration = 250
statistics = dotCount + "\n" + clickCount + "\n" + clickUpgradeCount + "\n" + stageCount + "\n" + upgradeRequirementCount + "\n" + prestigeRequirementCount + "\n" + stagePrestigeRequirementCount
screen = py.display.set_mode((screenWidth , screenHeight))
py.display.set_icon(py.image.load("Window Icon.png"))
py.display.set_caption("Hack Club Project")
IDLEDOTGAIN = py.USEREVENT + 1
IDLEDPCGAIN = py.USEREVENT + 2
IDLEUPGRADE = py.USEREVENT + 3
IDLEPRESTIGE = py.USEREVENT + 4
SCREENCOLOURCHANGE = py.USEREVENT + 5
py.time.set_timer(IDLEDOTGAIN , 50)
py.time.set_timer(IDLEDPCGAIN , 500)
py.time.set_timer(IDLEUPGRADE , 10)
py.time.set_timer(IDLEPRESTIGE , 10)
py.time.set_timer(SCREENCOLOURCHANGE , discoDuration)
classicDotButton = Button(30 , 30 , 250 , 190 , (0 , 200 , 255))
classicClickUpgradeButton = Button(30 , 30 , 250 , 230 , (200 , 255 , 0))
classicPrestigeButton = Button(30 , 30 , 250 , 270 , (255 , 0 , 0))
classicStagePrestigeButton = Button(30 , 30 , 250 , 310 , (0 , 255 , 20))
classicStartButton = Button(110 , 60 , 250 , 220 , (0 , 200 , 255))
classicThemesButton = Button(105 , 30 , 250 , 250 , (0 , 200 , 255))
classicInvertedButton = Button(138 , 38 , 250 , 130 , (0 , 200 , 255))
classicInvertedishButton = Button(170 , 38 , 250 , 170 , (0 , 200 , 255))
classicYangYinButton = Button(138 , 38 , 250 , 210 , (0 , 200 , 255))
classicClassicButton = Button(110 , 38 , 250 , 250 , (0 , 200 , 255))
classicYinYangButton = Button(138 , 38 , 250 , 290 , (0 , 200 , 255))
classicClassicishButton = Button(160 , 38 , 250 , 330 , (0 , 200 , 255))
classicEasterEggLvlOne = Button(5 , 5 , 5 , 495 , (0 , 200 , 255))
classicEasterEggLvlTwo = Button(5 , 5 , 250 , 250 , (255 , 0 , 255))
classicEasterEggLvlThree = Button(2 , 2 , 76 , 236 , (255 , 0 , 255))
classicEasterEggLvlFour = Button(1 , 1 , 347 , 378 , (255 , 0 , 255))
classicAbyssButton = Button(160 , 38 , 250 , 370 , (0 , 200 , 255))
classicBackButton = Button(78 , 33  , 55 , 35 , (0 , 200 , 255))
classicSettingsButton = Button(110 , 30 , 250 , 270 , (0 , 200 , 255))
classicCreditsButton = Button(100 , 30 , 250 , 215 , (0 , 200 , 255))
classicFactoryResetButton = Button(180 , 30 , 250 , 285 , (0 , 200 , 255))
classicInvertedButtonText = Text("Inverted" , 250 , 130 , (255 , 255 , 255) , 30)
classicInvertedishButtonText = Text("Invertedish" , 250 , 170 , (255 , 255 , 255) , 30)
classicYangYinButtonText = Text("Yang Yin" , 250 , 210 , (255 , 255 , 255) , 30)
classicClassicButtonText = Text("Classic" , 250 , 250 , (255 , 255 , 255) , 30)
classicYinYangButtonText = Text("Yin Yang" , 250 , 290 , (255 , 255 , 255) , 30)
classicClassicishButtonText = Text("Classicish" , 250 , 330 , (255 , 255 , 255) , 30)
classicAbyssButtonText = Text("Abyss" , 250 , 370 , (255 , 255 , 255) , 30)
classicBackButtonText = Text("Back" , 55 , 35 , (255 , 255 , 255) , 30)
classicStartButtonText = Text("Play" , 250 , 218 , (255 , 255 , 255) , 50)
classicThemesButtonText = Text("Themes" , 250 , 250 , (255 , 255 , 255) , 25)
classicSettingsButtonText = Text("Settings" , 250 , 270 , (255 , 255 , 255) , 25)
classicFactoryResetButtonText = Text("Factory Reset" , 250 , 285 , (255 , 255 , 255) , 25)
classicCreditsButtonText = Text("Credits" , 250 , 215 , (255 , 255 , 255) , 25)
classicDotCounter = Text(dotCount , 410 , 35 , (255 , 255 , 255) , 25)
classicMenuObjects = py.sprite.Group()
classicSettingsObjects = py.sprite.Group()
classicThemesObjects = py.sprite.Group()
classicCreditsObjects = py.sprite.Group()
classicGameObjects = py.sprite.Group()
classicEasterEggLvlOneObjects = py.sprite.Group()
classicEasterEggLvlTwoObjects = py.sprite.Group()
classicEasterEggLvlThreeObjects = py.sprite.Group()
classicEasterEggLvlFourObjects = py.sprite.Group()
classicDiscoObjects = py.sprite.Group()
classicMenuObjects.add(classicStartButton , classicSettingsButton , classicStartButtonText , classicSettingsButtonText)
classicSettingsObjects.add(classicThemesButton , classicThemesButtonText , classicBackButton , classicBackButtonText , classicFactoryResetButton , classicFactoryResetButtonText , classicCreditsButton , classicCreditsButtonText)
classicThemesObjects.add(classicClassicButton , classicYinYangButton , classicYangYinButton , classicClassicButtonText , classicYinYangButtonText , classicYangYinButtonText , classicInvertedButton , classicInvertedButtonText , classicInvertedishButton , classicInvertedishButtonText , classicClassicishButton , classicClassicishButtonText , classicAbyssButton , classicAbyssButtonText , classicBackButton , classicBackButtonText)
classicGameObjects.add(classicDotButton , classicDotCounter , classicBackButton , classicBackButtonText)
classicCreditsObjects.add(classicBackButton , classicBackButtonText)
classicEasterEggLvlOneObjects.add(classicEasterEggLvlOne , classicBackButton , classicBackButtonText)
classicEasterEggLvlTwoObjects.add(classicEasterEggLvlTwo , classicBackButton , classicBackButtonText)
classicEasterEggLvlThreeObjects.add(classicEasterEggLvlThree , classicBackButton , classicBackButtonText)
classicEasterEggLvlFourObjects.add(classicEasterEggLvlFour , classicBackButton , classicBackButtonText)
classicDiscoObjects.add(classicBackButton , classicBackButtonText)
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
yinYangCreditsButton = yinYang(classicCreditsButton , False)
yinYangYinYangButton = yinYang(classicYinYangButton , False)
yinYangEasterEggLvlOne = yinYang(classicEasterEggLvlOne , False)
yinYangEasterEggLvlTwo = yinYang(classicEasterEggLvlTwo , True)
yinYangEasterEggLvlThree = yinYang(classicEasterEggLvlThree , True)
yinYangEasterEggLvlFour = yinYang(classicEasterEggLvlFour , True)
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
yinYangCreditsButtonText = yinYang(classicCreditsButtonText , True)
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
yinYangCreditsObjects = py.sprite.Group()
yinYangEasterEggLvlOneObjects = py.sprite.Group()
yinYangEasterEggLvlTwoObjects = py.sprite.Group()
yinYangEasterEggLvlThreeObjects = py.sprite.Group()
yinYangEasterEggLvlFourObjects = py.sprite.Group()
yinYangDiscoObjects = py.sprite.Group()
yinYangMenuObjects.add(yinYangStartButton , yinYangSettingsButton , yinYangSettingsButtonText , yinYangStartButtonText)
yinYangSettingsObjects.add(yinYangThemesButton , yinYangThemesButtonText , yinYangBackButton , yinYangBackButtonText , yinYangFactoryResetButton , yinYangFactoryResetButtonText , yinYangCreditsButton , yinYangCreditsButtonText)
yinYangThemesObjects.add(yinYangClassicButton , yinYangClassicButtonText , yinYangYangYinButton , yinYangYangYinButtonText , yinYangYinYangButton , yinYangYinYangButtonText , yinYangBackButton , yinYangBackButtonText , yinYangInvertedButton , yinYangInvertedButtonText , yinYangInvertedishButton , yinYangInvertedishButtonText , yinYangClassicishButton , yinYangClassicishButtonText , yinYangAbyssButton , yinYangAbyssButtonText)
yinYangGameObjects.add(yinYangDotButton , classicDotCounter , yinYangBackButton , yinYangBackButtonText)
yinYangCreditsObjects.add(yinYangBackButton , yinYangBackButtonText)
yinYangEasterEggLvlOneObjects.add(yinYangEasterEggLvlOne , yinYangBackButton , yinYangBackButtonText)
yinYangEasterEggLvlTwoObjects.add(yinYangEasterEggLvlTwo , yinYangBackButton , yinYangBackButtonText)
yinYangEasterEggLvlThreeObjects.add(yinYangEasterEggLvlThree , yinYangBackButton , yinYangBackButtonText)
yinYangEasterEggLvlFourObjects.add(yinYangEasterEggLvlFour , yinYangBackButton , yinYangBackButtonText)
yinYangDiscoObjects.add(yinYangBackButton , yinYangBackButtonText)
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
yangYinEasterEggLvlOne = yinYang(classicEasterEggLvlOne , True)
yangYinEasterEggLvlTwo = yinYang(classicEasterEggLvlTwo , False)
yangYinEasterEggLvlThree = yinYang(classicEasterEggLvlThree , False)
yangYinEasterEggLvlFour = yinYang(classicEasterEggLvlFour , False)
yangYinYinYangButton = yinYang(classicYinYangButton , True)
yangYinClassicishButton = yinYang(classicClassicishButton , True)
yangYinFactoryResetButton = yinYang(classicFactoryResetButton , True)
yangYinAbyssButton = yinYang(classicAbyssButton , True)
yangYinBackButton = yinYang(classicBackButton , True)
yangYinSettingsButton = yinYang(classicSettingsButton , True)
yangYinCreditsButton = yinYang(classicCreditsButton , True)
yangYinDotCounter = yinYang(classicDotCounter , True)
yangYinMenuObjects = py.sprite.Group()
yangYinSettingsObjects = py.sprite.Group()
yangYinThemesObjects = py.sprite.Group()
yangYinGameObjects = py.sprite.Group()
yangYinCreditsObjects = py.sprite.Group()
yangYinEasterEggLvlOneObjects = py.sprite.Group()
yangYinEasterEggLvlTwoObjects = py.sprite.Group()
yangYinEasterEggLvlThreeObjects = py.sprite.Group()
yangYinEasterEggLvlFourObjects = py.sprite.Group()
yangYinDiscoObjects = py.sprite.Group()
yangYinMenuObjects.add(yangYinStartButton , yangYinSettingsButton , classicSettingsButtonText , classicStartButtonText)
yangYinSettingsObjects.add(yangYinThemesButton , classicThemesButtonText , yangYinBackButton , classicBackButtonText , yangYinFactoryResetButton , classicFactoryResetButtonText , yangYinCreditsButton , classicCreditsButtonText)
yangYinThemesObjects.add(yangYinClassicButton , classicClassicButtonText , yangYinYinYangButton , classicYinYangButtonText , yangYinYangYinButton , classicYangYinButtonText , yangYinBackButton , classicBackButtonText , yangYinInvertedButton , classicInvertedButtonText , yangYinInvertedishButton , classicInvertedishButtonText , yangYinClassicishButton , classicClassicishButtonText , yangYinAbyssButton , classicAbyssButtonText)
yangYinGameObjects.add(yangYinDotButton , yangYinDotCounter , yangYinBackButton , classicBackButtonText)
yangYinCreditsObjects.add(yangYinBackButton , classicBackButtonText)
yangYinEasterEggLvlOneObjects.add(yangYinEasterEggLvlOne , yangYinBackButton , classicBackButtonText)
yangYinEasterEggLvlTwoObjects.add(yangYinEasterEggLvlTwo , yangYinBackButton , classicBackButtonText)
yangYinEasterEggLvlThreeObjects.add(yangYinEasterEggLvlThree , yangYinBackButton , classicBackButtonText)
yangYinEasterEggLvlFourObjects.add(yangYinEasterEggLvlFour , yangYinBackButton , classicBackButtonText)
yangYinDiscoObjects.add(yangYinBackButton , classicBackButtonText)
classicishMenuObjects = py.sprite.Group()
classicishSettingsObjects = py.sprite.Group()
classicishThemesObjects = py.sprite.Group()
classicishGameObjects = py.sprite.Group()
classicishCreditsObjects = py.sprite.Group()
classicishEasterEggLvlOneObjects = py.sprite.Group()
classicishEasterEggLvlTwoObjects = py.sprite.Group()
classicishEasterEggLvlThreeObjects = py.sprite.Group()
classicishEasterEggLvlFourObjects = py.sprite.Group()
classicishDiscoObjects = py.sprite.Group()
classicishMenuObjects.add(classicStartButton , classicSettingsButton , yinYangStartButtonText , yinYangSettingsButtonText)
classicishSettingsObjects.add(classicThemesButton , yinYangThemesButtonText , classicBackButton , yinYangBackButtonText , classicFactoryResetButton , yinYangFactoryResetButtonText , classicCreditsButton , yinYangCreditsButtonText)
classicishThemesObjects.add(classicClassicButton , classicYinYangButton , classicYangYinButton , yinYangClassicButtonText , yinYangYinYangButtonText , yinYangYangYinButtonText , classicBackButton , yinYangBackButtonText , classicInvertedButton , yinYangInvertedButtonText , classicInvertedishButton , yinYangInvertedishButtonText , classicClassicishButton , yinYangClassicishButtonText , classicAbyssButton , yinYangAbyssButtonText)
classicishGameObjects.add(classicDotButton , yangYinDotCounter , classicBackButton , yinYangBackButtonText)
classicishCreditsObjects.add(classicBackButton , yinYangBackButtonText)
classicishEasterEggLvlOneObjects.add(classicEasterEggLvlOne , classicBackButton , yinYangBackButtonText)
classicishEasterEggLvlTwoObjects.add(classicEasterEggLvlTwo , classicBackButton , yinYangBackButtonText)
classicishEasterEggLvlThreeObjects.add(classicEasterEggLvlThree , classicBackButton , yinYangBackButtonText)
classicishEasterEggLvlFourObjects.add(classicEasterEggLvlFour , classicBackButton , yinYangBackButtonText)
classicishDiscoObjects.add(classicBackButton , yinYangBackButtonText)
invertedishDotButton = Button(30 , 30 , 250 , 190 , (255 , 55 , 0))
invertedishClickUpgradeButton = Button(30 , 30 , 250 , 230 , (55 , 0 , 255))
invertedishPrestigeButton = Button(30 , 30 , 250 , 270 , (0 , 255 , 255))
invertedishStagePrestigeButton = Button(30 , 30 , 250 , 310 , (255 , 0 , 235))
invertedishStartButton = Button(110 , 60 , 250 , 220 , (255 , 55 , 0))
invertedishThemesButton = Button(105 , 30 , 250 , 250 , (255 , 55 , 0))
invertedishInvertedButton = Button(138 , 38 , 250 , 130 , (255 , 55 , 0))
invertedishInvertedishButton = Button(170 , 38 , 250 , 170 , (255 , 55 , 0))
invertedishFactoryResetButton = Button(180 , 30 , 250 , 285 , (255 , 55 , 0))
invertedCreditsButton = Button(138 , 30 , 250 , 215 , (255 , 55 , 0))
invertedishYangYinButton = Button(138 , 38 , 250 , 210 , (255 , 55 , 0))
invertedishClassicButton = Button(110 , 38 , 250 , 250 , (255 , 55 , 0))
invertedishEasterEggLvlOne = Button(5 , 5 , 5 , 495 , (255 , 55 , 0))
invertedishEasterEggLvlTwo = Button(5 , 5 , 250 , 250 , (0 , 255 , 0))
invertedishEasterEggLvlThree = Button(2 , 2 , 76 , 236 , (0 , 255 , 0))
invertedishEasterEggLvlFour = Button(1 , 1 , 347 , 378 , (0 , 255 , 0))
invertedishYinYangButton = Button(138 , 38 , 250 , 290 , (255 , 55 , 0))
invertedishClassicishButton = Button(160 , 38 , 250 , 330 , (255 , 55 , 0))
invertedishAbyssButton = Button(160 , 38 , 250 , 370 , (255 , 55 , 0))
invertedishBackButton = Button(78 , 33  , 55 , 35 , (255 , 55 , 0))
invertedishSettingsButton = Button(110 , 30 , 250 , 270 , (255 , 55 , 0))
invertedishMenuObjects = py.sprite.Group()
invertedishSettingsObjects = py.sprite.Group()
invertedishThemesObjects = py.sprite.Group()
invertedishGameObjects = py.sprite.Group()
invertedishCreditsObjects = py.sprite.Group()
invertedishEasterEggLvlOneObjects = py.sprite.Group()
invertedishEasterEggLvlTwoObjects = py.sprite.Group()
invertedishEasterEggLvlThreeObjects = py.sprite.Group()
invertedishEasterEggLvlFourObjects = py.sprite.Group()
invertedishDiscoObjects = py.sprite.Group()
invertedishMenuObjects.add(invertedishStartButton , invertedishSettingsButton , classicStartButtonText , classicSettingsButtonText)
invertedishSettingsObjects.add(invertedishThemesButton , classicThemesButtonText , invertedishBackButton , classicBackButtonText , invertedishFactoryResetButton , classicFactoryResetButtonText , invertedCreditsButton , classicCreditsButtonText)
invertedishThemesObjects.add(invertedishClassicButton , invertedishYinYangButton , invertedishYangYinButton , classicClassicButtonText , classicYinYangButtonText , classicYangYinButtonText , invertedishInvertedButton , classicInvertedButtonText , invertedishInvertedishButton , classicInvertedishButtonText , invertedishClassicishButton , classicClassicishButtonText , invertedishAbyssButton , classicAbyssButtonText , invertedishBackButton , classicBackButtonText)
invertedishGameObjects.add(invertedishDotButton , classicDotCounter , invertedishBackButton , classicBackButtonText)
invertedishCreditsObjects.add(invertedishBackButton , classicBackButtonText)
invertedishEasterEggLvlOneObjects.add(invertedishEasterEggLvlOne , invertedishBackButton , classicBackButtonText)
invertedishEasterEggLvlTwoObjects.add(invertedishEasterEggLvlTwo , invertedishBackButton , classicBackButtonText)
invertedishEasterEggLvlThreeObjects.add(invertedishEasterEggLvlThree , invertedishBackButton , classicBackButtonText)
invertedishEasterEggLvlFourObjects.add(invertedishEasterEggLvlFour , invertedishBackButton , classicBackButtonText)
invertedishDiscoObjects.add(invertedishBackButton , classicBackButtonText)
invertedMenuObjects = py.sprite.Group()
invertedSettingsObjects = py.sprite.Group()
invertedThemesObjects = py.sprite.Group()
invertedGameObjects = py.sprite.Group()
invertedCreditsObjects = py.sprite.Group()
invertedEasterEggLvlOneObjects = py.sprite.Group()
invertedEasterEggLvlTwoObjects = py.sprite.Group()
invertedEasterEggLvlThreeObjects = py.sprite.Group()
invertedEasterEggLvlFourObjects = py.sprite.Group()
invertedDiscoObjects = py.sprite.Group()
invertedMenuObjects.add(invertedishStartButton , invertedishSettingsButton , yinYangStartButtonText , yinYangSettingsButtonText)
invertedSettingsObjects.add(invertedishThemesButton , yinYangThemesButtonText , invertedishBackButton , yinYangBackButtonText , invertedishFactoryResetButton , yinYangFactoryResetButtonText , invertedCreditsButton , yinYangCreditsButtonText)
invertedThemesObjects.add(invertedishClassicButton , invertedishYinYangButton , invertedishYangYinButton , yinYangClassicButtonText , yinYangYinYangButtonText , yinYangYangYinButtonText , invertedishInvertedButton , yinYangInvertedButtonText , invertedishInvertedishButton , yinYangInvertedishButtonText , invertedishClassicishButton , yinYangClassicishButtonText , invertedishAbyssButton , yinYangAbyssButtonText , invertedishBackButton , yinYangBackButtonText)
invertedGameObjects.add(invertedishDotButton , yangYinDotCounter , invertedishBackButton , yinYangBackButtonText)
invertedCreditsObjects.add(invertedishBackButton , yinYangBackButtonText)
invertedEasterEggLvlOneObjects.add(invertedishEasterEggLvlOne , invertedishBackButton , yinYangBackButtonText)
invertedEasterEggLvlTwoObjects.add(invertedishEasterEggLvlTwo , invertedishBackButton , yinYangBackButtonText)
invertedEasterEggLvlThreeObjects.add(invertedishEasterEggLvlThree , invertedishBackButton , yinYangBackButtonText)
invertedEasterEggLvlFourObjects.add(invertedishEasterEggLvlFour , invertedishBackButton , yinYangBackButtonText)
invertedDiscoObjects.add(invertedishBackButton , yinYangBackButtonText)
abyssMenuObjects = py.sprite.Group()
abyssSettingsObjects = py.sprite.Group()
abyssThemesObjects = py.sprite.Group()
abyssGameObjects = py.sprite.Group()
abyssCreditsObjects = py.sprite.Group()
abyssEasterEggLvlOneObjects = py.sprite.Group()
abyssEasterEggLvlTwoObjects = py.sprite.Group()
abyssEasterEggLvlThreeObjects = py.sprite.Group()
abyssEasterEggLvlFourObjects = py.sprite.Group()
abyssDiscoObjects = py.sprite.Group()
abyssMenuObjects.add(yangYinStartButton , yangYinSettingsButton , yinYangStartButtonText , yinYangSettingsButtonText)
abyssSettingsObjects.add(yangYinThemesButton , yinYangThemesButtonText , yangYinBackButton , yinYangBackButtonText , yangYinFactoryResetButton , yinYangFactoryResetButtonText , yangYinCreditsButton , yinYangCreditsButtonText)
abyssThemesObjects.add(yangYinClassicButton , yangYinYinYangButton , yangYinYangYinButton , yinYangClassicButtonText , yinYangYinYangButtonText , yinYangYangYinButtonText , yangYinInvertedButton , yinYangInvertedButtonText , yangYinInvertedishButton , yinYangInvertedishButtonText , yangYinClassicishButton , yinYangClassicishButtonText , yangYinAbyssButton , yinYangAbyssButtonText , yangYinBackButton , yinYangBackButtonText)
abyssGameObjects.add(yangYinDotButton , yangYinDotCounter , yangYinBackButton , yinYangBackButtonText)
abyssCreditsObjects.add(yangYinBackButton , yinYangBackButtonText)
abyssEasterEggLvlOneObjects.add(yangYinEasterEggLvlOne , yangYinBackButton , yinYangBackButtonText)
abyssEasterEggLvlTwoObjects.add(yangYinEasterEggLvlTwo , yangYinBackButton , yinYangBackButtonText)
abyssEasterEggLvlThreeObjects.add(yangYinEasterEggLvlThree , yangYinBackButton , yinYangBackButtonText)
abyssEasterEggLvlFourObjects.add(yangYinEasterEggLvlFour , yangYinBackButton , yinYangBackButtonText)
abyssDiscoObjects.add(yangYinBackButton , yinYangBackButtonText)
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
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Game"
            elif mouseX > classicSettingsButton.rect.left and mouseX < classicSettingsButton.rect.right and mouseY > classicSettingsButton.rect.top and mouseY < classicSettingsButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Settings"
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
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
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Themes"
            elif mouseX > classicCreditsButton.rect.left and mouseX < classicCreditsButton.rect.right and mouseY > classicCreditsButton.rect.top and mouseY < classicCreditsButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Credits"
            elif mouseX > classicFactoryResetButton.rect.left and mouseX < classicFactoryResetButton.rect.right and mouseY > classicFactoryResetButton.rect.top and mouseY < classicFactoryResetButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
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
            elif mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Menu"
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
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
    elif level == "Credits":
        if creditsMessage == False:
            creditsMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Credits" , "Credits to Mixit for their sound effects. Their website is at https://mixit.co , and their sound efffects page can be found at https://mixit.co/free-sound-effects/")
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Bug" , "Just to let you know, there is a bug that takes effect when you press the Backslash key. Don't press it, or else all your progress will be lost.")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Settings"
                    creditsMessage = False
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
                if event.key == py.K_BACKSLASH:
                    level = "Easter Egg Level One"
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicCreditsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangCreditsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            for object in yangYinCreditsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            for object in classicishCreditsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            for object in invertedishCreditsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            for object in invertedCreditsObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            for object in abyssCreditsObjects:
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
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Classic"
            elif mouseX > classicYinYangButton.rect.left and mouseX < classicYinYangButton.rect.right and mouseY > classicYinYangButton.rect.top and mouseY < classicYinYangButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Yin Yang"
            elif mouseX > classicYangYinButton.rect.left and mouseX < classicYangYinButton.rect.right and mouseY > classicYangYinButton.rect.top and mouseY < classicYangYinButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Yang Yin"
            elif mouseX > classicClassicishButton.rect.left and mouseX < classicClassicishButton.rect.right and mouseY > classicClassicishButton.rect.top and mouseY < classicClassicishButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Classicish"
            elif mouseX > classicInvertedishButton.rect.left and mouseX < classicInvertedishButton.rect.right and mouseY > classicInvertedishButton.rect.top and mouseY < classicInvertedishButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Invertedish"
            elif mouseX > classicInvertedButton.rect.left and mouseX < classicInvertedButton.rect.right and mouseY > classicInvertedButton.rect.top and mouseY < classicInvertedButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Inverted"
            elif mouseX > classicAbyssButton.rect.left and mouseX < classicAbyssButton.rect.right and mouseY > classicAbyssButton.rect.top and mouseY < classicAbyssButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    theme = "Abyss"
            elif mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Settings"
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
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
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    dotValue = dotValue + clickValue
            elif mouseX > classicClickUpgradeButton.rect.left and mouseX < classicClickUpgradeButton.rect.right and mouseY > classicClickUpgradeButton.rect.top and mouseY < classicClickUpgradeButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                        clickValue = (clickValue + 1) * (prestigeValue + 1)
                        clickUpgradeValue = clickUpgradeValue + 1
            elif mouseX > classicPrestigeButton.rect.left and mouseX < classicPrestigeButton.rect.right and mouseY > classicPrestigeButton.rect.top and mouseY < classicPrestigeButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
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
            elif mouseX > classicStagePrestigeButton.rect.left and mouseX < classicStagePrestigeButton.rect.right and mouseY > classicStagePrestigeButton.rect.top and mouseY < classicStagePrestigeButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
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
            elif mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Menu"
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
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
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
        classicGameObjects.remove(classicDotCounter)
        yinYangGameObjects.remove(classicDotCounter)
        yangYinGameObjects.remove(yangYinDotCounter)
        classicishGameObjects.remove(yangYinDotCounter)
        invertedishGameObjects.remove(classicDotCounter)
        invertedGameObjects.remove(yangYinDotCounter)
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
        classicGameObjects.add(classicDotCounter)
        yinYangGameObjects.add(classicDotCounter)
        yangYinGameObjects.add(yangYinDotCounter)
        classicishGameObjects.add(yangYinDotCounter)
        invertedishGameObjects.add(classicDotCounter)
        invertedGameObjects.add(yangYinDotCounter)
        abyssGameObjects.add(yangYinDotCounter)
        if theme == "Classic":
            for object in classicGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(classicClickUpgradeButton.surface , classicClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(classicPrestigeButton.surface , classicPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(classicStagePrestigeButton.surface , classicStagePrestigeButton.rect)
        elif theme == "Yin Yang":
            for object in yinYangGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(yinYangClickUpgradeButton.surface , yinYangClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(yinYangPrestigeButton.surface , yinYangPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(yinYangStagePrestigeButton.surface , yinYangStagePrestigeButton.rect)
        elif theme == "Yang Yin":
            for object in yangYinGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(yangYinClickUpgradeButton.surface , yangYinClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(yangYinPrestigeButton.surface , yangYinPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(yangYinStagePrestigeButton.surface , yangYinStagePrestigeButton.rect)
        elif theme == "Classicish":            
            for object in classicishGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(classicClickUpgradeButton.surface , classicClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(classicPrestigeButton.surface , classicPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(classicStagePrestigeButton.surface , classicStagePrestigeButton.rect)
        elif theme == "Invertedish":
            for object in invertedishGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(invertedishClickUpgradeButton.surface , invertedishClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(invertedishPrestigeButton.surface , invertedishPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(invertedishStagePrestigeButton.surface , invertedishStagePrestigeButton.rect)
        elif theme == "Inverted":
            for object in invertedGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(invertedishClickUpgradeButton.surface , invertedishClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(invertedishPrestigeButton.surface , invertedishPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(invertedishStagePrestigeButton.surface , invertedishStagePrestigeButton.rect)
        elif theme == "Abyss":
            for object in abyssGameObjects:
                screen.blit(object.surface , object.rect)
            if dotValue > ((10 ** (clickUpgradeValue + 2)) * stageValue):
                screen.blit(yangYinClickUpgradeButton.surface , yangYinClickUpgradeButton.rect)
            if dotValue > ((15000 * ((prestigeValue + 1) ** prestigeValue)) * stageValue):
                screen.blit(yangYinPrestigeButton.surface , yangYinPrestigeButton.rect)
            if prestigeValue > (9 ** stageValue) and dotValue > int((15000 * (((9 ** stageValue + 1)) ** (9 ** stageValue))) * 0.75):
                screen.blit(yangYinStagePrestigeButton.surface , yangYinStagePrestigeButton.rect)
        py.display.flip()
    elif level == "Easter Egg Level One":
        if easterEggLevelOneMessage == False:
            easterEggLevelOneMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Bug" , "Don't say I didn't warn you about the bug...")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicEasterEggLvlOne.rect.left and mouseX < classicEasterEggLvlOne.rect.right and mouseY > classicEasterEggLvlOne.rect.top and mouseY < classicEasterEggLvlOne.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Easter Egg Level Two"
            elif mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Credits"
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicEasterEggLvlOneObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangEasterEggLvlOneObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            for object in yangYinEasterEggLvlOneObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            for object in classicishEasterEggLvlOneObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            for object in invertedishEasterEggLvlOneObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            for object in invertedEasterEggLvlOneObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            for object in abyssEasterEggLvlOneObjects:
                screen.blit(object.surface , object.rect)
        py.display.flip()
    elif level == "Easter Egg Level Two":
        if easterEggLevelTwoMessage == False:
            easterEggLevelTwoMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Work In Progress" , "Oh, this section is just a work in progress. You may ask why the button was so small, and about that, as I told you, it was a random bug as this section is not finished.")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicEasterEggLvlTwo.rect.left and mouseX < classicEasterEggLvlTwo.rect.right and mouseY > classicEasterEggLvlTwo.rect.top and mouseY < classicEasterEggLvlTwo.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Easter Egg Level Three"
            elif mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Easter Egg Level One"
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicEasterEggLvlTwoObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangEasterEggLvlTwoObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            for object in yangYinEasterEggLvlTwoObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            for object in classicishEasterEggLvlTwoObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            for object in invertedishEasterEggLvlTwoObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            for object in invertedEasterEggLvlTwoObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            for object in abyssEasterEggLvlTwoObjects:
                screen.blit(object.surface , object.rect)
        py.display.flip()
    elif level == "Easter Egg Level Three":
        if easterEggLevelThreeMessage == False:
            easterEggLevelThreeMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Restricted Area" , "You're not supposed to be here. This section can cause crashes to your computer, as it uses commands still in the beta testing phase. Good luck.")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicEasterEggLvlThree.rect.left and mouseX < classicEasterEggLvlThree.rect.right and mouseY > classicEasterEggLvlThree.rect.top and mouseY < classicEasterEggLvlThree.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Easter Egg Level Four"
            elif mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Easter Egg Level Two"
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicEasterEggLvlThreeObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangEasterEggLvlThreeObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            for object in yangYinEasterEggLvlThreeObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            for object in classicishEasterEggLvlThreeObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            for object in invertedishEasterEggLvlThreeObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            for object in invertedEasterEggLvlThreeObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            for object in abyssEasterEggLvlThreeObjects:
                screen.blit(object.surface , object.rect)
        py.display.flip()
    elif level == "Easter Egg Level Four":
        py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
        if easterEggLevelFourMessage == False:
            easterEggLevelFourMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Secret" , "Ok, this screen is secret for a reason. This contains unreleased areas, which you have somehow found a backdoor to. Do not persist and dwell on this for too long, just go back to the main game.")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicEasterEggLvlFour.rect.left and mouseX < classicEasterEggLvlFour.rect.right and mouseY > classicEasterEggLvlFour.rect.top and mouseY < classicEasterEggLvlFour.rect.bottom:
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Disco"
            elif mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Easter Egg Level Three"
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
        if theme == "Classic":
            screen.fill((255 , 0 , 255))
            for object in classicDiscoObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yin Yang":
            screen.fill((0 , 0 , 0))
            for object in yinYangEasterEggLvlFourObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Yang Yin":
            screen.fill((255 , 255 , 255))
            for object in yangYinEasterEggLvlFourObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Classicish":
            screen.fill((255 , 0 , 255))
            for object in classicishEasterEggLvlFourObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Invertedish":
            screen.fill((0 , 255 , 0))
            for object in invertedishEasterEggLvlFourObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Inverted":
            screen.fill((0 , 255 , 0))
            for object in invertedEasterEggLvlFourObjects:
                screen.blit(object.surface , object.rect)
        elif theme == "Abyss":
            screen.fill((0 , 0 , 0))
            for object in abyssEasterEggLvlFourObjects:
                screen.blit(object.surface , object.rect)
        py.display.flip()
    elif level == "Disco":
        randomColour = (rd.randint(0 , 255) , rd.randint(0 , 255) , rd.randint(0 , 255))
        if discoMessage == False:
            discoMessage = True
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("The Disco" , "Your persistence and stubborness paid off. You have entered the disco. If you have epilepsy or feel uncomfortable with flashing lights, do not press the Slash key, as it toggles the flashing lights on and off. If you don't need to worry about that, you can press the Slash key to get fully immersed into the disco. You can also use the key to keep the background on a colour that you like.")
            if sfxBool == True:
                py.mixer.music.load("Message.wav")
                py.mixer.music.set_volume(0.4)
                py.mixer.music.play()
            ms.showinfo("Some Settings" , "If you wanna change how long it takes for the screen to change colour, you can use the Comma and Period keys to change that. They change based on how small it currently takes for your screen to change colour")
        for event in py.event.get():
            if event.type == py.QUIT:
                programRunning = False
            if mouseX > classicBackButton.rect.left and mouseX < classicBackButton.rect.right and mouseY > classicBackButton.rect.top and mouseY < classicBackButton.rect.bottom:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
                if event.type == py.MOUSEBUTTONDOWN:
                    if sfxBool == True:
                        py.mixer.music.load("Click.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        py.mixer.music.load("Transition.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    level = "Easter Egg Level Four"
            else:
                py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    if sfxBool == True:
                        sfxBool = False
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now off")
                    elif sfxBool == False:
                        sfxBool = True
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                        ms.showinfo("Sound Effects" , "Sound effects are now on")
                if event.key == py.K_SLASH:
                    if flashingBool == True:
                        flashingBool = False
                    elif flashingBool == False:
                        flashingBool = True
                if event.key == py.K_COMMA:
                    discoDuration = discoDuration + 50
                    screenFlashCount = "Your screen flashes every " + str(discoDuration) + " milliseconds"
                    py.time.set_timer(SCREENCOLOURCHANGE , discoDuration)
                    if sfxBool == True:
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    ms.showinfo("Screen Flash" , screenFlashCount)
                if event.key == py.K_PERIOD:
                    if discoDuration > 99:
                        discoDuration = discoDuration - 50
                    elif discoDuration > 19:
                        discoDuration = discoDuration - 5
                    elif discoDuration > 0:
                        discoDuration = discoDuration - 1
                    screenFlashCount = "Your screen flashes every " + str(discoDuration) + " milliseconds"
                    py.time.set_timer(SCREENCOLOURCHANGE , discoDuration)
                    if sfxBool == True:
                        py.mixer.music.load("Message.wav")
                        py.mixer.music.set_volume(0.4)
                        py.mixer.music.play()
                    ms.showinfo("Screen Flash" , screenFlashCount)
            if event.type == SCREENCOLOURCHANGE and flashingBool == True:
                randomColour = (rd.randint(0 , 255) , rd.randint(0 , 255) , rd.randint(0 , 255))
                screen.fill(randomColour)
        for object in classicDiscoObjects:
            screen.blit(object.surface , object.rect)
        py.display.flip()
py.quit()
