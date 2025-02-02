import kivy
import kivymd
import google.generativeai as genai
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
#from chatterbot import chatbot
genai.configure(api_key=your_google_api_key)

class ChatMessage(MDCard):
    my_text = StringProperty()
    font_size = NumericProperty()

class ResPonse(MDCard):
    my_text = StringProperty()
    font_size = NumericProperty()

class ChatScreen(Screen):
    #chat_area  = ObjectProperty()
    message = ObjectProperty()

    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)

        #self.chatbot = chatbot("Donna")


    def send_message(self):
        self.user_input = self.ids.message.text
        self.ids.message.text = " "

        length = len(self.user_input)

        if length >= 40:
            self.ids.chat_area.add_widget(
                ChatMessage(my_text = self.user_input, font_size = 17, height = length)
            )

        else:
            self.ids.chat_area.add_widget(
                ChatMessage(my_text = self.user_input, font_size = 17)
            )
    
    def bot_response(self):
        model = genai.GenerativeModel("gemini-1.5-flash")

        Response = model.generate_content(self.user_input)
        length = len(Response.text)


        if length >= 40:
            self.ids.chat_area.add_widget(
                ResPonse(my_text = Response.text, font_size = 17, height = length)
            )

        else:
            self.ids.chat_area.add_widget(
                ResPonse(my_text = Response.text, font_size = 17)
            )
 

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
       
        ms = MDScreenManager()
        ms.add_widget(ChatScreen(name = "chat"))
        return ms


if __name__ == "__main__":
    MainApp().run()
