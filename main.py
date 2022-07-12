from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return  Button(text= "Hello Kivy")



TestApp().run()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
