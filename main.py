from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDTimePicker
# kivymd.uix.picker는 OutOfService now

from datetime import datetime

class MainApp(MDApp):

    def build(self):
        screen = Screen()
        self.alarm_time = "Fix your time"

        # button: open time picker
        button = MDRectangleFlatButton(text="Open Time Picker",
                                       pos_hint={'center_x':.5, 'center_y':.5},)
        button.bind(on_release=self.show_time_picker)
        screen.add_widget(button)

        # label: show the time
        self.label = MDLabel(text="Alarm : "+str(self.alarm_time),
                        pos_hint={'center_x':.8, 'center_y':.4},)
        screen.add_widget(self.label)

        return screen


    def show_time_picker(self, instance):
        time_dialog = MDTimePicker()
        time_dialog.set_time(self.chk_alarm_time())
        time_dialog.open()
        
        time_dialog.bind(on_save=self.set_time)

    def chk_alarm_time(self):
        if self.alarm_time == "Fix your time":
            set_time = datetime.strptime("00:00:00", "%H:%M:%S")
        else:
            set_time = self.alarm_time
        
        return set_time
    
    def set_time(self, instance, time):
        self.alarm_time = time
        self.label.text = "Alarm : " + str(self.alarm_time)
        

if __name__ == '__main__':
    MainApp().run()