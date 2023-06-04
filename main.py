from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from random import randint
from kivy.animation import Animation
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 800)
Oyes = 0
Xno = 0


class MyApp(App):

    def generate(self):
        global a
        global b
        global c
        global e
        a = randint(1, 9)
        b = randint(1, 9)
        c = a * b
        e = ('Пример: ' + str(a) + " * " + str(b) + " = ?")

    def update_label(self):
        self.lbl.text = self.formula

    def update_after_check(self):
        self.lblp.text = self.formula

    def add_number(self, instance):  # убирает ноль
        if (self.formula == "0"):
            self.formula = ""

        self.formula += str(instance.text)  # instance.text отвечает за прибавление текста из кнопок в пример
        self.update_label()

    def build(self):
        while True:
            self.generate()
            self.formula = "0"
            self.lblp = "0"
            self.background = Label(text='Т', font_size=10000, color=(255, 100, 1, 1))
            self.labelO = str(Oyes)
            self.labelX = str(Xno)
            bl = BoxLayout(orientation='vertical')
            gl = GridLayout(cols=3, spacing=[0], padding=[0, -70, 0, 0])
            bl.add_widget(self.background)
            self.schetovod = Label(text="Счетовод", font_size=80, color=(255, 1, 1, 1))
            bl.add_widget(self.schetovod)
            self.lblp = Label(text=e, font_size=60)
            bl.add_widget(self.lblp)

            self.lbl = Label(text=self.formula, font_size=100)
            self.yes = Label(text=self.labelO, font_size=30, color=(0, 1, 0, 1))
            self.no = Label(text=self.labelX, font_size=30, color=(1, 0, 0, 1))

            bl.add_widget(self.yes)
            bl.add_widget(self.lbl)
            bl.add_widget(self.no)

            gl.add_widget(Button(text="1", on_press=self.add_number, background_color=(1, 0, 0, 1)))
            gl.add_widget(Button(text="2", on_press=self.add_number, background_color=(0, 1, 0, 1)))
            gl.add_widget(Button(text="3", on_press=self.add_number, background_color=(0, 0, 1, 1)))
            gl.add_widget(Button(text="4", on_press=self.add_number, background_color=(1, 0, 0, 1)))
            gl.add_widget(Button(text="5", on_press=self.add_number, background_color=(0, 1, 0, 1)))
            gl.add_widget(Button(text="6", on_press=self.add_number, background_color=(0, 0, 1, 1)))
            gl.add_widget(Button(text="7", on_press=self.add_number, background_color=(1, 0, 0, 1)))
            gl.add_widget(Button(text="8", on_press=self.add_number, background_color=(0, 1, 0, 1)))
            gl.add_widget(Button(text="9", on_press=self.add_number, background_color=(0, 0, 1, 1)))
            gl.add_widget(Button(text="Очистить", on_press=self.clear, background_color=(1, 0, 0, 1)))
            gl.add_widget(Button(text="0", on_press=self.add_number, background_color=(0, 1, 0, 1)))
            gl.add_widget(Button(text="Проверить", on_press=self.check, background_color=(0, 0, 1, 1)))

            anim = Animation(x=0, y=600)
            anim.start(self.schetovod)
            anim = Animation(x=0, y=400)
            anim.start(self.lblp)
            anim = Animation(x=0, y=200)
            anim.start(self.lbl)
            anim = Animation(x=-280, y=700)
            anim.start(self.yes)
            anim = Animation(x=-280, y=650)
            anim.start(self.no)

            bl.add_widget(gl)

            return bl

    def check(self, instance):
        global c
        global Oyes
        global Xno
        if self.lbl.text == str(c):
            print('Правильно')
            self.schetovod.color = (0, 1, 0, 1)
            self.schetovod.text = ("Правильно")
            self.formula = "0"
            self.generate()
            self.lblp.text = (str(a) + " * " + str(b) + " = ?")
            self.lblp.font_size = 70
            Oyes = Oyes + 1
            self.yes.text = str(Oyes)
        else:
            print("Неправильно")
            self.schetovod.color = (1, 0, 0, 1)
            self.schetovod.text = ("Неправильно")
            Xno = Xno + 1
            self.no.text = str(Xno)

    def clear(self, instance):
        self.lbl.text = "0"
        self.formula = "0"


if __name__ == "__main__":
    MyApp().run()
