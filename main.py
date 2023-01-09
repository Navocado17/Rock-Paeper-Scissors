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



class Game(Screen):
    playerSideImage = StringProperty("assets/rock.jpg")
    opponentImage = StringProperty("assets/loading.jpg")
    movesList  = ["rock", "paper", "scissors"]
    opponentCharacterImage = StringProperty("assets/opponent.jpg")
    opponentThinking = StringProperty("assets/thinking.jpg")
    eddieVoicelines = ["You cant beat me maen", "the only thing they fear is me maen", "ill onepump u maen", "back to class maen", "sit ur place maen", "quit the game maen"]
    playerChoice = "rock"
    opponentChoice = ""
    confirmed = BooleanProperty(False)
    eddieMode = False
    message = ""
    gameResult = ""
    def on_pre_enter(self, *args):
        settings = self.manager.get_screen('settings')
        self.eddieMode = settings.eddieMode
        print(self.eddieMode)
        if self.eddieMode:
            self.opponentCharacterImage = "assets/reactions/eddie/6.jpg"
            self.opponentThinking = "assets/reactions/eddie/3.jpg"
        return super().on_pre_enter(*args)
        
        
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
        self.opponentCharacterImage = self.opponentThinking
        self.confirmed = True
        self.opponentImage = "assets/loading.jpg"
        
        def delayedWork(*l):
            if self.eddieMode == True:
                if self.playerChoice == "rock":
                    self.opponentImage = "assets/paper_FLIPPED.jpg"
                elif self.playerChoice == "paper":
                    self.opponentImage = "assets/scissors_FLIPPED.jpg"
                elif self.playerChoice== "scissors":
                    self.opponentImage = "assets/rock_FLIPPED.jpg" 
                self.opponentCharacterImage = "assets/reactions/eddie/6.jpg"
            else:
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
                if self.eddieMode == True:
                    message = self.eddieVoicelines[random.randint(0, len(self.eddieVoicelines)-1)]
                    self.gameResult = "e"
                elif self.playerChoice == self.opponentChoice:
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
                if self.eddieMode:
                    self.opponentCharacterImage = "assets/reactions/eddie/6.jpg"
                else:
                    self.opponentCharacterImage = "assets/opponent.jpg"
                
            Clock.schedule_once(show_result, 2)
        Clock.schedule_once(delayedWork, 2)
        
class Result(Screen):
    result_text = StringProperty("")
    image = StringProperty("")
    loseImages = ["assets/reactions/lose/1.jpg", "assets/reactions/lose/2.jpg", "assets/reactions/lose/3.jpg", "assets/reactions/lose/4.jpg"]
    winImages = ["assets/reactions/win/1.jpg", "assets/reactions/win/2.jpg", "assets/reactions/win/3.jpg", "assets/reactions/win/4.jpg"]
    tieImages = ["assets/reactions/tie/1.jpg", "assets/reactions/tie/2.jpg", "assets/reactions/tie/3.jpg", "assets/reactions/tie/4.jpg"]
    eddieImages = ["assets/reactions/eddie/1.png", "assets/reactions/eddie/2.png", "assets/reactions/eddie/4.jpg", "assets/reactions/eddie/5.jpg", "assets/reactions/eddie/7.jpg", "assets/reactions/eddie/8.jpg"]
    def on_pre_enter(self, *args):
        gameWindow = self.manager.get_screen('game')
        self.result_text = gameWindow.message
        if gameWindow.gameResult == "w":
            self.image = self.winImages[random.randint(0, (len(self.winImages) - 1))]
        elif gameWindow.gameResult == "l":
            self.image = self.loseImages[random.randint(0, (len(self.loseImages) - 1))]
        elif gameWindow.gameResult == "t":
            self.image = self.tieImages[random.randint(0, (len(self.tieImages) - 1))]
        elif gameWindow.gameResult == "e":
            self.image = self.eddieImages[random.randint(0, (len(self.eddieImages) - 1))]
        return super().on_pre_enter(*args)

    def returnToGame(self):
        self.manager.current = 'game'
        self.manager.transition = SlideTransition()
class Settings(Screen):
    eddieMode = False
    eddieSound = SoundLoader.load("SOUND/badpiggiestheme.mp3")
    background = StringProperty("assets/settings.png")
    def on_slider_value(self,widget):
        if sound:
            sound.volume = widget.value
        if self.eddieSound:
            self.eddieSound.volume = widget.value
    def on_switch_active(self,widget):
        print("Switch:",str(widget.active))
        if(widget.active):
            self.eddieMode = True
            def jumpscare(*l):
                self.background = 'assets/reactions/eddie/2.png'
                
            Clock.schedule_once(jumpscare, 1)
            print(self.eddieMode)
            if sound:
                sound.stop()

    
            if self.eddieSound:
                self.eddieSound.loop=True
                self.eddieSound.play()
        else:
            self.eddieMode = False
            self.background = 'assets/settings.png'
            if self.eddieSound:
                self.eddieSound.stop()
            if sound:
                sound.play()

class MainMenu(Screen):
    eddieMode = False
    background = StringProperty("")
    def quitGame(self):
        import sys
        sys.exit()
    def on_pre_enter(self, *args):
        settings = self.manager.get_screen('settings')
        self.eddieMode = settings.eddieMode
        if self.eddieMode == False:
            self.background = "assets/background1.png"
        else:
            self.background = "assets/reactions/eddie/9.png"
        return super().on_pre_enter(*args)
    
class LoadingScreen(Screen):
    def wait(self, *args):
        self.manager.current = "menu"
    def on_pre_enter(self, *args):
        Clock.schedule_once(self.wait, 3)
        return super().on_pre_enter(*args)
    def on_leave(self, *args):
        if sound:
            sound.loop = True
            sound.play()
        return super().on_leave(*args)
class RockPaeperScissorsGame2022(App):
    def build(self):
        self.icon = "assets/icon.png"
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(LoadingScreen(name = 'loading'))
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(Settings(name='settings'))
        sm.add_widget(Game(name='game'))
        sm.add_widget(Result(name='outcome'))
        return sm

    
RockPaeperScissorsGame2022().run()