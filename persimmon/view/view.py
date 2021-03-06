# Persimmon imports
from persimmon.view import BlackBoard, Blocks
from persimmon.view.util import PlayButton, Notification
# Kivy imports
from kivy.app import App
from kivy.config import Config
from kivy.factory import Factory
from kivy.properties import ObjectProperty
# Kivy Widgets
from kivy.uix.image import Image
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
# Others
import logging
import sys


logger = logging.getLogger(__name__)
Config.read('config.ini')

class ViewApp(App):
    background = ObjectProperty()

    def build(self):
        self.title = 'Persimmon'
        self.background = Image(source='background.png').texture

class Backdrop(FloatLayout):
    """ Class on top of blackboard where the main control panel and buttons are
    displayed. Unaffected by zoom/movement of the underlying scatter. """
    play_button = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_hint()

    def on_graph_executed(self):
        self.play_button.ready()

    def remove_hint(self):
        self.remove_widget(self.hint)
        self.hint = None

    def add_hint(self):
        self.hint = Factory.Hint()
        self.add_widget(self.hint, index=len(self.children))


if __name__ == '__main__':
    ViewApp().run()
