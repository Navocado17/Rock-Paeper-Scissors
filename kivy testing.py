from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.screenmanager import RiseInTransition
from kivy.config import Config

Config.set('graphics', 'window_state', 'maximized')


class MainMenu(Screen):
    def quitGame(self):
        import sys
        sys.exit()

class Game(Screen):
    playerSideImage = StringProperty("assets/rock.jpg")
    def rock(self):
        self.playerSideImage = "assets/rock.jpg" 
    def paper(self):
        self.playerSideImage = "assets/paper.jpg" 
    def scissors(self):
        self.playerSideImage = "assets/scissors.jpg" 

class Settings(Screen):
    def on_slider_value(self,widget):
        if sound:
            sound.volume = widget.value
    def on_switch_active(self,widget):
        print("Switch:",str(widget.active))
        

class RockPaperScissorsGame2022(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(Game(name='game'))
        sm.add_widget(Settings(name='settings'))
        return sm

sound = SoundLoader.load('SOUND/angrybirdstheme.mp3')
if sound:
    sound.loop = True
    sound.play()
    
RockPaperScissorsGame2022().run()