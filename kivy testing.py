from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader


class MainMenu(BoxLayout):
    pass

class MainWidget(Widget):
    pass


class RockPaperScissorsGame2022(App):
    pass

sound = SoundLoader.load('SOUND/angrybirdstheme.mp3')
if sound:
    sound.play()
RockPaperScissorsGame2022().run()
