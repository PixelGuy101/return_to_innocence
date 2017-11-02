import kivy
kivy.require('1.10.0')
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

Builder.load_file('main.kv')

class MenuScreen(Screen):
    pass
class GalleryScreen(Screen):
    pass
class AboutScreen(Screen):
    def createtext(self, index):
        arr = ['Первый пробный текст','Второй пробный текст','Третий пробный текст']
        return arr[index]

sm = ScreenManager(transition=WipeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GalleryScreen(name='gallery'))
sm.add_widget(AboutScreen(name='about'))

class MainApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    MainApp().run()