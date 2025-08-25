from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import webbrowser

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text="سایت اول")
        btn1.bind(on_press=lambda x: webbrowser.open("https://example.com"))
        btn2 = Button(text="سایت دوم")
        btn2.bind(on_press=lambda x: webbrowser.open("https://google.com"))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout

MyApp().run()
