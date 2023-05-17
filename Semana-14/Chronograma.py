import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window

from datetime import datetime

Window.size=(600, 400)
class Crono(App):

    def build(self):
        self.start = datetime.now()
        box = BoxLayout(orientation="horizontal", padding=40, spacing=20)
        buttonRow = BoxLayout(orientation="horizontal", padding=20, spacing=20)
        self.label=Label(text=self.getTime(), font_size=50, color=(1,1,1,1))
        box.add_widget(buttonRow)
        box.add_widget(self.label)
        self.button1 = Button(text="Start", font_size=50)
        self.button2 = Button(text="Reset", font_size = 50)
        buttonRow.add_widget(self.button1)
        buttonRow.add_widget(self.button2)
        self.button1.bind(on_press=self.startPausePressed) #Binds a function to the button
        self.button2.bind(on_press=self.resetPressed)
        # Define an attribute that will hold a periodic event for the
        # chronograph
        self.chronoEvent = None
        # the clock attribute is usefull for pause/resume operations
        self.clock = 0
        # we MUST return the main root widget:
        return box
    
    def setTimeValue(self, x):
        """
        setTimeValue Updates the label with elapsed time. This function
        is called periodically.
        """
        self.label.text = self.getTime()

    def startPausePressed(self, x):
        if self.button1.text == "Start":
            self.start = datetime.now()
            self.chronoEvent = Clock.schedule_interval(self.setTimeValue, 1.0/2.0)
            self.button1.text = "Pause"
        elif self.button1.text == 'Pause':
            self.clock = datetime.now()
            self.chronoEvent.cancel()
            self.button1.text = 'Resume'
        elif self.button1.text == 'Resume':
            self.start = datetime.now() - self.clock + self.start
            self.chronoEvent = Clock.schedule_interval(self.setTimeValue,
                                                       1.0/100)
            self.button1.text = 'Pause'

    def resetPressed(self, x):
        self.start = datetime.now()
        
    def getTime(self):
        """Gets the Elapsed time since start

        Returns:
            _datetime_: _time elapsed_
        """
        time = self.start - datetime.now()
        return str(time)[:-7]
    
    def setTimeLabel(self):
        self.label.text = self.getTime()
    
    def resetTime(self):
        self.start = datetime.now()

    
Crono().run()