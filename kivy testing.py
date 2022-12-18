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
                elif self.playerChoice == "rock":
                    if self.opponentChoice == "scissors":
                        message = "Rock smashes scissors! You win!"
                    else:
                        message = "Paper covers rock! You lose."
                elif self.playerChoice == "paper":
                    if self.opponentChoice == "rock":
                        message = "Paper covers rock! You win!"
                    else:
                        message = "Scissors cuts paper! You lose."
                elif self.playerChoice == "scissors":
                    if self.opponentChoice == "paper":
                        message = "Scissors cuts paper! You win!"
                    else:
                        message = "Rock smashes scissors! You lose."
                self.message = message
                self.confirmed = False
                self.parent.transition = RiseInTransition()
                self.parent.current = "outcome"
                
                
            Clock.schedule_once(show_result, 2)
        Clock.schedule_once(delayedWork, 3)
        
class Result(Screen):
    result_text = StringProperty("")
    def on_pre_enter(self, *args):
        gameWindow = self.manager.get_screen('game')
        self.result_text = gameWindow.message
        return super().on_pre_enter(*args)

    def returnToGame(self):
        self.manager.current = 'game'
        self.manager.transition = SlideTransition()
class Settings(Screen):
    def on_slider_value(self,widget):
        if sound:
            sound.volume = widget.value
    def on_switch_active(self,widget):
        print("Switch:",str(widget.active))
        

class RockPaperScissorsGame2022(App):
    def build(self):
        self.icon = "assets/icon.png"
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(Game(name='game'))
        sm.add_widget(Settings(name='settings'))
        sm.add_widget(Result(name='outcome'))
        return sm


sound = SoundLoader.load('SOUND/angrybirdstheme.mp3')
if sound:
    sound.loop = True
    sound.play()
    
RockPaperScissorsGame2022().run()

