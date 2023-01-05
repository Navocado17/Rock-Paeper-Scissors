from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
import time
import random
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.screenmanager import RiseInTransition
from kivy.clock import Clock
from kivy.config import Config

Config.set('graphics', 'window_state', 'maximized')
global sound
sound = SoundLoader.load('SOUND/angrybirdstheme.mp3')

class MainMenu(Screen):
    def quitGame(self):
        import sys
        sys.exit()

class Game(Screen):
    playerSideImage = StringProperty("assets/rock.jpg")
    opponentImage = StringProperty("assets/loading.jpg")
    movesList  = ["rock", "paper", "scissors"]
    opponentCharacterImage = StringProperty("assets/opponent.jpg")
    playerChoice = "rock"
    opponentChoice = ""
    confirmed = BooleanProperty(False)
    message = ""
    gameResult = ""
    def rock(self):
        self.playerSideImage = "assets/rock.jpg"
        self.playerChoice = "rock"
    def paper(self):
        self.playerSideImage = "assets/paper.jpg" 
        self.playerChoice = "paper"
    def scissors(self):
        self.playerSideImage = "assets/scissors.jpg"
        self.playerChoice = "scissors"
    def confirm(self):
        self.opponentCharacterImage = "assets/thinking.jpg"
        self.confirmed = True
        self.opponentImage = "assets/loading.jpg"
        
        def delayedWork(*l):
            self.opponentChoice = self.movesList[random.randint(0, 2)]
            if self.opponentChoice == "rock":
                self.opponentImage = "assets/rock_FLIPPED.jpg"
            elif self.opponentChoice == "paper":
                self.opponentImage = "assets/paper_FLIPPED.jpg"
            elif self.opponentChoice == "scissors":
                self.opponentImage = "assets/scissors_FLIPPED.jpg"  
            self.opponentCharacterImage = "assets/opponent.jpg"
            def show_result(*l):
                message = ""
                if self.playerChoice == self.opponentChoice:
                    message = f"Both players selected {self.playerChoice}. It's a tie!"
                    self.gameResult = "t"
                elif self.playerChoice == "rock":
                    if self.opponentChoice == "scissors":
                        message = "Rock smashes scissors! You win!"
                        self.gameResult = "w"
                    else:
                        message = "Paper covers rock! You lose."
                        self.gameResult = "l"
                elif self.playerChoice == "paper":
                    if self.opponentChoice == "rock":
                        message = "Paper covers rock! You win!"
                        self.gameResult = "w"
                    else:
                        message = "Scissors cuts paper! You lose."
                        self.gameResult = "l"
                elif self.playerChoice == "scissors":
                    if self.opponentChoice == "paper":
                        message = "Scissors cuts paper! You win!"
                        self.gameResult = "w"
                    else:
                        message = "Rock smashes scissors! You lose."
                        self.gameResult = "l"
                self.message = message
                self.confirmed = False
                self.manager.transition = RiseInTransition()
                self.manager.current = "outcome"
                
                
            Clock.schedule_once(show_result, 2)
        Clock.schedule_once(delayedWork, 3)
        
class Result(Screen):
    result_text = StringProperty("")
    image = StringProperty("")
    loseImages = ["assets/reactions/lose/1.jpg", "assets/reactions/lose/2.jpg", "assets/reactions/lose/3.jpg", "assets/reactions/lose/4.jpg"]
    winImages = ["assets/reactions/win/1.jpg", "assets/reactions/win/2.jpg", "assets/reactions/win/3.jpg", "assets/reactions/win/4.jpg"]
    tieImages = ["assets/reactions/tie/1.jpg", "assets/reactions/tie/2.jpg", "assets/reactions/tie/3.jpg", "assets/reactions/tie/4.jpg"]
    def on_pre_enter(self, *args):
        gameWindow = self.manager.get_screen('game')
        self.result_text = gameWindow.message
        if gameWindow.gameResult == "w":
            self.image = self.winImages[random.randint(0, (len(self.winImages) - 1))]
        elif gameWindow.gameResult == "l":
            self.image = self.loseImages[random.randint(0, (len(self.loseImages) - 1))]
        elif gameWindow.gameResult == "t":
            self.image = self.tieImages[random.randint(0, (len(self.tieImages) - 1))]
        return super().on_pre_enter(*args)

    def returnToGame(self):
        self.manager.current = 'game'
        self.manager.transition = SlideTransition()
class Settings(Screen):
    eddieMode = False
    eddieSound = SoundLoader.load("SOUND/badpiggiestheme.mp3")
    def on_slider_value(self,widget):
        if sound:
            sound.volume = widget.value
    def on_switch_active(self,widget):
        print("Switch:",str(widget.active))
        if(widget.active):
            self.eddieMode = True
            if sound:
                sound.stop()
    
            if self.eddieSound:
                self.eddieSound.play()
        else:
            if self.eddieSound:
                self.eddieSound.stop()
class RockPaperScissorsGame2022(App):
    def build(self):
        self.icon = "assets/icon.png"
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(Game(name='game'))
        sm.add_widget(Settings(name='settings'))
        sm.add_widget(Result(name='outcome'))
        return sm
if sound:
    sound.loop = True
    sound.play()
    
RockPaperScissorsGame2022().run()

