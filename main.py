from os import pathconf
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as sr
import threading


engine  = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

convo  = [
      
      'hello',
      'hi there !',
      'what is your name ?',
      'My name is Bot, I am created by Rahul. ',
      'How are you ?',
      'I am doing great these days',
      'Thank You',
      'In which city you live ?',
      'I live in India',
      'In which language do you talk?',
      'I mostly talk in English'
]

trainer = ListTrainer(bot)

# Training the bot with the help of trainers

trainer.train(convo)



## UI designing

main = Tk()

main.geometry("500x600+60+30")
main.title("My Chatbot")
img = PhotoImage(file ="bot1.png")

photo = Label(main,image=img)
photo.pack(pady=5)

# Taking audio from user and convert it to string

def takeQuery():
    srs = sr.Recognizer()
    srs.pause_threshold = 1
    print("Your Bot is listening try to speak")
    with sr.Microphone() as m:
        try:
            audio = srs.listen(m)
            query = srs.recognize_google(audio,language='eng-in')
            print(query)
            text.delete(0, END)
            text.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognised")


        

## Ask from bot function
def ask_from_bot():
    query = text.get()
    answer_from_bot =bot.get_response(query)
    messages.insert(END,"You : " +query)
    print(type(answer_from_bot))
    messages.insert(END, "Bot : " +str(answer_from_bot))

    speak(answer_from_bot)

    text.delete(0, END)
    messages.yview(END)

frame = Frame(main)
scroll_bar  = Scrollbar(frame)

messages = Listbox(frame, width=80, height=16, yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
messages.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

## Creating Text Field
text = Entry(main, font=("Times New Roman", 18))
text.pack(fill=X, pady=10)

btn = Button(main, text="Ask from Bot", font=('Times New Roman', 18),command=ask_from_bot)
btn.pack()

# Creating function 
def enter_function(event):
    btn.invoke()

# Bind main window with Enter key
main.bind('<Return>', enter_function)

def repeat_l():
    while True:
        takeQuery()


t=threading.Thread(target=repeat_l)
t.start()


main.mainloop()
