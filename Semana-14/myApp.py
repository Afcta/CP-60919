import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window

Window.size=(600,400)

#Prob not needed, replace with class MyAppLayout
class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    

class MyAppLayout(BoxLayout):

    def __init__(self, **kwargs):
        # ...
        """a MyAppLayout(BoxLayout) 

        Args:
            BoxLayout (**kwargs): str topRowText, str topRowLabel, int topRowFont_size
        """
        # self.box = BoxLayout(orientation='vertical', padding=50, spacing=20)

        super().__init__(**kwargs)
        # if "topRowFont_size" not in kwargs: kwargs["topRowFont_size"] = 70
        # self.topRow = Label(text="MyApp", font_size=70, color=(1,1,1,1))
        # self.mainPanel = self.getMainPanel()
        # self.bottomRow = self.getBottomRow()
        # self.box.add_widget(self.topRow)
        # self.box.add_widget(self.mainPanel)
        # self.box.add_widget(self.bottomRow)     

    def getMainPanel(self):
        mainPanel = BoxLayout(orientation='vertical', padding=30, spacing=20)
        a = SquareButton(text="a", disabled=True) #Inactive
        b = SquareButton(text="b", disabled=True)
        c = SquareButton(text="c", disabled=True) #Inactive
        d = SquareButton(text="d", disabled=True)
        self.buttonRow = BoxLayout(orientation="vertical", padding = 10, spacing=20)
        self.buttonRow.add_widget(a)
        self.buttonRow.add_widget(b)
        self.buttonRow.add_widget(c)
        self.buttonRow.add_widget(d)
        mainPanel.add_widget(self.buttonRow)
        self.centerLabel = Label(text="Hello!", font_size=80, color=(1,1,1,1))
        mainPanel.add_widget(self.centerLabel)
        return mainPanel
        
    def getBottomRow(self):
        self.bottomRow = BoxLayout(orientation="horizontal", spacing=20, padding=50)
        return self.bottomRow

    # mais getters se necessário...


class MyApp(App):
    def build(self):
        myAppLayout = MyAppLayout(orientation="vertical", padding=50, spacing=20)
        self.box = BoxLayout(orientation='vertical', padding=50, spacing=20)


        self.topRow = Label(text="MyApp", font_size=70, color=(1,1,1,1))
        self.mainPanel = self.getMainPanel()
        self.bottomRow = self.getBottomRow()
        self.box.add_widget(self.topRow)
        self.box.add_widget(self.mainPanel)
        self.box.add_widget(self.bottomRow)    
        myAppLayout.add_widget(self.box)
        return myAppLayout
    
    def getMainPanel(self):
        mainPanel = BoxLayout(orientation='vertical', padding=30, spacing=20)
        a = SquareButton(text="a", disabled=True) #Inactive
        b = SquareButton(text="b", disabled=True)
        c = SquareButton(text="c", disabled=True) #Inactive
        d = SquareButton(text="d", disabled=True)
        self.buttonRow = BoxLayout(orientation="vertical", padding = 10, spacing=20)
        self.buttonRow.add_widget(a)
        self.buttonRow.add_widget(b)
        self.buttonRow.add_widget(c)
        self.buttonRow.add_widget(d)
        mainPanel.add_widget(self.buttonRow)
        self.centerLabel = Label(text="Hello!", font_size=80, color=(1,1,1,1))
        mainPanel.add_widget(self.centerLabel)
        return mainPanel
        
    def getBottomRow(self):
        self.bottomRow = BoxLayout(orientation="horizontal", spacing=20, padding=50)
        return self.bottomRow

# if __name__ == '__main__':
#     MyApp().run()

def lo():
    """_summary_

    Returns:
        _type_: _description_
    """

class SquareButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = self.text
        self.color = (1,1,1,1)
        self.bold = True
        self.height = 70
        self.size_hint_y = None
        self.width = 70
        self.size_hint_x = None
        self.disabled = False

    def disable(self):
        self.disabled = True

    def enable(self):
        self.disabled = False

    def __str__(self):
        return 'SquareButton-' + self.text


MyApp().run()