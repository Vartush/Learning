from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from datetime import datetime
from collections import defaultdict

class PressRecorderApp(App):
    def build(self):
        self.press_counts = defaultdict(int)
        self.root = BoxLayout(orientation='vertical')

        self.button = Button(text='Press Me', size_hint=(1, 0.1))
        self.button.bind(on_press=self.record_press)
        self.root.add_widget(self.button)

        self.scroll_view = ScrollView(size_hint=(1, 0.9))
        self.label = Label(size_hint_y=None, text_size=(None, None), valign='top')
        self.label.bind(texture_size=self.label.setter('size'))
        self.scroll_view.add_widget(self.label)
        self.root.add_widget(self.scroll_view)

        return self.root

    def record_press(self, instance):
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.press_counts[current_date] += 1
        self.display_counts()

    def display_counts(self):
        display_text = ""
        for date, count in self.press_counts.items():
            display_text += f"{date}: {count} times\n"
        self.label.text = display_text

if __name__ == '__main__':
    PressRecorderApp().run()
