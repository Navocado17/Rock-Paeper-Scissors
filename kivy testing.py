from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen


class MainMenu(Screen):
    def quitGame(self):
        import sys
        sys.exit()


class Game(Screen):
    pass

class Settings(Screen):
    pass



class MainWidget(Widget):
    pass


class RockPaperScissorsGame2022(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(Game(name='game'))
        sm.add_widget(Settings(name='settings'))
        return sm

sound = SoundLoader.load('SOUND/angrybirdstheme.mp3')
if sound:
    sound.play()
    
RockPaperScissorsGame2022().run()
